from .models import Service
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateServices(request, services, results):

    page = request.GET.get('page')
    paginator = Paginator(services, results)

    try:
        services = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        services = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        services = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, services


def searchServices(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')


    services = Service.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query)
    )
    return services, search_query
