// File: textbook/docs/overrides/js/citations.js

document.addEventListener('DOMContentLoaded', () => {
    initializeCopyButtons();
});

function initializeCopyButtons() {
    const copyButtons = document.querySelectorAll('.copy-button');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            const formatContent = button.parentElement.textContent.trim();
            
            try {
                await navigator.clipboard.writeText(formatContent);
                
                // Visual feedback
                button.textContent = 'Copied!';
                button.classList.add('copied');
                
                // Reset after 2 seconds
                setTimeout(() => {
                    button.textContent = 'Copy';
                    button.classList.remove('copied');
                }, 2000);
                
            } catch (err) {
                console.error('Failed to copy text:', err);
                button.textContent = 'Failed to copy';
                
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000);
            }
        });
    });
}
