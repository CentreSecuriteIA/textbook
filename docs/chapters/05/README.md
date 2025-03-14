# Chapter 05 - Evaluations

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
                    Markov Grey & Charbel-Raphael Segerie
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
            Maxime Riché, Martin, Fabien Roger, Jeanne Salle, Camille Berger, Leo Karoubi
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
                <div class="meta-value">2025-01-15</div>
            </div>
        </div>
        
        <!-- Reading Time -->
		<div class="meta-item">
			<span class="meta-icon">
				<i class="fas fa-clock"></i>
			</span>
			<div class="meta-content">
				<div class="meta-label">Reading Time</div>
				<div class="meta-value">132 min (core)</div>
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
                    <a href="https://docs.google.com/document/d/1KI95w27Ce7yWoynE11PJ94IXK0gT0NwP8091s06P7wM/edit?usp=sharing" class="meta-link">Google Docs</a>
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
    <a href="https://docs.google.com/document/d/1T-UU0FBeElX6cvbWYKpVAl3U4ivrQLHA3IdIWqWKuBA/edit?tab=t.0#heading=h.fo57hwsn3del" class="action-button">
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
            src="https://mega.nz/embed/ieBRQZQZ#GzZAljhhfVUmUHSG0cWEBaW2AkuCm4LmpfYFGtWKBbM!1v1c" 
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
            <li><strong>3:00</strong> - Error - Feature visualizations (are not that helpful currently; behavioral approaches remain the best way to evaluate deception)</li>
            <li><strong>4:00</strong> - Imprecise - Multiple labs evaluate CBRN capabilities, not just OpenAI</li>
            <li><strong>12:30</strong> - Debated - TruthfulQA is not really a propensity evaluation</li>
            <li><strong>17:30</strong> - Error - Sandbagging emerges from the AI itself, it is not implemented by developers</li>
            <li><strong>18:40</strong> - Inaccurate - One of the most important limitations is not just that we lack evaluations in cybersecurity; rather, it's difficult to elicit the capabilities of a system, and we cannot be certain whether it will be impossible to create a system that performs</li>
        </ul>
        <p class="report-errors">Found more errors? Please report to <a href="mailto:contact@securite-ia.fr">contact@securite-ia.fr</a></p>
    </div>
</div>

# Introduction

As AI systems grow increasingly powerful, our ability to rigorously evaluate them becomes crucial for safety and governance. The challenge isn't just measuring what AI systems can do, but understanding their behavioral tendencies and verifying our ability to maintain control. This section introduces the landscape of AI evaluation and explains why we need increasingly sophisticated approaches beyond simple benchmarking.

<figure markdown="span">
![Enter image alt description](Images/OR7_Image_1.png){ loading=lazy }
  <figcaption markdown="1"><b>Figure 5.1:</b> Overview of chapter content.</figcaption>
</figure>

**Benchmarks.** Building on this need for measurement, we explore how standardized tests like MMLU or TruthfulQA have historically helped quantify AI capabilities. While these benchmarks provide valuable standardization, they face fundamental limitations - models can memorize answers without understanding, and benchmark performance may not translate to real-world safety. The "reversal curse" demonstrates how models might score well on tests while failing to learn basic logical relationships, highlighting why we need more comprehensive evaluation approaches.

**Evaluated Properties.** To develop better evaluations, we first need to understand exactly what properties of AI systems matter for safety. This section introduces three fundamental categories: capabilities (what a model can do), propensities (what it tends to do), and control (whether we can prevent unacceptable outcomes). This framework helps clarify why, for instance, a model being capable of writing malicious code is different from having a tendency to do so, and both are different from our ability to prevent it from doing so even if it tries.

**Evaluation Techniques.** With clear properties to measure, we explore specific techniques for gathering evidence about AI systems. We examine both behavioral techniques that study model outputs and internal techniques that analyze model mechanisms. This includes approaches like best-of-N sampling, multistep reasoning prompting, and red teaming, providing concrete tools for the evaluations explored in subsequent sections.

**Dangerous Capability Evaluations.** Focusing first on dangerous capabilities, we examine how to measure abilities like deception, situational awareness, and autonomous replication. These evaluations aim to establish upper bounds on what AI systems can achieve when explicitly trying, providing crucial information about potential risks. METR's evaluation of GPT-4 demonstrates how systematic protocols can probe concerning capabilities even in current systems.

**Dangerous Propensity Evaluations.** Building on capability assessment, we explore how to measure behavioral tendencies like power-seeking or deception. These become increasingly critical as models grow more capable - knowing what a model can do isn't enough, we need to understand what it's likely to do by default. This involves carefully designed choice frameworks and consistency measurements to reveal underlying behavioral patterns.

**Control Evaluations.** Taking evaluation to its logical conclusion, we examine whether we can maintain meaningful control even if an AI system actively tries to circumvent safety measures. This section explores how techniques like red team/blue team testing can help verify safety protocols remain effective under worst-case scenarios, while acknowledging the inherent challenges in simulating truly adversarial behavior.

**Evaluation Design.** Moving from theory to practice, we examine how to implement these evaluations effectively at scale. This includes designing robust evaluation protocols, automating assessment processes where possible, and integrating evaluations with broader safety frameworks and auditing systems. A key focus is developing systematic approaches that can be reliably implemented across different organizations.

**Limitations.** Finally, we talk about the fundamental challenges facing AI evaluations. From the difficulty of proving absence of capabilities, to technical constraints around measurement precision, to governance challenges around independence and standardization - understanding these limitations is crucial for both improving our methods and maintaining appropriate epistemic humility about their results.

