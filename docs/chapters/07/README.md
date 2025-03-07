# Chapter 07 - Generalization

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
                <div class="meta-value">
                    Markov Grey
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
				<i class="fas fa-clock"></i>
			</span>
			<div class="meta-content">
				<div class="meta-label">Reading Time</div>
				<div class="meta-value">35 min (core)</div>
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

<div class="action-buttons">
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </div>
    <a href="#" class="action-button">
        <i class="fas fa-headphones"></i>
        <span>Listen</span>
    </a>
    <div class="action-button disabled" data-tippy-content="PDF coming soon">
        <i class="fas fa-file-pdf"></i>
        <span>Download</span>
    </div>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1uQooTncb7Hw2NhITtr3S5iGHqT6cvj74c0SZ4Unad_M/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

<div class="atlas-audio-player">
    <!-- Header section -->
    <div class="audio-player__header">
        <div class="header-left">
            <i class="fas fa-headphones-alt"></i>
            <span class="audio-player__title">Audio Version</span>
            <span class="audio-warning-text"><i class="fas fa-robot"></i> AI-generated</span>
        </div>
        <div class="header-right">
            <button class="audio-close-button" aria-label="Close audio player">
                <i class="fas fa-times"></i>
            </button>
        </div>
    </div>
    
    <!-- MEGA embed wrapper -->
    <div class="mega-audio-wrapper">
        <iframe 
            width="100%" 
            height="160" 
            frameborder="0" 
            src="https://mega.nz/embed/2XR13D5L#1ekM2LQT0Je043erjy_fV4mBoxtyP9tNR8pdhlbVWKs!1v1c" 
            allowfullscreen
            loading="lazy"
            allow="autoplay">
        </iframe>
    </div>
    
    <!-- Error toggle button at the bottom -->
    <div class="errors-toggle-container">
        <button class="errors-toggle-button" aria-label="View known errors">
            <i class="fas fa-exclamation-circle"></i> View known errors in AI-generated audio
        </button>
    </div>
    
    <!-- Hidden errors panel at the bottom -->
    <div class="audio-errors-panel">
        <h4>Known Errors in AI-Generated Audio</h4>
        <ul>
            <li><strong>Note:</strong> - This is an AI-generated audio version. Please report any errors you find.</li>
        </ul>
        <p class="report-errors">Found errors? Please report to <a href="mailto:contact@securite-ia.fr">contact@securite-ia.fr</a></p>
    </div>
</div>

# Introduction

**Goal Misgeneralization** : This section introduces the concept of goals as distinct from rewards. It explains what it might be if a model's capabilities generalize, while the goals do not. The section provides various examples of game playing agents, LLMs and other thought experiments to show how this could be a potentially catastrophic failure mode distinct from reward misspecification.

**Inner Alignment** : The next section begins with an explanation of the machine learning process, and how it can be seen as analogous to search. Since the machine learning process can be seen analogous to search, one type of algorithm that can be “found" is an optimizer. This motivates a discussion of the distinction between base and mesa-optimizers.

**Deceptive Alignment** : Having understood mesa-optimizers, the next section introduces the different types of mesa-optimizers that can arise as well as the corresponding failure modes. This section also explores training dynamics that could potentially increase or decrease the likelihood of the emergence of deceptive alignment.
