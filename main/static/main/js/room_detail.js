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
        delay: 4500,
        disableOnInteraction: false,
        speed: 5000,
        pauseOnMouseEnter: true,
    },

});