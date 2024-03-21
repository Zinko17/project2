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

    // При нажатии на карточку игры
    const gameCards = document.querySelectorAll('.game-card');
    gameCards.forEach(card => {
        card.addEventListener('click', function () {
            const gameId = card.dataset.gameId; // Получаем ID игры из data-атрибута
            window.location.href = `/game/${gameId}/`; // Перенаправляем на страницу с подробным описанием игры
        });
    });
});
