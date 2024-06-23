  var cartItemsCount = 0;

    function updateCartCounter() {
        var cartCounter = document.getElementById("cart-counter");
        if (cartCounter) {
            cartCounter.innerText = cartItemsCount;
        }
    }

    function addToCart() {
        cartItemsCount++;
        updateCartCounter();
    }

    function removeFromCart() {
        if (cartItemsCount > 0) {
            cartItemsCount--;
            updateCartCounter();
        }
    }

    // Вызов функции для обновления счетчика при загрузке страницы
    window.onload = updateCartCounter;

    $(document).ready(function() {
      var menu = $(".menu");
      var menuOffset = menu.offset().top;

      $(window).scroll(function() {
          if ($(window).scrollTop() >= menuOffset) {
              menu.addClass("fixed");
          } else {
              menu.removeClass("fixed");
          }
      });
  });
  $(window).scroll(function() {
  if ($(this).scrollTop() > 100) {
      $('.menu').addClass('fixed');
  } else {
      $('.menu').removeClass('fixed');
  }
  });

  $(document).ready(function() {
    var currentLocation = window.location.href;
    
    $(".menu-list a").each(function() {
        if ($(this).attr("href") == currentLocation) {
            $(this).addClass("active");
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
  const dropdownMenu = document.querySelector('.dropdown-menu');
  dropdownMenu.style.display = 'none';

  const subLists = document.querySelectorAll('.sub-list');
  subLists.forEach(function(subList) {
    subList.style.display = 'none';
  });

  const subSubLists = document.querySelectorAll('.sub-sub-list');
  subSubLists.forEach(function(subSubList) {
    subSubList.style.display = 'none';
  });
  const dropdownToggle = document.querySelector('.dropdown-toggle');

  dropdownToggle.addEventListener('click', function() {
    dropdownMenu.style.display = (dropdownMenu.style.display === 'none' || dropdownMenu.style.display === '') ? 'block' : 'none';
  });

  const mainListItems = document.querySelectorAll('.main-list > li');

  mainListItems.forEach(function(item) {
    item.addEventListener('click', function(e) {
      e.stopPropagation();
      const subList = this.querySelector('.sub-list');
      if (subList) {
        mainListItems.forEach(function(otherItem) {
          if (otherItem !== item) {
            const otherSubList = otherItem.querySelector('.sub-list');
            if (otherSubList) {
              otherSubList.style.display = 'none';
              otherItem.classList.remove('selected');
            }
          }
        });
        subList.style.display = (subList.style.display === 'none' || subList.style.display === '') ? 'block' : 'none';
        this.classList.toggle('selected');
      }
    });
  });

  const subListItems = document.querySelectorAll('.sub-list > li');
  const subSubListItems = document.querySelectorAll('.sub-sub-list');

  subListItems.forEach(function(item) {
    item.addEventListener('click', function(e) {
      e.stopPropagation();
      const subList = this.querySelector('.sub-sub-list');
      if (subList) {
        subSubListItems.forEach(function(otherItem) {
          if (otherItem !== subList) {
            otherItem.style.display = 'none';
            otherItem.classList.remove('selected');
          }
        });
        subList.style.display = (subList.style.display === 'none' || subList.style.display === '') ? 'block' : 'none';
        this.classList.toggle('selected');
      }
    });
  });

  subSubListItems.forEach(function(item) {
    item.addEventListener('click', function(e) {
      e.stopPropagation();
      // Д
    });
  });
});

var range = document.getElementById('scroll-range');
range.addEventListener('mousedown', function(e) {
    e.preventDefault();
    var startY = e.clientY;
    var startScroll = window.pageYOffset;
    
    function move(e) {
        var diffY = e.clientY - startY;
        var newScroll = startScroll - diffY;
        window.scrollTo(0, newScroll);
    }
    
    function up(e) {
        document.removeEventListener('mousemove', move);
        document.removeEventListener('mouseup', up);
    }
    
    document.addEventListener('mousemove', move);
    document.addEventListener('mouseup', up);
});

window.onscroll = function() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scroll-range").classList.add("show");
    } else {
        document.getElementById("scroll-range").classList.remove("show");
    }
};


var range = document.getElementById('scroll-range');
range.addEventListener('mousedown', function(e) {
  e.preventDefault();
  var startY = e.clientY;
  var startScroll = window.pageYOffset;
  
  function move(e) {
    var diffY = e.clientY - startY;
    var newScroll = startScroll - diffY;
    window.scrollTo(0, newScroll);
  }
  
  function up(e) {
    document.removeEventListener('mousemove', move);
    document.removeEventListener('mouseup', up);
  }
  
  document.addEventListener('mousemove', move);
  document.addEventListener('mouseup', up);
});
