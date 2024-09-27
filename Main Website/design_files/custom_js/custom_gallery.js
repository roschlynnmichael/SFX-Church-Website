document.addEventListener('DOMContentLoaded', function() {
    var carousels = document.querySelectorAll('.carousel');
    carousels.forEach(function(carousel) {
        new mdb.Carousel(carousel, {
            interval: 3000,
            touch: false
        });
    });
});