document.addEventListener('DOMContentLoaded', () => {
    // Update scroll progress bar
    window.addEventListener('scroll', () => {
        const docElement = document.documentElement;
        const scrollTotal = docElement.scrollHeight - docElement.clientHeight;
        const scrollProgress = `${(docElement.scrollTop / scrollTotal) * 100}%`;
        document.documentElement.style.setProperty('--scroll-progress', scrollProgress);
    });
});
