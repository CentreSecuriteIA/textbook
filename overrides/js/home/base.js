/* File: docs/overrides/js/home/base.js */

document.addEventListener('DOMContentLoaded', () => {
    // Handle hero section
    const heroElement = document.querySelector('[data-mdx-component="hero"]');
    if (heroElement) {
        mountHero(heroElement);
    }

    // Handle stat cards animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.visibility = 'visible';
                observer.unobserve(entry.target);
            }
        });
    });

    document.querySelectorAll('.atlas-stat-card').forEach((card, index) => {
        card.style.animationDelay = `${0.2 * index}s`;
        observer.observe(card);
    });
});
