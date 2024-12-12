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
                    <div><a href="https://manifund.org/projects/ai-safety-textbook" target="_blank" style="text-decoration: none; color: inherit;">Ryan Kidd (Manifund)</a></div>
                    <div>Open Philanthropy</div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

## Fundamentals

The first four chapters form the foundational understanding of AI Safety that every stakeholder needs, regardless of their technical background. These chapters are written to be accessible to wide audiences, while still maintaining technical accuracy and depth where needed. The target audience includes anyone seeking to understand why AI Safety matters and how we might address it. While no specific technical prerequisites are required, basic familiarity with AI concepts and current developments in the field will help readers get the most out of these chapters.

The progression through these chapters is carefully structured: we begin with understanding AI capabilities (what the technology can do), move to potential risks (what could go wrong), explore proposed solutions (how we might prevent those problems), examine governance frameworks (how to implement those solutions systematically). This sequence ensures readers build a comprehensive understanding of both the challenges and potential approaches to addressing them.

### Capabilities

This chapter lays essential groundwork by examining the current state and trajectory of AI technology, introducing key concepts like foundation models, scaling laws, and methods for measuring and forecasting AI progress. This foundational understanding of what AI systems can do today—and may be capable of tomorrow—is crucial for grasping the risks and challenges discussed in subsequent chapters, as we can't meaningfully address AI safety without first understanding the technology we're trying to make safe.

### Risks

This chapter builds directly on our understanding of AI capabilities to explore three fundamental categories of risk: misuse risks where humans intentionally deploy AI for harm, misalignment risks where AI systems pursue goals that conflict with human values, and systemic risks that emerge from complex interactions between AI systems and global structures. By systematically breaking down these risks and examining how they can manifest at different scales, from localized disruptions to existential threats, this chapter establishes why AI safety work is crucial and what specific challenges need to be addressed.

### Solutions

This chapter responds to the risks identified in Chapter 2 by examining current approaches and proposals for ensuring safe AI development, covering strategies from technical solutions to alignment to organizational safety practices and governance frameworks. While acknowledging that the field of AI safety is still young and no single solution appears sufficient, this chapter provides a comprehensive overview of available tools and strategies, setting up readers to understand the more technical deep-dives into specific safety mechanisms that follow in later chapters.

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

