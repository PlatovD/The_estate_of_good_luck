const swiper = new Swiper(".swiperRoomInfo", {
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    loop: true,
    autoplay: {
        delay: 6500,
        disableOnInteraction: false,
        pauseOnMouseEnter: true,
    },

});

function fullScreenGalery() {
    document.querySelector(".swipper-fullscreen").addEventListener('click', e => {
        fsLightbox.open();
    })
}

fullScreenGalery();