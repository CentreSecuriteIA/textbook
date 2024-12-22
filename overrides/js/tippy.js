// File: docs/js/tippy.js

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
            appendTo: document.body,
            delay: [100, 50],
            duration: [200, 150],
            maxWidth: 300,
            offset: [0, 12]
        });
        
        // Store title and remove it to prevent default tooltip
        if (abbr.hasAttribute('title')) {
            abbr.setAttribute('data-original-title', abbr.getAttribute('title'));
            abbr.removeAttribute('title');
        }
    });
}

// Initialize on first load
document.addEventListener('DOMContentLoaded', initializeTippy);

// Handle MkDocs page changes
document$.subscribe(() => {
    // Small delay to ensure DOM is fully updated
    setTimeout(initializeTippy, 100);
});

// Initialize tooltips for disabled buttons
function initializeDisabledTooltips() {
    tippy('.action-button.disabled', {
        theme: 'elegant',
        placement: 'top',
        arrow: true,
        animation: 'fade',
        duration: [0, 0],
        hideOnClick: false,
    });
}

// Initialize disabled tooltips on first load
document.addEventListener('DOMContentLoaded', initializeDisabledTooltips);

// Handle MkDocs page changes for disabled tooltips
document$.subscribe(initializeDisabledTooltips);
