document.addEventListener('DOMContentLoaded', function () {
    const prevButton = document.querySelector('.prev-slide');
    const nextButton = document.querySelector('.next-slide');
    const sliderRow = document.querySelector('.slider-row');

    let slideIndex = 0;
    const slides = document.querySelectorAll('.game-card');
    const totalSlides = slides.length;
    const slideWidth = slides[0].offsetWidth + parseInt(getComputedStyle(slides[0]).marginRight);

    // При нажатии на кнопку "вперед"
    nextButton.addEventListener('click', function () {
        slideIndex++;
        if (slideIndex > totalSlides - 4) {
            slideIndex = totalSlides - 4;
        }
        sliderRow.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
    });

    // При нажатии на кнопку "назад"
    prevButton.addEventListener('click', function () {
        slideIndex--;
        if (slideIndex < 0) {
            slideIndex = 0;
        }
        sliderRow.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
    });
});
