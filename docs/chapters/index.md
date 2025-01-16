# AI Safety Atlas


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
                    <div>
                    <div>Markov Grey</div>
                    <div>Charbel-Raphael Segerie</div>
                    <div>Jeanne Salle</div>
                    <div>Charles Martinet</div>
                    </div>
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
                    <div>Vincent Corruble</div>
                    <div>Jonathan Claybrough</div>
                    <div>Jérémy Andréoletti</div>
                    <div>Evander Hammer</div>
                </div>
            </div>
        </div>
    </div>
    <!-- Right Column -->
    <div class="meta-col">

        <!-- Citation -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-quote-right"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Cite this work as</div>
                <div class="meta-value">
                    <div>Grey, M., Segerie, C.R., et al. (2024). AI Safety Atlas. French Center for AI Safety (CeSIA). URL: ai-safety-atlas.com</div>
                </div>
            </div>
        </div>

        <!-- Project funded by -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-hand-holding-dollar"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Project funded by</div>
                <div class="meta-value">
                    <div><a href="https://manifund.org/projects/ai-safety-textbook" target="_blank" style="text-decoration: none; color: inherit;">Ryan Kidd (Manifund Regrant)</a></div>
                    <div>Open Philanthropy</div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

## Fundamentals

The first four chapters form the foundation of AI Safety understanding that every stakeholder needs, regardless of their technical background. These chapters are written to be accessible to wide audiences, while still maintaining technical accuracy and depth where needed. The target audience includes anyone seeking to understand why AI Safety matters and how we might address it. While no specific technical prerequisites are required, basic familiarity with AI concepts and current developments in the field will help readers get the most out of these chapters.

The progression through these is: beginning with understanding AI capabilities (what the AI can do), move to potential risks (what could go wrong), explore proposed solution strategies (how we might prevent those problems), examine governance frameworks (how to implement the strategies systematically). This sequence ensures readers build a comprehensive understanding of both the challenges and potential approaches to addressing them. The follow up technical chapters go into detail on specific strategies to problems in AI safety.

### Capabilities

AI models are transforming from narrow, specialized tools into increasingly general-purpose systems that can handle complex tasks. Empirical trends show that scaling up - using more data, compute, and parameters - is leading to steady gains in both performance and generality. Rather than viewing AI progress through simple thresholds like "narrow" versus "general" intelligence, we introduce frameworks for measuring capabilities along continuous dimensions. The chapter covers things like definitions of capabilities, scaling patterns, performance trends, and forecasting methods. Understanding these concepts shapes how we think about potential risks, safety measures, and governance approaches throughout the rest of the book.

<div class="action-buttons">
    <a href="https://www.youtube.com/watch?v=J_iMeH1hb9M" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Audio coming soon">
        <i class="fas fa-headphones"></i>
        <span>Listen</span>
    </div>
    <div class="action-button disabled" data-tippy-content="PDF coming soon">
        <i class="fas fa-file-pdf"></i>
        <span>Download</span>
    </div>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1L32xCVUCWEsm-x8UZ3GSTgKnmBcC7rJQLLIh9wGLj40/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

### Risks

The previous chapter establishes that we see increasing trends of capability, generality and autonomy in AI. Building on this we look at how risks emerge when these capabilities are combined with human incentives, and complex social systems. We divide risks into three main categories: misuse (humans using AI for harm, like cyber attacks or bioweapons), misalignment (AI systems failing in unintended ways), and systemic risks (problems that emerge when AI interacts with other comlex systems). We also talk about other factors that amplify these risks like competitive pressures creating race dynamics. Finally, we also give brief overviews of specific capabilities that amplify risks - like deception, situational awareness, autonomous replication and power-seeking behavior.


### Strategies

Building on our understanding of AI capabilities and risks, we explore concrete approaches to making AI development safer. We divide potential solutions into the same three categories as risks: preventing misuse (through monitored APIs and defensive technologies), addressing alignment (via technical research and control measures), and managing systemic impacts (through governance and safety culture). The field of AI safety is still emerging and no single solution might be sufficient - rather, we need a layered "Swiss cheese" approach where multiple safeguards work together to create robust protection against risks. The technical approaches discussed here set up readers for the deep-dives that follow in later chapters, while our examination of systemic and social solutions leads into the next few chapters on governance and evaluation frameworks, which explore how to implement these strategies through policy and coordination.

### Governance 

This chapter examines how we can implement and enforce the solutions discussed in Chapter 3 through effective oversight and regulation across multiple layers—from corporate policies to national legislation to international cooperation. By exploring key governance challenges and essential tools like compute monitoring, model registries, and incident reporting frameworks, this chapter completes our foundational understanding of AI safety by showing how technical solutions and policy mechanisms must work together to ensure beneficial AI development.

## Technical

The technical extension to the textbook, comprising chapters 5 through 9. It delves into the specific mechanisms and challenges of implementing AI Safety. These chapters assume familiarity with machine learning fundamentals, especially transformers in Natural Language Processing (NLP) and Reinforcement Learning (RL). The target audience roughly includes ML engineers, researchers, and technical practitioners who need to understand how to actually build safer AI systems.

Each technical chapter is structured to first thoroughly examine a specific problem (like reward misspecification or goal misgeneralization), explain why it presents a fundamental challenge to AI Safety, and then explore current approaches to addressing it along with their limitations. Together, these chapters provide the technical depth needed to engage with and contribute to current AI Safety research and development.

### Evaluations

This chapter serves as a bridge between the governance frameworks and technical implementation by exploring how we can rigorously assess AI systems' safety and capabilities. The chapter introduces key evaluation techniques from simple benchmarking to comprehensive protocols for testing dangerous capabilities, propensities, and control mechanisms, establishing how we can verify whether our safety measures are actually working and providing the measurement tools needed to implement many of the governance frameworks discussed in Chapter 4.

### Specification

This chapter tackles one of the fundamental challenges in AI alignment: ensuring that AI systems optimize for what we truly want rather than following reward functions literally or exploiting loopholes. This chapter examines why simply specifying the right reward is extremely difficult, how reward-based learning can lead to unintended behaviors through mechanisms like reward hacking and reward tampering, and explores potential solutions including learning from demonstrations, feedback, and constitutional AI approaches.

### Generalization

This chapter builds on the reward specification problem to explore a deeper issue: even when AI systems appear to learn the right behavior during training, they may learn and pursue the wrong goals when deployed in new situations. Through detailed examination of real-world examples and theoretical frameworks, this chapter explores how misaligned goals can emerge even from well-specified rewards, introducing concepts like mesa-optimization and deceptive alignment that are crucial for understanding advanced AI safety risks.

### Oversight

This chapter addresses a critical challenge that emerges as AI systems become more capable: how can we maintain meaningful human oversight when AI systems begin to exceed human capabilities in various domains? The chapter examines various approaches to this problem, from debate and amplification to recursive reward modeling, showing how we might maintain control and alignment even as AI capabilities scale beyond human-level in many areas.

### Interpretability

This chapter explores how we can understand the internal workings of AI systems, which is crucial for verifying their safety and alignment. Moving from simple visualization techniques to sophisticated methods for analyzing neural networks, this chapter examines both current tools and fundamental challenges in making AI systems more transparent and interpretable, which is essential for implementing many of the safety approaches discussed in previous chapters.

