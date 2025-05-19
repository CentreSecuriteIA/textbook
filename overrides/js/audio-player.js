/* File: docs/overrides/js/audio-player.js */
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all audio players
    initializeAudioPlayers();
    
    // Set up audio toggle buttons
    setupAudioToggleButtons();
    
    function initializeAudioPlayers() {
        const audioPlayers = document.querySelectorAll('.atlas-audio-player');
        
        audioPlayers.forEach(player => {
            if (!player.hasAttribute('data-initialized')) {
                initializePlayer(player);
                player.setAttribute('data-initialized', 'true');
            }
        });
    }
    
    function initializePlayer(player) {
        // For the MEGA player, we only need to handle the errors panel
        const errorsToggleButton = player.querySelector('.errors-toggle-button');
        const errorsPanel = player.querySelector('.audio-errors-panel');
        
        // Errors panel toggle
        if (errorsToggleButton && errorsPanel) {
            errorsToggleButton.addEventListener('click', function() {
                errorsPanel.classList.toggle('active');
                
                // Change button text based on state
                if (errorsPanel.classList.contains('active')) {
                    errorsToggleButton.innerHTML = '<i class="fas fa-times-circle"></i> Hide known errors';
                } else {
                    errorsToggleButton.innerHTML = '<i class="fas fa-exclamation-circle"></i> View known errors in AI-generated audio';
                }
            });
        }
        
        // Add close button functionality if present
        const closeButton = player.querySelector('.audio-close-button');
        if (closeButton) {
            closeButton.addEventListener('click', function() {
                player.classList.add('hidden-player');
            });
        }
    }
    
	function setupAudioToggleButtons() {
    const toggleButtons = document.querySelectorAll('.action-button:has(.fa-headphones)');
    
    toggleButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            // Find the associated audio player (next sibling or search for it)
            const audioPlayer = findAssociatedAudioPlayer(button);
            if (audioPlayer) {
                audioPlayer.classList.remove('hidden-player');
                // Scroll to the audio player
                audioPlayer.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });
}
    
    function findAssociatedAudioPlayer(button) {
        // First try to find the player as a sibling to the action-buttons container
        const actionButtons = button.closest('.action-buttons');
        if (actionButtons) {
            let sibling = actionButtons.nextElementSibling;
            while (sibling) {
                if (sibling.classList.contains('atlas-audio-player')) {
                    return sibling;
                }
                sibling = sibling.nextElementSibling;
            }
        }
        
        // If not found, look for the first audio player on the page
        return document.querySelector('.atlas-audio-player');
    }
    
    // Support for dynamic content with MkDocs
    if (typeof document$ !== 'undefined') {
        document$.subscribe(() => {
            setTimeout(() => {
                initializeAudioPlayers();
                setupAudioToggleButtons();
            }, 300);
        });
    }
});
