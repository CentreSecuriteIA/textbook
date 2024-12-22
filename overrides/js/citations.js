// File: docs/js/citations.js

class Citations {
  constructor(element, metadata) {
    this.container = element;
    this.metadata = metadata;
    this.currentFormat = 'bibtex';
    
    this.formats = {
      bibtex: { id: 'bibtex', name: 'BibTeX' },
      apa: { id: 'apa', name: 'APA' },
      chicago: { id: 'chicago', name: 'Chicago' },
      mla: { id: 'mla', name: 'MLA' }
    };
    
    this.render();
    this.attachEventListeners();
  }
  
  generateCitation(format) {
    const { authors, title, date, url } = this.metadata;
    const authorStr = authors.join(", ");
    const year = new Date(date).getFullYear();
    
    switch (format) {
      case 'bibtex':
        const key = title.toLowerCase().replace(/[^a-z0-9]/g, '-');
        return `@misc{${key},
    author = {${authors.join(" and ")}},
    title = {${title}},
    year = {${year}},
    publisher = {AI Safety Atlas},
    url = {${url}}
}`;
      case 'apa':
        return `${authorStr}. (${year}). ${title}. AI Safety Atlas. ${url}`;
      case 'chicago':
        return `${authorStr}. "${title}." AI Safety Atlas, ${year}. ${url}.`;
      case 'mla':
        return `${authorStr}. "${title}." AI Safety Atlas, ${year}, ${url}.`;
    }
  }
  
  render() {
    this.container.innerHTML = `
      <div class="citations-wrapper">
        <div class="citations-header">
          <i class="fas fa-quote-left"></i>
          <span class="section-title">How to cite</span>
        </div>
        
        <div class="citations-tabs">
          ${Object.values(this.formats).map(format => `
            <button class="tab-button ${format.id === this.currentFormat ? 'active' : ''}" 
                    data-format="${format.id}">
              ${format.name}
            </button>
          `).join('')}
        </div>
        
        <div class="citation-content">
          <button class="copy-button" aria-label="Copy citation">
            <i class="fas fa-copy"></i>
          </button>
          <pre class="citation-text">${this.generateCitation(this.currentFormat)}</pre>
        </div>
      </div>
    `;
  }
  
  attachEventListeners() {
    // Tab switching
    this.container.querySelectorAll('.tab-button').forEach(button => {
      button.addEventListener('click', () => {
        this.currentFormat = button.dataset.format;
        
        // Update active tab
        this.container.querySelectorAll('.tab-button').forEach(btn => 
          btn.classList.toggle('active', btn.dataset.format === this.currentFormat));
        
        // Update citation text
        this.container.querySelector('.citation-text').textContent = 
          this.generateCitation(this.currentFormat);
      });
    });
    
    // Copy button
    const copyButton = this.container.querySelector('.copy-button');
    copyButton.addEventListener('click', async () => {
      try {
        const citation = this.generateCitation(this.currentFormat);
        await navigator.clipboard.writeText(citation);
        
        // Visual feedback
        copyButton.classList.add('copied');
        const icon = copyButton.querySelector('i');
        
        icon.classList.remove('fa-copy');
        icon.classList.add('fa-check');
        
        setTimeout(() => {
          copyButton.classList.remove('copied');
          icon.classList.remove('fa-check');
          icon.classList.add('fa-copy');
        }, 2000);
      } catch (err) {
        console.error('Failed to copy:', err);
      }
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.citations-container').forEach(container => {
    const metadata = JSON.parse(container.dataset.metadata);
    new Citations(container, metadata);
  });
});


// Initialize citations
function initializeCitations() {
  document.querySelectorAll('.citations-container').forEach(container => {
    const metadata = JSON.parse(container.dataset.metadata);
    new Citations(container, metadata);
  });
}

// Initial load
document.addEventListener('DOMContentLoaded', initializeCitations);

// Handle MkDocs page changes
document$.subscribe(initializeCitations);
