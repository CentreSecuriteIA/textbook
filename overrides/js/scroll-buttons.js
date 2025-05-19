//# File: textbook/docs/overrides/js/scroll-buttons.js

document.addEventListener('DOMContentLoaded', () => {
   // Add scroll to top button
   const scrollToTopButton = document.createElement('button');
   scrollToTopButton.className = 'md-scroll-button md-scroll-top';
   scrollToTopButton.title = 'Scroll to top';
   scrollToTopButton.innerHTML = '<svg viewBox="0 0 24 24"><path d="M12 6V18M12 6L7 11M12 6L17 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
   document.body.appendChild(scrollToTopButton);

   // Add scroll to bottom button
   const scrollToBottomButton = document.createElement('button');
   scrollToBottomButton.className = 'md-scroll-button md-scroll-bottom';
   scrollToBottomButton.title = 'Scroll to bottom';
   scrollToBottomButton.innerHTML = '<svg viewBox="0 0 24 24"><path d="M12 6V18M12 18L7 13M12 18L17 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
   document.body.appendChild(scrollToBottomButton);

   let hideTimeout;
   let isMouseOverButton = false;

   // Function to show buttons
   const showButtons = () => {
       scrollToTopButton.classList.remove('md-scroll-inactive');
       scrollToBottomButton.classList.remove('md-scroll-inactive');
       
       // Clear any existing timeout
       if (hideTimeout) {
           clearTimeout(hideTimeout);
       }
       
       // Set new timeout only if mouse isn't over buttons
       if (!isMouseOverButton) {
           hideTimeout = setTimeout(() => {
               scrollToTopButton.classList.add('md-scroll-inactive');
               scrollToBottomButton.classList.add('md-scroll-inactive');
           }, 2000); // Hide after 2 seconds of inactivity
       }
   };

   // Mouse/touch event handlers
   [scrollToTopButton, scrollToBottomButton].forEach(button => {
       button.addEventListener('mouseenter', () => {
           isMouseOverButton = true;
           showButtons();
       });
       
       button.addEventListener('mouseleave', () => {
           isMouseOverButton = false;
           showButtons();
       });
   });

   scrollToTopButton.addEventListener('click', () => {
       window.scrollTo({
           top: 0,
           behavior: 'smooth'
       });
   });

   scrollToBottomButton.addEventListener('click', () => {
       window.scrollTo({
           top: document.documentElement.scrollHeight,
           behavior: 'smooth'
       });
   });

   // Show/hide buttons based on scroll position
   let lastScrollTime = Date.now();
   window.addEventListener('scroll', () => {
       const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
       const scrollHeight = document.documentElement.scrollHeight;
       const clientHeight = document.documentElement.clientHeight;
       const scrollBottom = scrollHeight - clientHeight - scrollTop;

       lastScrollTime = Date.now();
       
       // Show top button when not at top
       if (scrollTop > 100) {
           scrollToTopButton.dataset.mdState = 'active';
       } else {
           scrollToTopButton.dataset.mdState = '';
       }
       
       // Show bottom button when not at bottom
       if (scrollBottom > 100) {
           scrollToBottomButton.dataset.mdState = 'active';
       } else {
           scrollToBottomButton.dataset.mdState = '';
       }

       showButtons();
   });

   // Initial check for scroll position
   window.dispatchEvent(new Event('scroll'));
});
