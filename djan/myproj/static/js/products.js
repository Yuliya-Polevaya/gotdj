
document.addEventListener('DOMContentLoaded', function () {

    const filterButtons = document.querySelectorAll('.filter-button');
    const productCards = document.querySelectorAll('.catalog-card');
    const productCount = document.getElementById('product-count');
    const noProducts = document.getElementById('no-products');

    filterButtons.forEach(function (button) {

        button.addEventListener('click', function () {

            const selectedCategory = this.dataset.category;
            let visibleCount = 0;

            // Переключаем активную кнопку
            filterButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });

            this.classList.add('active');

            // Показываем товары выбранной категории
            productCards.forEach(function (card) {

                const cardCategory = card.dataset.category;

                if (
                    selectedCategory === 'all' ||
                    cardCategory === selectedCategory
                ) {
                    card.hidden = false;
                    visibleCount++;
                } else {
                    card.hidden = true;
                }

            });

            // Обновляем количество товаров
            productCount.textContent = visibleCount;

            // Показываем сообщение, если товаров нет
            noProducts.hidden = visibleCount !== 0;

        });

    });

});
