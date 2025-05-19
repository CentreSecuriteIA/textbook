/* File: docs/overrides/js/tippy.js */

// Wait for document load
document.addEventListener('DOMContentLoaded', () => {
    initializeTippy();
    
    // Watch for navigation changes using MkDocs' event system
    document$.subscribe(() => {
        // Small delay to ensure DOM is fully updated
        setTimeout(initializeTippy, 200);
    });
});

function removeAllMaterialTooltips() {
    // Remove all tooltip elements that might exist
    document.querySelectorAll('[id^="__tooltip"]').forEach(tooltip => tooltip.remove());
    
    // Remove all aria-describedby attributes
    document.querySelectorAll('[aria-describedby]').forEach(el => {
        el.removeAttribute('aria-describedby');
    });
}

function initializeTippy() {
    // First remove any Material tooltips
    removeAllMaterialTooltips();
    
    // Set up a mutation observer to catch any dynamically added tooltips
    const observer = new MutationObserver((mutations) => {
        mutations.forEach((mutation) => {
            mutation.addedNodes.forEach((node) => {
                if (node.id && node.id.startsWith('__tooltip')) {
                    node.remove();
                }
            });
        });
    });

    observer.observe(document.body, { childList: true, subtree: true });

    // First, remove all abbr styling from excluded locations
    const excludedAbbrs = document.querySelectorAll(`
        h1 abbr, h2 abbr, h3 abbr, h4 abbr, h5 abbr, h6 abbr,
        a abbr,
        button abbr,
        .md-nav__link abbr,
        .md-header__inner abbr,
        .md-footer abbr,
        .md-tabs abbr
    `);
    
	excludedAbbrs.forEach(abbr => {
    abbr.className = 'excluded-abbr';
    if (abbr._tippy) {
        abbr._tippy.destroy();
    }
    abbr.removeAttribute('title');
    abbr.removeAttribute('data-original-title');
    // Remove any inline styles that might have been added
    abbr.style.removeProperty('text-decoration');
    abbr.style.removeProperty('cursor');
    abbr.style.removeProperty('border-bottom');
});

    // Then initialize Tippy only on remaining abbrs
    const abbrs = document.querySelectorAll('.md-typeset abbr:not(.excluded-abbr)');
    
    abbrs.forEach(abbr => {
        if (
            abbr.closest('a') || 
            abbr.closest('button') || 
            abbr.closest('h1, h2, h3, h4, h5, h6') || 
            abbr.closest('.md-nav__link') || 
            abbr.closest('.md-header__inner') || 
            abbr.closest('.md-footer') || 
            abbr.closest('.md-tabs')
        ) {
            // Add the class to prevent styling
            abbr.className = 'excluded-abbr';
            return;
        }

        if (abbr._tippy) {
            abbr._tippy.destroy();
        }

        tippy(abbr, {
            content: abbr.getAttribute('data-original-title') || abbr.getAttribute('title'),
            allowHTML: true,
            placement: 'top',
            theme: 'elegant',
            animation: 'perspective-extreme',
            arrow: true,
            appendTo: document.body,
            delay: [100, 50],
            duration: [200, 150],
            maxWidth: 300,
            offset: [0, 12],
            trigger: 'mouseenter click',
            hideOnClick: false,
            interactive: true,
            onMount(instance) {
                removeAllMaterialTooltips();
                const box = instance.popper.querySelector('.tippy-box');
                if (box) {
                    box.style.opacity = '1';
                }
            }
        });
        
        // Add click handler to close tooltip when clicking elsewhere
        document.addEventListener('click', (event) => {
            if (!abbr.contains(event.target) && 
                !event.target.closest('.tippy-box')) {
                if (abbr._tippy) {
                    abbr._tippy.hide();
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

// Initialize tooltips for action buttons
document.addEventListener('DOMContentLoaded', () => {
    tippy('.action-button.disabled', {
        theme: 'elegant',
        placement: 'top',
        arrow: true,
        animation: 'fade',
        duration: [0, 0],
        hideOnClick: false,
    });
});
