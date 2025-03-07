# Chapter 01 - Capabilities

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
            Jeanne Salle, Charles Martinet, Vincent Corruble, Diego Dorn, Josh Thorsteinson, Jonathan Claybrough, Alejandro Acelas, Jamie Raldua Veuthey, Alexandre Variengien, Léo Dana, Angélina Gentaz, Nicolas Guillard, Leo Karoubi
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
                <div class="meta-value">2024-11-20</div>
            </div>
        </div>
        
        <!-- Reading Time -->
		<div class="meta-item">
			<span class="meta-icon">
				<i class="fas fa-clock"></i>
			</span>
			<div class="meta-content">
				<div class="meta-label">Reading Time</div>
				<div class="meta-value">94 min (core), 51 min (appendix)</div>
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
                    <a href="https://www.alignmentforum.org/posts/MkfaQyxB9PN4h8Bs9/" class="meta-link">Alignment Forum</a> · <a href="https://docs.google.com/document/d/1HKo0Kest9Xppjn7m2ODpfMUlEu93SzLsfxXBH48Xaus/edit?usp=sharing" class="meta-link">Google Docs</a>
                </div>
            </div>
        </div>
    </div>
</div>



<div class="action-buttons">
   <a href="https://www.youtube.com/watch?v=J_iMeH1hb9M" class="action-button">
       <i class="fas fa-video"></i>
       <span>Watch</span>
   </a>
   <button class="action-button audio-toggle-button">
       <i class="fas fa-headphones"></i>
       <span>Listen</span>
   </button>
   <a href="https://raw.githubusercontent.com/CentreSecuriteIA/textbook/main/latex/AI%20Safety%20Atlas%20-%20Capabilities.pdf" class="action-button" download>
       <i class="fas fa-file-pdf"></i>
       <span>Download</span>
   </a>
   <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
       <i class="fas fa-comment"></i>
       <span>Feedback</span>
   </a>
   <a href="https://docs.google.com/document/d/1L32xCVUCWEsm-x8UZ3GSTgKnmBcC7rJQLLIh9wGLj40/edit?usp=sharing" class="action-button">
       <i class="fas fa-users"></i>
       <span>Facilitate</span>
   </a>
</div>

<div class="atlas-audio-player hidden-player">
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
            src="https://mega.nz/embed/TbR00YZa#pxHbeGX_Xx8S_s5wvYXzqR9vdR9oX_6LiXtVzf8FFV8!1v1c" 
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

<figure class="video-figure" markdown="span">
<iframe style="width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="https://www.youtube.com/embed/J_iMeH1hb9M"></iframe>
  <figcaption markdown="1"><b>Video 1.1:</b> Optional video to get an overview of AI capabilities.</figcaption>
</figure>

!!! quote "Yann LeCun Chief AI scientist at Meta and Turing Prize winner, May 2023 ([Heaven, 2023](https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/))"



    There is no question that machines will become smarter than humans—in all domains in which humans are smart—in the future. It's a question of when and how, not a question of if.



The field of artificial intelligence has undergone a remarkable transformation in recent years. This chapter lays the groundwork for the entire book by establishing what AI systems can currently do, how they achieve these capabilities, and how we might anticipate their future development. This understanding is essential for all subsequent chapters: the discussion of dangerous capabilities and potential risks (Chapter 2) follows directly from understanding capabilities. Similarly, proposed technical (Chapter 3) and governance solutions (Chapter 4) both must account for the current and projected future of AI capabilities.

<figure markdown="span">
![Enter image alt description](Images/XnK_Image_1.png){ loading=lazy }
  <figcaption markdown="1"><b>Figure 1.1:</b> We first explain foundation models, which have been continuously showing improved capabilities due to scale. Then examine empirically observed scaling laws. Based on these trends we look at some techniques that researchers use to try and forecast future AI progress.</figcaption>
</figure>

**State-of-the-Art AI - Achieved breakthrough capabilities across multiple domains** . We begin by exploring how AI systems have evolved from narrow, specialized tools to increasingly general-purpose tools. Language models can now engage in complex reasoning, while computer vision systems demonstrate sophisticated understanding of visual information. In robotics, we're seeing the emergence of systems that can learn and adapt to real-world environments with increasing autonomy. The goal of this section is to give the reader many examples from different domains of accelerating AI capabilities.

**Foundation models - Revolutionized how we build AI systems.** The next section explores how we have moved from smaller specialized architectures to large scale general-purpose architectures. Rather than building separate systems for each task, these foundation models serve as the starting point. They are building blocks that can be later adapted for various applications using fine-tuning. We explore how these models are trained, their key properties, and the unique challenges they present. The emergence of unexpected capabilities from these models raises important questions about both their potential and implications for AI safety.

**Understanding Intelligence - Capabilities require precise measurement to guide safety work** . The objective of this section is to provide an understanding of what terms like artificial general intelligence and artificial superintelligence actually mean in practice. Through detailed case studies and empirical observations, we examine different approaches to defining and measuring AI capabilities. Moving beyond traditional binary distinctions between "narrow" and "general" AI, we introduce more nuanced formal frameworks that track progress along multiple dimensions, essential for understanding when and how safety measures need to be implemented.

**Scaling - The bitter lesson and empirical scaling laws show that scale drives progress** . We explore how simple algorithms plus massive computation often outperform sophisticated hand-crafted approaches. This leads us to examine scaling laws that describe how AI performance improves with different variables like - data, parameter count and increased computational resources. This section also contains an examination of the debate around whether scale alone is sufficient for achieving transformative AI capabilities.

**Forecasting - Predicting capabilities progress helps us prepare safety measures in advance** . Building on our understanding of current capabilities and scaling behaviors, we examine various approaches to anticipating future progress. From biological anchors to trend analysis, we explore frameworks for making informed predictions about AI development trajectories. This is very important to know when different safety measures need to be in place.

**Appendices - Overview of expert opinions on AI, detailed debates around scale, and scaling trends.** We consider these sections optional, but still useful to those who want to get a little bit of a deeper dive. The chapter concludes with appendices examining expert opinions on AI progress, deeper discussions about the nature and limitations of large language models, and comprehensive data on key trends in AI development.

