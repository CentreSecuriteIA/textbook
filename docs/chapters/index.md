# AI Safety Atlas

<div class="chapter-meta">
<div class="meta-grid">
    <!-- Left Column -->
    <div class="meta-col">
        <!-- Authors -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-pen-nib"></i>
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
                <i class="fas fa-university"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Affiliations</div>
                <div class="meta-value meta-list">
                    <div><div>French Center for AI Safety (CeSIA)</div></div>
                </div>
            </div>
        </div>

        <!-- Advisors section -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-graduation-cap"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Advisors</div>
                <div class="meta-value">
                    <div>Vincent Corruble</div>
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
                    <div>Markov Grey and Charbel-Raphael Segerie et al. 2024. AI Safety Atlas. French Center for AI Safety (CeSIA). ai-safety-atlas.com</div>
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

        <!-- Acknowledgements section -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-heart"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Acknowledgements</div>
                <div class="meta-value">
                    <div>Jonathan Claybrough</div>
                    <div>Jérémy Andréoletti</div>
                    <div>Evander Hammer</div>
                    <div>Josh Thorsteinson</div>
                </div>
            </div>
        </div>
    </div>
</div>
</div>

<div style="content: ''; display: block; width: 100%; height: 3px; background-color: currentColor; opacity: 0.7; margin: 1.5em 0;"></div>

AI is undergoing unprecedented growth in capabilities, from writing code and analyzing scientific papers to generating images and engaging in complex reasoning. As these systems rapidly approach and potentially surpass human-level performance in many domains, the decisions we make today about their development will shape humanity's future. This book provides a comprehensive framework for understanding and addressing AI Safety challenges - from fundamental concepts to technical implementation. Whether you're a policymaker, researcher, engineer, or concerned citizen, our aim is to equip you with the knowledge needed to contribute meaningfully to ensuring AI development benefits humanity.

!!! quote "Geoffrey Hinton (Most cited computer scientist ever, Godfather of modern AI, Turing Award Recipient) ([Hinton, 2024](https://www.cbsnews.com/news/geoffrey-hinton-ai-dangers-60-minutes-transcript/))"

    I can't see a path that guarantees safety. We're entering a period of great uncertainty where we're dealing with things we've never dealt with before. And normally, the first time you deal with something totally novel, you get it wrong. And we can't afford to get it wrong with these things.
    [...]
    If you take the existential risk seriously, as I now do, it might be quite sensible to just stop developing these things any further [...] it's as if aliens had landed and people haven't realized because they speak very good English



## [Capabilities](https://ai-safety-atlas.com/chapters/01/)

*Why might AIs keep growing both increasingly general and capable?*

AI models are moving from specialized tools into increasingly general-purpose systems that can handle complex tasks. In this chapter we talk about empirical trends which show that scaling up - using more data, compute, and parameters - is leading to steady gains in both capabilities and generality. We explain the definitions of things like artificial general intelligence (AGI) and superintelligence (ASI) that we will be using throughout the book. Rather than viewing AI progress through discrete thresholds like "narrow" versus "general" intelligence, we introduce frameworks for measuring capabilities, generality and autonomy along continuous curves. Based on this we look at arguments for different AI takeoff scenarios, and provide expert opinions on timelines to transformative AI. Understanding these concepts shapes the conversations around potential sources of risks and safety strategies throughout the rest of the book. After reading this chapter, you'll be able to critically evaluate many of the claims about AI progress and engage in informed discussions about future AI developments.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/01/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <a href="https://www.youtube.com/watch?v=J_iMeH1hb9M" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
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

## [Risks](https://ai-safety-atlas.com/chapters/02/)

*What can go wrong if AI keeps becoming more capable?*

Once we have established the core arguments behind why capabilities, generality and autonomy might keep increasing, we can look at what risks correspond to these increased levels. We divide risks from AI into three main categories: misuse (humans using AI for harm, like cyber attacks or bioweapons), misalignment (AI systems failing in unintended ways), and systemic risks (problems that emerge when AI interacts with other complex systems). We also talk about underlying factors that amplify all of these risks like competitive pressures creating race dynamics and widespread deployment. Finally, we also give brief explanations of how to concretely think about dangerous capabilities like - deception, situational awareness, autonomous replication, scheming and power-seeking behavior. By the end of this chapter, you will be able to identify how different risks emerge from technical failures of AI systems, or the combination of AI capabilities with human incentives, and other complex socio-technical systems.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/02/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <a href="https://www.youtube.com/watch?v=dhr4u-w75aQ" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </a>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1evE1rG91DKBuKlWnqPw45QtPxKBz0GlD_ZYrurNdvN4/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

## [Strategies](https://ai-safety-atlas.com/chapters/03/)

*What strategies can we develop to mitigate risks?*

Building upon the understanding of capabilities and risks, in this chapter we look at concrete strategies for mitigating these risks and making AI development safer. We divide potential mitigation strategies into the same three categories as risks: preventing misuse (e.g. through monitored APIs and defensive technologies), addressing alignment (e.g. via technical research and control measures), and managing systemic impacts (e.g. through governance and safety culture). We explain how AI Safety is just starting to gain momentum as a field, but it is important to remember that no single solution might be sufficient. We might need a layered approach where multiple safeguards all work together to create robust protection against the risks outlined in the previous chapter. The purpose of this chapter is to give an overview of many different safety strategies and proposals and to show how these individual pieces might fit into the bigger picture. By reading this chapter and the ones before it, you have a solid foundation for the individual deep-dives that follow in all chapters after this. The systemic and social strategies outlined lead directly into the next few chapters on governance and evaluations, and the technical problems and mitigation strategies are discussed in dedicated individual chapters as well.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/03/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <a href="https://www.youtube.com/watch?v=iO7Jl4xders" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </a>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1cv0gzwSouDjckYHzV7gYbHPKhJZR6bwbJWgHzEJ604Q/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

## [Governance](https://ai-safety-atlas.com/chapters/04/)

*How can we guide safe AI development and deployment?*

Previous chapters provided overviews of what AI can do, what could go wrong, and potential mitigation strategies, in this chapter we take a deeper look at how to shape the impact of AI through governance frameworks. We start by explaining why AI regulation faces unique challenges due things like unexpected capability jumps, post deployment safety issues, and rapid proliferation. We explain key governance targets like - compute governance (controlling key inputs like chips and training resources), data governance (managing training data and deployment). Following this we look at individual layers that can introduce changes to affect the chosen targets - corporate governance (internal safety frameworks like Anthropic's RSPs), national governance (governmental initiatives like AI Safety Institutes and regulations like the EU AI Act), and international governance (approaches ranging from non-proliferation to regulatory agreements). Reiterating what we said in the strategies chapter, no single governance layer might be completely sufficient - rather, we need coordinated action across all levels to address AI risks effectively. Reading this chapter will help you participate meaningfully in discussions on AI development, deployment, auditing and policy.


<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/04/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <a href="https://www.youtube.com/watch?v=FSKuDqze9es" class="action-button">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </a>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1tp5rpzw_gekjju-UBp8tkbbnQOuA2QzsPF_um8Z4IOU/edit?tab=t.0#heading=h.fo57hwsn3del" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

## [Evaluations](https://ai-safety-atlas.com/chapters/05/)

*How do we measure if an AI system is actually safe?*

Evaluations is the first chapter in what we consider to be the technical sequence, because it helps us bridge theory and practice by showing how evaluation results can trigger specific governance actions or technical safety protocols. Our explanation is decomposed into the questions of - what are we evaluating? (evaluated properties), how are we evaluating it? (evaluation techniques), and what elements play into good evaluations? (evaluation design). We cover AI Safety specific evaluation methods in three different categories - dangerous capability evaluations (what AI systems can do), propensity evaluations (how they tend to behave by default), and control evaluations (our ability to maintain safety under adversarial conditions). We explain how we might create techniques for evaluating dangerous capabilities (deception, CBRN risks, and autonomous replication) and dangerous propensities (e.g. power-seeking and scheming) which we previously outlined in the risks chapter. After reading this chapter, you will be able to understand what designing AI Safety evaluations entails, and how their results can inform both technical research directions and governance decisions.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/05/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
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

## [Specification](https://ai-safety-atlas.com/chapters/06/)

*Why is telling AI systems what we want so hard?*

Evaluations help us figure out what AI systems can do or tend to do, and if our current mitigation measures are enough. The next step is to try and answer - how do we correctly specify what we even want AI to do in the first place? We introduced the general concept of specification gaming in the risks chapter, here we build upon that and look at theoretical foundations and practical failure modes like reward hacking (finding unintended ways to maximize reward) and reward tampering (directly manipulating reward mechanisms). We also explain how suggested mitigation strategies to the specification problem might work. This includes things like imitation-based methods (e.g. behavioral cloning, inverse reinforcement learning) and feedback-based approaches (e.g. reward modeling, reinforcement learning from human feedback (RLHF), Constitutional AI). We also cover the limitations of these approaches which helps set up the context for the next few chapters on generalization and scalable oversight. After reading this chapter, you will be able to understand why trying to encode even simple instructions can lead to unexpected behaviors and how AI safety research is currently trying to address these challenges.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/06/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </div>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1JfmzGii5QG6hW8AM5WxzDBVyGc14aLV_Lc_1PkK2ZLc/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

## [Generalization](https://ai-safety-atlas.com/chapters/07/)

*Why might AIs pursue unintended goals?*

In this chapter we turn to how AI systems actually learn and generalize from training. We start by a reminder of what an AI's “goals” concretely means, and how people in AI Safety use the term. This builds on the intuition provided in both the risks and the evaluations chapters between capabilities (what AI systems can do) versus propensities (how they tend to behave by default). We walk you through how capability generalization and goal generalization are separate things using concrete empirical results. We specifically focus on goal misgeneralization which is a different concern from standard ML generalization problems like overfitting. We also explore why goal misgeneralization happens by looking at the theory of neural network loss landscapes which shows how different types of learned algorithms can emerge from different training runs. We pay particular attention to one specific type of learned algorithm - a learned optimizer. Using the concept of learned optimizers as a starting point, we dive deeper into the inner alignment and deceptive alignment (scheming) problems that have been mentioned in many of the previous chapters. We also connect these concerns to evaluation strategies mentioned previously, as well as mitigation strategies which are explored in the subsequent chapter on interpretability. At the end of this chapter you should be able to distinguish between different ways that ML models might generalize between distributions and understand how and why capable AI systems might scheme, deceive, and pursue long term unintended goals.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/07/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
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

## [Scalable Oversight](https://ai-safety-atlas.com/chapters/08/)

*How can we maintain meaningful control when AIs are smarter than us?*

Building on the specification problem explored in previous chapters, we look at how we could maintain meaningful human oversight even when tasks start to exceed human ability to iteratively provide feedback. The core challenge is providing accurate training signals for complex "fuzzy" tasks where success criteria are ambiguous and direct evaluation becomes infeasible. We start by exploring how to break down highly complex tasks into more manageable pieces through techniques like task decomposition. We then explain approaches that seek to elicit an AI's latent knowledge through externalized reasoning oversight and procedural cloning - strategies which focus on aligning the AI's entire reasoning process rather than just its outputs. We dive deeper into theoretical frameworks like Iterated Amplification and Distillation (IDA) and more practical approaches like AI Safety via. debate and weak-to-strong (W2S) generalization. Finally, we examine methods for evaluating these oversight techniques, which includes explanations of sandwiching experiments and meta-level adversarial evaluations. By the end of this chapter, you should understand the existing strategies for maintaining control over AI systems that exceed human capabilities.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/08/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </div>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1DaygDSW0L5dWuJnpSjYPF2XUbW51UoBJsT1cjLYKc2w/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

## [Interpretability](https://ai-safety-atlas.com/chapters/09/)

*How can we understand what's happening inside AI systems?*

Our final chapter examines how we might understand the internal workings of AI models. Progress in interpretability could help address many of the risks and challenges discussed throughout the book - from detecting deceptive behavior to guiding and verifying training outcomes. We primarily focus on mechanistic interpretability - a bottom-up approach that aims to reverse-engineer neural networks by studying how their components process information. We explain both observational methods that analyze model components without modification (like feature visualization and probing), and interventional methods that actively test and alter model behavior (like activation patching and steering). We also look at some efforts to automate and scale interpretability through techniques like Automatic Circuit Discovery (ACDC).

Like all approaches discussed in this book - from governance frameworks to technical safety measures - interpretability is just one tool in our AI Safety toolbox. The path to safer AI systems will likely require combining insights and methods from all these different approaches. While current interpretability techniques face significant limitations, they also represent some of our best attempts at understanding these increasingly complex systems. After reading this chapter, you'll understand both the promise and current limitations of these tools, and how they might contribute to building safer AI systems in the future.

<div class="action-buttons">
    <a href="https://ai-safety-atlas.com/chapters/09/" class="action-button">
        <i class="fas fa-book"></i>
        <span>Read</span>
    </a>
    <div class="action-button disabled" data-tippy-content="Video coming soon">
        <i class="fas fa-video"></i>
        <span>Watch</span>
    </div>
    <a href="https://forms.gle/ZsA4hEWUx1ZrtQLL9" class="action-button">
        <i class="fas fa-comment"></i>
        <span>Feedback</span>
    </a>
    <a href="https://docs.google.com/document/d/1izDWZKR_xB2qj2a8LkbqcnqnjBIC-C7fn-74CIA-m9w/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

# The Path Forward

AI Safety entails huge technical and social coordination challenges. By writing this book, we hope to help you join the growing community of people working on these problems. Whether you choose to contribute through technical research, policy work, or just spreading the word through advocacy, your involvement matters! Every new mind working on these problems brings us closer to ensuring AI development leads to a flourishing future for humanity.
