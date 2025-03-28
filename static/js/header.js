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
        if (navMobile.style.left === '100%') {
            navMobile.style.left = '0';
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

});

window.addEventListener('scroll', function () {
    if (this.screen.width < 800) {
        return;
    }
    const nav = document.querySelector('.nav');
    if (window.scrollY > 65) {
        nav.classList.add('sticky');
    } else {
        nav.classList.remove('sticky');
    }
});

