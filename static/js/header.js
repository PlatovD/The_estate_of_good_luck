function copyText(event) {
    const text = event.target.innerText;
    navigator.clipboard.writeText(text);
}

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".dropdown").forEach(dropdown => {
        const dropdownContent = dropdown.querySelector(".dropdown-content");

        dropdown.addEventListener("mouseenter", () => {
            dropdownContent.style.display = "flex";
        });

        dropdown.addEventListener("mouseleave", () => {
            dropdownContent.style.display = "none";
        });
    });
});
