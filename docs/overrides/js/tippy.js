// Wait for document load
document.addEventListener('DOMContentLoaded', () => {
    initializeTippy();
    
    // Watch for navigation changes using MkDocs' event system
    document$.subscribe(() => {
        // Small delay to ensure DOM is fully updated
        setTimeout(initializeTippy, 200);
    });
});

function initializeTippy() {
    // Get all abbr elements
    const abbrs = document.querySelectorAll('.md-typeset abbr');
    
    // Remove any existing tippy instances to prevent duplicates
    abbrs.forEach(abbr => {
        if (abbr._tippy) {
            abbr._tippy.destroy();
        }
    });

    // Initialize tippy for each abbr
    abbrs.forEach(abbr => {
        tippy(abbr, {
            content: abbr.getAttribute('title') || abbr.getAttribute('data-original-title'),
            allowHTML: true,
            placement: 'top',
            theme: 'elegant',
            animation: 'perspective-extreme',
            arrow: true,
            appendTo: document.body, // Ensures proper positioning
            delay: [100, 50],
            duration: [200, 150],
            maxWidth: 300,
            offset: [0, 12],
            onMount(instance) {
                // Ensure arrow is visible after mount
                const box = instance.popper.querySelector('.tippy-box');
                if (box) {
                    box.style.opacity = '1';
                }
            }
        });
        
        // Store title and remove it to prevent default tooltip
        if (abbr.hasAttribute('title')) {
            abbr.setAttribute('data-original-title', abbr.getAttribute('title'));
            abbr.removeAttribute('title');
        }
    });
}
