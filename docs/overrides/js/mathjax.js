// File: docs/overrides/js/mathjax.js

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  startup: {
    ready: () => {
      console.log('MathJax is loaded, but not yet initialized');
      MathJax.startup.defaultReady();
      console.log('MathJax is initialized');
    }
  }
};

// Ensure MathJax is loaded and typeset when the page content changes
document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM fully loaded and parsed');
  if (typeof MathJax !== 'undefined') {
    MathJax.typeset();
  }
});

// If using instant loading feature of MkDocs
document.addEventListener('DOMContentSwitch', function() {
  console.log('DOM content switched');
  if (typeof MathJax !== 'undefined') {
    MathJax.typeset();
  }
});
