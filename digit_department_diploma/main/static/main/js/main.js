let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(slideIndex) {
    slides.forEach(slide => slide.style.display = 'none');
    slides[slideIndex].style.display = 'block';
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
}

setInterval(nextSlide, 3000);

type = "text/javascript" >
    ddaccordion.init({
        headerclass: "expandable",
        contentclass: "categoryitems",
        revealtype: "clickgo",
        mouseoverdelay: 200,
        collapseprev: true,
        defaultexpanded: [0],
        onemustopen: false,
        animatedefault: false,
        persiststate: true,
        toggleclass: ["", "openheader"],
        togglehtml: ["prefix", "", ""],
        animatespeed: "fast",
        oninit: function (headers, expandedindices) {
            //do nothing
        },
        onopenclose: function (header, index, state, isuseractivated) {
            //do nothing
        }
    })