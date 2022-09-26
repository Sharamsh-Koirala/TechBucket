(function() {

    "use strict";

    $(window).on("scroll", function() {
        if($(window).scrollTop() > 50) {
            $(".header").addClass("header-scrolled");
        } else {
            $(".header").removeClass("header-scrolled");
        }
    });

    document.getElementById("productDetailPage").onclick = function () {
        location.href = '../pages/product-details.html'
    };

    
    
})()




