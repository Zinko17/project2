document.addEventListener('DOMContentLoaded', function () {
    /// При нажатии на карточку игры
    const gameCards = document.querySelectorAll('.game-card');
    gameCards.forEach(card => {
        card.addEventListener('click', function () {
            const gameId = card.dataset.gameId; // Получаем ID игры из data-атрибута
            window.location.href = `/game/${gameId}/`; // Перенаправляем на страницу с подробным описанием игры
        });
    });
});