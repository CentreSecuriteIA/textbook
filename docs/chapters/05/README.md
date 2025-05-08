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
				<div class="meta-value">154 min (core)</div>
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
                    <a href="https://docs.google.com/document/d/1KI95w27Ce7yWoynE11PJ94IXK0gT0NwP8091s06P7wM/edit?usp=sharing" class="meta-link">Google Docs</a> · <a href="https://www.lesswrong.com/s/GTAGBi3fyw88yArQi" class="meta-link">Alignment Forum</a>
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
   <a href="https://docs.google.com/document/d/1T-UU0FBeElX6cvbWYKpVAl3U4ivrQLHA3IdIWqWKuBA/edit?tab=t.0#heading=h.fo57hwsn3del" class="action-button">
       <i class="fas fa-users"></i>
       <span>Facilitate</span>
   </a>
</div>

# Introduction

!!! quote "Lord Kelvin ([Oxford Reference, 2016](https://www.oxfordreference.com/display/10.1093/acref/9780191826719.001.0001/q-oro-ed4-00006236))"



    When you can measure what you are speaking about, and express it in numbers, you know something about it, when you cannot express it in numbers, your knowledge is of a meager and unsatisfactory kind; it may be the beginning of knowledge, but you have scarcely, in your thoughts advanced to the stage of science.



**The gap between what AI systems can do and what we can reliably measure creates a fundamental safety challenge.** In late 2024, AI researchers created FrontierMath, a benchmark of exceptionally difficult problems they predicted would "*resist AIs for several years*". Just a few months later, OpenAI's o3 model achieved 25.2% accuracy on these supposedly insurmountable problems. This pattern repeats across AI development: tools designed to measure AI capabilities become obsolete almost immediately as models rapidly surpass them. As AI systems approach potentially transformative capabilities in domains like cybersecurity, autonomous operation, and strategic planning, this evaluation gap becomes increasingly dangerous. We cannot afford to discover the full extent of advanced AI capabilities through their emergent real-world impacts.

**Benchmarks provide standardization of measurement but fail to capture the complex risks posed by advanced AI systems.** Early AI development faced a measurement crisis similar to pre-standardized engineering—without reliable metrics, progress was chaotic and unpredictable.

Benchmarks revolutionized AI development by creating standardized metrics that allowed meaningful comparisons between systems. While benchmarks like MMLU, GPQA, or FrontierMath are extremely useful, they still fall short when predicting real-world behavior. They fail to measure what happens when models are pushed to their limits or operate in complex environments where unexpected capability combinations emerge. As we move towards highly capable AI systems, we need stronger safety guarantees in a wider range of scenarios than what benchmarks alone can provide.

**Safety risks emerge from interactions between capabilities, creating a combinatorial challenge.** Individual capabilities like situational awareness or deception appear manageable when measured in isolation, but their combination creates emergent risks fundamentally different from either capability alone. Models might recognize when they're being evaluated and selectively hide capabilities during testing but demonstrate concerning behaviors during deployment. This combinatorial explosion makes comprehensive testing exponentially more difficult but essential for meaningful safety claims. A model passing most safety benchmarks might still harbor dangerous capability combinations that weren't explicitly tested. This is why we need to move measurement of safety critical properties of a system towards comprehensive evaluations.

**Effective safety assessment requires measuring three distinct properties: capabilities, propensities, and control.** Dangerous capabilities evaluations establish upper bounds on what models can do when pushed to their limits through techniques like scaffolding and tool-augmentation. Propensity evaluations reveal what behaviors models tend to exhibit by default, measuring behavioral tendencies rather than just maximum abilities. Control evaluations verify whether safety protocols remain effective when models actively try to circumvent them. This three-part taxonomy provides a systematic framework for safety measurement that helps answer the most decision-relevant questions about AI.

 \
**Safety evaluation requires both behavioral and internal techniques, each providing different forms of evidence.** Behavioral techniques examine model outputs through approaches like red teaming, which systematically attempts to elicit concerning behaviors; supervised fine-tuning, which elicits capabilities by modifying weights rather than just prompting; and best-of-N sampling, which examines multiple potential responses to understand output distributions. These techniques can establish upper bounds on potential capabilities but struggle to tell us “why” models generate certain outputs. Internal techniques complement this by examining model mechanisms directly. For example, sparse autoencoders have successfully extracted interpretable features related to safety-relevant behaviors including deception, sycophancy, and bias. Other techniques like mechanistic interpretability, can help trace computational pathways through the model, enumerative safety can catalogs concepts the model has encoded, and representation engineering can examine how models encode information. Behavioral and internal evaluation techniques are complementary and together provide stronger safety guarantees than either approach alone.

**Evaluation frameworks help transform measurements into concrete development and deployment decisions.** Rather than relying on ad-hoc responses to capabilities, frameworks like Anthropic's Responsible Scaling Policies establish "AI Safety Levels" inspired by biosafety containment protocols, with each level requiring increasingly stringent evaluation requirements and safety measures. These frameworks create "evaluation gates" that determine when scaling can proceed safely—requiring models to pass cybersecurity, biosecurity, and autonomous replication evaluations before development continues. By integrating evaluations into governance structures, we create systematic approaches to managing AI risk rather than relying on ad-hoc decisions.

**Evaluations must be systematically designed to maintain quality and scale across increasingly complex models.** Evaluation design requires careful consideration of affordances—the resources and opportunities provided to the model during testing. By systematically varying affordances from minimal (restricting tools and resources) to maximal (providing all potentially relevant tools and context), we can build a more complete picture of model behavior under different conditions. As the number of safety-relevant properties grows, automating evaluation becomes necessary. We can potentially use model-written evaluations to help address scaling challenges.

**Despite significant progress, AI evaluations face fundamental limitations that threaten their reliability.** The asymmetry between proving presence versus absence of capabilities means we can never be certain we've detected all potential risks. Evaluations can conclusively confirm that a model possesses certain capabilities but cannot definitively prove their absence. Technical challenges include measurement sensitivity—performance can vary based on seemingly trivial changes in prompting formats—and the combinatorial explosion of test cases as we add new dimensions to evaluate. Misalignment might lead to model "sandbagging" (strategic underperformance on evaluations), research shows language models can be made to selectively underperform on tests for dangerous capabilities while maintaining performance on general benchmarks. Organizational incentives might lead labs themselves to do "safetywashing" (misrepresenting capability improvements as safety advancements). These challenges highlight the need for continued research into more robust evaluation methodologies and institutional arrangements that support genuinely independent assessment.

<figure markdown="span">
![Enter image alt description](Images/nvk_Image_1.png){ loading=lazy }
  <figcaption markdown="1"><b>Figure 5.1:</b> Overview of chapter content.</figcaption>
</figure>

This introduction gave you the general overview of many of the concepts that we will be talking about throughout this chapter. The sections will largely proceed in the order that we introduced the ideas above. We begin by exploring how benchmarks have shaped AI development.