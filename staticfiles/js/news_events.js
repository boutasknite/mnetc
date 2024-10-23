

function Switch(id_to_show, ids_to_remove) {

    document.getElementById(id_to_show).classList.add('active');
    document.getElementById(id_to_show.slice(0, -4)).style.display = 'block';
    var i=0;
    for(i=0; i < ids_to_remove.length; i++){
        document.getElementById(ids_to_remove[i]).classList.remove('active');
        document.getElementById(ids_to_remove[i].slice(0, -4)).style.display = 'none';
    }
}







document.addEventListener('DOMContentLoaded', function () {
var swiper = new Swiper('.swiper-container', {
    loop: true,
    speed: 600,
    autoplay: {
        delay: 5000
    },
    slidesPerView: 'auto',
    spaceBetween: 20,
    pagination: {
        el: '.swiper-pagination',
        type: 'bullets',
        clickable: true
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 10
        },
        1200: {
            slidesPerView: 3,
            spaceBetween: 20
        }
    }
});
});
