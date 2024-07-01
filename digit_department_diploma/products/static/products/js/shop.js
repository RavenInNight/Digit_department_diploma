let currentSlide=0;
const slides=document.querySelectorAll('.slide');

function showSlide(slideIndex) {
    slides.forEach(slide=> slide.style.display='none');
    slides[slideIndex].style.display='block';
}

function nextSlide() {
    currentSlide=(currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

setInterval(nextSlide, 3000);

function FindOnPage() {
    var input=document.getElementById('text-to-find').value;

    if (input.length < 3) {
        alert('Для поиска вы должны ввести три или более символов');
        return;
    }

    // Перенаправляем пользователя на новую страницу с учетом поискового запроса
    window.location.href='/search?query='+input;
}

document.addEventListener('DOMContentLoaded', function() {
        const categoryItems=document.querySelectorAll('.categoryitems');

        categoryItems.forEach(category=> {
                category.addEventListener('click', function(e) {
                        e.preventDefault(); // Отменяем стандартное действие ссылки

                        const target=e.target;
                        const wrapper=target.closest('.category-wrapper');
                        if ( !wrapper) return; // Если не нашли родительский элемент .category-wrapper, выходим

                        const arrow=wrapper.querySelector('.arrow');
                        const subcategories=wrapper.nextElementSibling;

                        // Закрываем все открытые категории, кроме текущей
                        document.querySelectorAll('.category-wrapper').forEach(item=> {
                                if (item !==wrapper && item.classList.contains('expanded')) {
                                    item.classList.remove('expanded');
                                    item.querySelector('.arrow').style.transform='rotate(90deg)';
                                    item.nextElementSibling.style.display='none';
                                }
                            });

                        // Открываем/закрываем текущую категорию
                        wrapper.classList.toggle('expanded');
                        arrow.style.transform=wrapper.classList.contains('expanded') ? 'rotate(0deg)' : 'rotate(90deg)';
                        subcategories.style.display=wrapper.classList.contains('expanded') ? 'block' : 'none';
                    });
            });

        const subcategoriesItems=document.querySelectorAll('.subcategories > li');

        subcategoriesItems.forEach(item=> {
                item.addEventListener('click', function() {
                        const subSubcategories=item.querySelector(".sub-subcategories");

                        // Закрываем все открытые третьи списки, кроме текущего
                        document.querySelectorAll('.sub-subcategories').forEach(sub=> {
                                if (sub !==subSubcategories && sub.style.display==='block') {
                                    sub.style.display='none';
                                }
                            });

                        if (subSubcategories.style.display==='none' || subSubcategories.style.display==='') {
                            subSubcategories.style.display='block';
                        }

                        else {
                            subSubcategories.style.display='none';
                        }
                    });
            });
    });

document.querySelectorAll('.favorite-btn').forEach(btn=> {
        btn.addEventListener('click', function() {
                console.log('Товар добавлен в избранное');
                document.getElementById('favorite-success-message').style.display='block';

                setTimeout(()=> {
                        document.getElementById('favorite-success-message').style.display='none';
                    }

                    , 5000); // Скрыть сообщение через 3 секунды
            });
    });

document.querySelectorAll('.cart-btn').forEach(btn=> {
        btn.addEventListener('click', function() {
                console.log('Товар добавлен в корзину');
                document.getElementById('cart-success-message').style.display='block';

                setTimeout(()=> {
                        document.getElementById('cart-success-message').style.display='none';
                    }

                    , 15000); // Скрыть сообщение через 3 секунды
            });
    });