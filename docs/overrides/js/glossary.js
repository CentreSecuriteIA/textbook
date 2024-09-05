document.addEventListener('DOMContentLoaded', function() {
    const tooltips = document.querySelectorAll('abbr[title]');
    
    tooltips.forEach(tooltip => {
        const tooltipText = tooltip.getAttribute('title');
        tooltip.removeAttribute('title');
        
        const wrapper = document.createElement('span');
        wrapper.className = 'glossary-term';
        tooltip.parentNode.insertBefore(wrapper, tooltip);
        wrapper.appendChild(tooltip);
        
        const tooltipElement = document.createElement('span');
        tooltipElement.className = 'md-tooltip';
        tooltipElement.textContent = tooltipText;
        wrapper.appendChild(tooltipElement);
        
        function showTooltip(e) {
            e.preventDefault();
            e.stopPropagation();
            adjustTooltipPosition();
            tooltipElement.style.visibility = 'visible';
            tooltipElement.style.opacity = '1';
        }

        function hideTooltip(e) {
            if (!tooltipElement.classList.contains('stick')) {
                tooltipElement.style.visibility = 'hidden';
                tooltipElement.style.opacity = '0';
            }
        }

        wrapper.addEventListener('mouseenter', showTooltip);
        wrapper.addEventListener('mouseleave', hideTooltip);
        
        wrapper.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            tooltipElement.classList.toggle('stick');
            adjustTooltipPosition();
        });

        document.addEventListener('click', function(e) {
            if (!wrapper.contains(e.target)) {
                tooltipElement.classList.remove('stick');
                hideTooltip(e);
            }
        });

        window.addEventListener('resize', adjustTooltipPosition);
        
        function adjustTooltipPosition() {
            const wrapperRect = wrapper.getBoundingClientRect();
            const tooltipRect = tooltipElement.getBoundingClientRect();
            const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
            const viewportHeight = window.innerHeight || document.documentElement.clientHeight;

            tooltipElement.classList.remove('right', 'left', 'bottom');

            if (viewportWidth <= 768) {
                // Mobile view: center the tooltip
                tooltipElement.style.left = '50%';
                tooltipElement.style.top = '50%';
                tooltipElement.style.transform = 'translate(-50%, -50%)';
            } else {
                // Desktop view: position relative to the term
                tooltipElement.style.left = '50%';
                tooltipElement.style.top = '';
                tooltipElement.style.transform = 'translateX(-50%)';

                if (wrapperRect.left + (tooltipRect.width / 2) > viewportWidth) {
                    tooltipElement.classList.add('right');
                } else if (wrapperRect.left - (tooltipRect.width / 2) < 0) {
                    tooltipElement.classList.add('left');
                }

                if (wrapperRect.top - tooltipRect.height - 10 < 0) {
                    tooltipElement.classList.add('bottom');
                }
            }

            // Adjust tooltip width
            const maxWidth = Math.min(300, viewportWidth - 40);
            tooltipElement.style.width = (tooltipRect.width > maxWidth) ? maxWidth + 'px' : 'max-content';
        }

        // Prevent default title tooltip from showing
        tooltip.addEventListener('mouseenter', function(e) {
            e.preventDefault();
            e.stopPropagation();
            tooltip.blur();
        });
    });
});
