/* File: docs/overrides/js/home/hero.js */
document.addEventListener('DOMContentLoaded', function() {
    // Handle card interactions on mobile
    if (window.innerWidth <= 768) {
        const cards = document.querySelectorAll('.atlas-card');
        cards.forEach(card => {
            let isFlipped = false;
            card.addEventListener('click', (e) => {
                if (!isFlipped) {
                    e.preventDefault();
                    card.style.transform = 'rotate(-5deg) scale(1.1)';
                    card.querySelector('.atlas-card__content').style.opacity = '1';
                    card.querySelector('.atlas-card__content').style.transform = 'translate(-50%, -50%) rotate(0deg)';
                    isFlipped = true;
                }
            });
        });
    }
});
