$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        loop: true,
        items: 4,
        autoplay: true,
        autoplaySpeed: 1000,
        margin: 20,
        responsiveClass: true,
        responsive:{

            0:{
    
                items:1
    
            },
    
            600:{
    
                items:1
    
            },
    
            1000:{
    
                items:4,
    
                loop:true
    
            }
    
        }
    });
});