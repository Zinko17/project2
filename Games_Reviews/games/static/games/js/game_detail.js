document.addEventListener('DOMContentLoaded', function () {
    // Находим все элементы с классом game-card-image
    const gameCardImages = document.querySelectorAll('.game-card-image');

    // Перебираем найденные элементы
    gameCardImages.forEach(image => {
        // Добавляем обработчик события наведения мыши
        image.addEventListener('mouseover', function () {
            // Увеличиваем размер изображения
            image.style.transform = 'scale(1.1)';
            image.style.transition = 'transform 0.3s ease';
        });

        // Добавляем обработчик события ухода мыши
        image.addEventListener('mouseout', function () {
            // Возвращаем изначальный размер изображения
            image.style.transform = 'scale(1)';
        });
    });
});