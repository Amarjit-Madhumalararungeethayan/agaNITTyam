// static/script.js

document.addEventListener('mousemove', function(e) {
    const star = document.createElement('div');
    star.classList.add('star');
    star.style.left = e.pageX + 'px';
    star.style.top = e.pageY + 'px';
    document.body.appendChild(star);

    setTimeout(() => {
        star.remove();
    }, 2000); // Adjust timeout to match animation duration
});
