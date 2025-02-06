<!-- File: docs/overrides/js/scroll-animations.js -->
document.addEventListener('DOMContentLoaded', () => {
    // Create the observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            // Add animation classes when element comes into view
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                // Unobserve after animation is triggered
                observer.unobserve(entry.target);
            }
        });
    }, {
        // Start animation when element is 10% in view
        threshold: 0.1,
        // Start when element is 50px from viewport
        rootMargin: '-50px'
    });

    // Observe all animated elements
    document.querySelectorAll('.animate-on-scroll').forEach((element) => {
        observer.observe(element);
    });
});
