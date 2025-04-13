function copyText(event) {
    const text = event.target.innerText;
    navigator.clipboard.writeText(text);
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".dropdown").forEach(dropdown => {
        const dropdownContent = dropdown.querySelector(".dropdown-content");

        dropdown.addEventListener("mouseenter", () => {
            dropdownContent.style.display = "flex";
            dropdown.querySelector("img").style.transform = "rotate(180deg)";
        });

        dropdown.addEventListener("mouseleave", () => {
            dropdownContent.style.display = "none";
            dropdown.querySelector("img").style.transform = "rotate(0deg)";
        });
    });

    document.querySelector(".burger").addEventListener('click', () => {
        const navMobile = document.querySelector(".mobile-burger-dropdown-nav");
        if (navMobile.style.left !== '60%') {
            navMobile.style.left = '60%';
        } else {
            navMobile.style.left = '100%';
        }
    })

    document.querySelectorAll(".mobile-dropdown-trigger").forEach(el => {
        el.addEventListener('click', e => {
            e.preventDefault();
            let dropdown = el.querySelector('.header-dropdown');
            if (dropdown.style.display === "none" || dropdown.style.display == "") {
                dropdown.style.display = "flex";

            } else {
                dropdown.style.display = "none";
            }
        })
    })



    document.querySelector("#book-menu-close-btn").addEventListener('click', e => {
        closeBookingDialog();
    })

    document.querySelector("#book-header").addEventListener('click', e => {
        blockWindow = document.querySelector(".book-block");
        if (blockWindow.style.display === 'flex') {
            closeBookingDialog();
            return;
        }
        mainContainer = document.querySelector(".main-container");
        mainContainer.classList.toggle("main-container-after");
        blockWindow.style.display = "flex";
    })

});

window.addEventListener('scroll', function () {
    if (this.screen.width < 800) {
        return;
    }
    const nav = document.querySelector('.nav');
    if (window.scrollY > 110) {
        nav.classList.add('sticky');
    } else {
        nav.classList.remove('sticky');
    }
});

window.addEventListener('scroll', function () {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = window.scrollY;
    const progress = scrollHeight > 0 ? (scrolled / scrollHeight) * 100 : 0;
    document.querySelector('#progress-line-mobile').style.width = Math.min(progress, 100) + '%';
});



function closeBookingDialog() {
    blockWindow = document.querySelector(".book-block");
    mainContainer = document.querySelector(".main-container");
    mainContainer.classList.toggle("main-container-after");
    blockWindow.style.display = "none";
}

