document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('abbr[title]');
    
    tooltips.forEach(tooltip => {
        const tooltipText = tooltip.getAttribute('title');
        tooltip.removeAttribute('title');
        
        // Create a wrapper span for the glossary term
        const wrapper = document.createElement('span');
        wrapper.className = 'glossary-term';
        tooltip.parentNode.insertBefore(wrapper, tooltip);
        wrapper.appendChild(tooltip);
        
        const tooltipElement = document.createElement('span');
        tooltipElement.className = 'md-tooltip';
        tooltipElement.textContent = tooltipText;
        wrapper.appendChild(tooltipElement);
        
        wrapper.addEventListener('click', function(e) {
            e.preventDefault();
            tooltipElement.classList.toggle('stick');
            adjustTooltipPosition();
        });
        
        document.addEventListener('click', function(e) {
            if (!wrapper.contains(e.target)) {
                tooltipElement.classList.remove('stick');
            }
        });

        // Adjust tooltip position if it goes off-screen
        window.addEventListener('resize', adjustTooltipPosition);
        wrapper.addEventListener('mouseenter', adjustTooltipPosition);
        
        function adjustTooltipPosition() {
            const wrapperRect = wrapper.getBoundingClientRect();
            const tooltipRect = tooltipElement.getBoundingClientRect();
            const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
            const viewportHeight = window.innerHeight || document.documentElement.clientHeight;

            // Reset positioning
            tooltipElement.style.left = '50%';
            tooltipElement.style.right = 'auto';
            tooltipElement.style.top = '100%';
            tooltipElement.style.bottom = 'auto';
            tooltipElement.style.transform = 'translateX(-50%) translateY(8px)';

            // Adjust horizontal position if needed
            if (wrapperRect.left + tooltipRect.width / 2 > viewportWidth) {
                tooltipElement.style.left = 'auto';
                tooltipElement.style.right = '0';
                tooltipElement.style.transform = 'translateY(8px)';
            } else if (wrapperRect.left < tooltipRect.width / 2) {
                tooltipElement.style.left = '0';
                tooltipElement.style.transform = 'translateY(8px)';
            }

            // Adjust vertical position if needed
            if (wrapperRect.bottom + tooltipRect.height > viewportHeight) {
                tooltipElement.style.top = 'auto';
                tooltipElement.style.bottom = '100%';
                tooltipElement.style.transform = tooltipElement.style.transform.replace('translateY(8px)', 'translateY(-8px)');
                tooltipElement.classList.add('top');
            } else {
                tooltipElement.classList.remove('top');
            }
        }
    });
});