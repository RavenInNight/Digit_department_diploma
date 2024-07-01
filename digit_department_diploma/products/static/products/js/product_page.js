
function displayImage(imageUrl) {
    mainImage.src = imageUrl;
    mainImage.classList.add('zoomed');

    mainImage.addEventListener('click', function () {
        zoomedImage.src = mainImage.src;
        document.body.appendChild(zoomedImage);
        zoomedImage.addEventListener('click', function () {
            document.body.removeChild(zoomedImage);
            zoomedImage.classList.remove('full-screen');
        });
    });
}

function displayImage(imageUrl) {
    mainImage.src = imageUrl;
    mainImage.classList.add('zoomed');
};

document.querySelector('.main-slide').addEventListener('click', function () {
    if (this.classList.contains('zoomed')) {
        this.classList.remove('zoomed');
        document.querySelector('.zoom-in').remove();
    } else {
        this.classList.add('zoomed');
        var zoomInButton = document.createElement('div');
        zoomInButton.classList.add('zoom-in');
        zoomInButton.innerHTML = '✖';
        zoomInButton.addEventListener('click', function () {
            document.querySelector('.main-slide').classList.remove('zoomed');
            this.remove();
        });
        document.body.appendChild(zoomInButton);
    }
});

function displayImage(imageUrl) {
    mainImage.src = imageUrl;
    mainImage.classList.remove('zoomed');
}

document.querySelector('.prev').addEventListener('click', function () {
    slideIndex--;
    showSlides();
});

document.querySelector('.next').addEventListener('click', function () {
    slideIndex++;
    showSlides();
});

var slideIndex = 0;
var slides = document.getElementsByClassName('slide');
var thumbnails = document.getElementsByClassName('thumbnail');
var mainImage = document.querySelector('.main-slide');
var zoomedContainer = document.createElement('div');
zoomedContainer.classList.add('zoomed-container');
var zoomedImage = document.createElement('img');
zoomedImage.classList.add('zoomed-image');

function showSlides() {
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    } else if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }

    for (var i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }

    slides[slideIndex].style.display = 'block';
}
function displayImageZoomed(imageUrl) {
    mainImage.src = imageUrl;
    mainImage.classList.add('zoomed');
    var closeButton = document.createElement('div');
    closeButton.classList.add('close-button');
    closeButton.innerHTML = '✖';
    closeButton.addEventListener('click', function () {
        mainImage.classList.remove('zoomed');
        this.remove();
    });
    mainImage.appendChild(closeButton);
}

function displayImageZoomed(imageUrl) {
    mainImage.src = imageUrl;
    mainImage.classList.add('zoomed');
}

mainImage.addEventListener('click', function () {
    zoomedImage.src = mainImage.src;
    zoomedImage.classList.add('full-screen');
    document.body.appendChild(zoomedImage);
});

document.querySelectorAll('.thumbnail').forEach(thumbnail => {
    thumbnail.addEventListener('click', function () {
        displayImage(this.src);
    });
});

for (var i = 0; i < thumbnails.length; i++) {
    thumbnails[i].addEventListener('click', function () {
        displayImage(this.src);
    });
}

document.querySelectorAll('.thumbnail').forEach(thumbnail => {
    thumbnail.addEventListener('mouseover', function () {
        document.querySelector('.main-slide').src = this.src;
    });

    thumbnail.addEventListener('click', function (event) {
        event.stopPropagation();
        document.querySelector('.main-slide').src = this.src;
    });
});

mainImage.addEventListener('mousemove', function (event) {
    if (mainImage.classList.contains('zoomed')) {
        var x = event.clientX;
        var y = event.clientY;

        zoomedImage.src = mainImage.src;
        zoomedImage.style.left = x + 'px';
        zoomedImage.style.top = y + 'px';

        if (!document.body.contains(zoomedContainer)) {
            zoomedContainer.appendChild(zoomedImage);
            document.body.appendChild(zoomedContainer);
        }
    }
});

showSlides();

$(document).ready(function () {
    $('.add-to-wishlist').click(function (e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: '{% url 'wishlist' %}',
            data: {
                'product_id': {{ product.id }},
        'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
    success: function (response) {
        $('#wishlist-message').text('Товар добавлен в избранное').show();
    },
    error: function (xhr, errmsg, err) {
        $('#wishlist-message').text('Произошла ошибка при добавлении товара в избранное').show();
    }
        });
    });
});  