function initSwipers() {
  const swiperItems = new Swiper('.item-swiper', {
    spaceBetween: 0,
    speed: 700,
    centeredSlides: true,
    loop: true,
    autoplay: {
      pauseOnMouseEnter: true,
      delay: 4500,
      disableOnInteraction: false,
    },
  });

  const swiperBigMain = new Swiper('.swiper-inozemcevo', {
    spaceBetween: 0,
    speed: 800,
    loop: true,
    centeredSlides: true,
    autoplay: {
      delay: 8500,
      disableOnInteraction: false,  
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  const swiperReviews = new Swiper(".reviewSwiper", {
    direction: "vertical",
    loop: true,
    speed: 900,
    effect: 'coverflow',
    coverflowEffect: {
      rotate: 30,
      stretch: 10,
      depth: 100,
      modifier: 2,
      slideShadows: true,
    },
    autoplay: {
      pauseOnMouseEnter: true,
      delay: 40000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
}


function animateLines() {
  const lines = document.querySelectorAll(".animated-line");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.5
  });

  lines.forEach((line) => {
    observer.observe(line);
  })
}

function setOnRoomsHover() {
  const texts = document.querySelectorAll('.swiper');
  texts.forEach(el => {
    const fixedHoverText = el.querySelector('.fixed-hover-text');
    if (fixedHoverText) {
      el.addEventListener('mouseenter', () => {
        fixedHoverText.style.display = 'block';
      })
      el.addEventListener('mouseleave', () => {
        fixedHoverText.style.display = 'none';
      })
    }
  })
}

function initYanexMap() {
  ymaps.ready(init);
  function init() {
    const myMap = new ymaps.Map("map", {
      center: [44.096305, 43.087160],
      zoom: 17,
      controls: ['zoomControl', 'searchControl', 'typeSelector', 'fullscreenControl']
    })

    const myPlacemark = new ymaps.Placemark([44.096305, 43.087160], {
      hintContent: '!',
      balloonContent: 'Столица России',
      preset: 'islands#icon',
      iconColor: '#0095b6'
    });

    myMap.geoObjects.add(myPlacemark);
  };
}

function animateBookmarks() {
  const bookmarks = document.querySelectorAll(".bookmark-container-animated");
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-bookmark');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0
  });

  bookmarks.forEach((bookmark) => {
    observer.observe(bookmark);
  })
}

function main() {
  animateLines();
  setOnRoomsHover();
  initSwipers();
  animateBookmarks();
  // initYanexMap();
}


document.addEventListener("DOMContentLoaded", main);

