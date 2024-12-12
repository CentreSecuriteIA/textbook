# Interpretability

<div class="chapter-meta">

<div class="meta-grid">
    <!-- Left Column -->
    <div class="meta-col">
        <!-- Authors -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-users"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Authors</div>
                <div class="meta-value meta-list">
                    <div><div>Jeanne Salle & Charbel-Raphael Segerie</div></div>
                </div>
            </div>
        </div>
        
        <!-- Affiliations -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-building"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Affiliations</div>
                <div class="meta-value meta-list">
                    <div><div>French Center for AI Safety (CeSIA)</div></div>
                </div>
            </div>
        </div>

<!-- Acknowledgements section -->
<div class="meta-item">
    <span class="meta-icon">
        <i class="fas fa-heart"></i>
    </span>
    <div class="meta-content">
        <div class="meta-label">Acknowledgements</div>
        <div class="meta-value">
            Markov Grey
        </div>
    </div>
</div>
    </div>

    <!-- Right Column -->
    <div class="meta-col">
        <!-- Date -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-calendar"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Last Updated</div>
                <div class="meta-value">2024-11-01</div>
            </div>
        </div>
        
        <!-- Reading Time -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-book-open"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Reading Time</div>
                <div class="meta-value">55 minutes</div>
            </div>
        </div>
        
        <!-- Links -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-link"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Also available on</div>
                <div class="meta-value meta-links">
                    <a href="https://docs.google.com/document/d/1mdYnniBG5vg4HjMMqqojEs8siFXoRnxi0RfxursBw7A/edit?usp=sharing" class="meta-link">Google Docs</a>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

[Feedback](https://forms.gle/ZsA4hEWUx1ZrtQLL9){ .md-button }
[Facilitate](https://docs.google.com/document/d/1izDWZKR_xB2qj2a8LkbqcnqnjBIC-C7fn-74CIA-m9w/edit?usp=sharing){ .md-button }

# Overview

We currently don’t understand how AI models work. We know how to train and build them, meaning we can design them and teach them to perform tasks, such as recognizing objects in images or generating coherent text in response to prompts. However, this does not mean we can always explain their behavior after training. As for now, we can’t explain why a network made a specific decision or produced a particular output. **The goal of interpretability is to understand the inner workings of these networks and explain how they function**, which in turn could allow us to better trust and control AI models.

!!! warning "Before reading this chapter it is recommended to be familiar with the transformer and CNN architectures."

<iframe style="width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="https://www.youtube.com/embed/KuXjwB4LzSA"></iframe>

!!! warning "If you are unfamiliar with transformers, the videos on transformers in this playlist will help you get up to speed before reading this chapter."

<iframe style="width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="https://www.youtube.com/embed/aircAruvnKk"></iframe>

For each method presented in this chapter, we first provide a high-level overview, followed by a more in-depth and technical explanation. The technical explanations can be skipped.
