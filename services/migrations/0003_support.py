# Generated by Django 4.0.5 on 2022-06-29 05:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('issue', models.CharField(max_length=200)),
                ('details', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
