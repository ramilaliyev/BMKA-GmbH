var winWidth = window.outerWidth;

if (winWidth <= 990) {
    document.getElementById('footer-nav').classList.add('container-fluid')
    document.getElementById('intro-logo').classList.add('d-block');
    document.getElementById('intro-logo').classList.add('mx-auto');
    document.getElementById('nav').classList.remove('container');
    document.getElementById('nav').classList.add('container-fluid');
    document.getElementById('footer-links').classList.remove('container');
    document.getElementById('footer-links').classList.add('container-fluid')
} else {
    document.getElementById('nav').classList.add('container');
    document.getElementById('intro-logo').classList.remove('d-block');
    document.getElementById('intro-logo').classList.remove('mx-auto');
    document.getElementById('nav').classList.remove('container-fluid');
    document.getElementById('footer-links').classList.add('container');
}