/* File: docs/overrides/js/home/header.js */
document.addEventListener('DOMContentLoaded', function() {
    if (!document.body.classList.contains('is-home-page')) return;
    
    const header = document.querySelector('.md-header');
    let isHeaderVisible = false;
    let lastScrollY = window.scrollY;
    
    function toggleHeader(show) {
        header.classList.toggle('header-visible', show);
        isHeaderVisible = show;
    }
    
    // Show header when mouse is near top
    document.addEventListener('mousemove', (e) => {
        if (e.clientY < 60) {
            toggleHeader(true);
        } else if (window.scrollY < 100) {
            toggleHeader(false);
        }
    });
    
    // Handle scroll
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        // Show header when scrolling up, hide when scrolling down
        if (scrollY < lastScrollY) {
            toggleHeader(true);
        } else if (scrollY > 100 && scrollY > lastScrollY) {
            toggleHeader(false);
        }
        
        lastScrollY = scrollY;
    });
});
