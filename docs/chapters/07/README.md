# Generalization

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
                    <div><div>Markov Grey</div></div>
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
            RA Writer, Charbel-Raphael Segerie, Jeanne Salle, Oscar Heitmann, Camille Berger, Josh Thorsteinson, Nicolas Guillard
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
                <div class="meta-value">2023-12-13</div>
            </div>
        </div>
        
        <!-- Reading Time -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-book-open"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Reading Time</div>
                <div class="meta-value">36 minutes</div>
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
                    <a href="https://docs.google.com/document/d/10aqDKJgqonHNc9IMMogtda64u8V_JsPlbuzruBMUmAU/edit?usp=sharing" class="meta-link">Google Docs</a>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

[Feedback](https://forms.gle/ZsA4hEWUx1ZrtQLL9){ .md-button }
[Facilitate](https://docs.google.com/document/d/1uQooTncb7Hw2NhITtr3S5iGHqT6cvj74c0SZ4Unad_M/edit?usp=sharing){ .md-button }

# Introduction

**Goal Misgeneralization**: This section introduces the concept of goals as distinct from rewards. It explains what it might be if a model's capabilities generalize, while the goals do not. The section provides various examples of game playing agents, LLMs and other thought experiments to show how this could be a potentially catastrophic failure mode distinct from reward misspecification.

**Inner Alignment**: The next section begins with an explanation of the machine learning process, and how it can be seen as analogous to search. Since the machine learning process can be seen analogous to search, one type of algorithm that can be “found" is an optimizer. This motivates a discussion of the distinction between base and mesa-optimizers.

**Deceptive Alignment**: Having understood mesa-optimizers, the next section introduces the different types of mesa-optimizers that can arise as well as the corresponding failure modes. This section also explores training dynamics that could potentially increase or decrease the likelihood of the emergence of deceptive alignment.