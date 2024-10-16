// File: docs/overrides/js/toc-collapse.js

document.addEventListener('DOMContentLoaded', function() {
    const tocItems = document.querySelectorAll('.md-nav__item--section');
    
    function closeOtherChapters(currentItem) {
        tocItems.forEach(item => {
            if (item !== currentItem && item.classList.contains('md-nav__item--active')) {
                item.classList.remove('md-nav__item--active');
                const nestedNav = item.querySelector('.md-nav');
                if (nestedNav) {
                    nestedNav.style.display = 'none';
                }
            }
        });
    }

    tocItems.forEach(item => {
        const link = item.querySelector('.md-nav__link');
        const nestedNav = item.querySelector('.md-nav');

        if (link && nestedNav) {
            link.addEventListener('click', function(e) {
                // Don't prevent default behavior
                
                // Close other chapters
                closeOtherChapters(item);

                // Toggle current chapter
                setTimeout(() => {
                    if (item.classList.contains('md-nav__item--active')) {
                        nestedNav.style.display = 'block';
                    } else {
                        nestedNav.style.display = 'none';
                    }
                }, 0);
            });
        }
    });
});
