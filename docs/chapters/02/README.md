# Risks

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
            Jeanne Salle, Charles Martinet, Vincent Corruble, Sebastian Gil, Alejandro Acelas, Evander Hammer, Mo Munem, Mateo Rendon, Kieron Kretschmar, Camille Berger
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
				<div class="meta-value">106 min (core), 12 min (appendix)</div>
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
                    <a href="https://docs.google.com/document/d/1ifYc49Wq-9HuqCXCa8jIr5n6ZOYjZ3FvxE9vHPMcu58/edit?usp=sharing" class="meta-link">Google Docs</a>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

<div class="action-buttons">
    <a href="https://www.youtube.com/watch?v=dhr4u-w75aQ" class="action-button">
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
    <a href="https://docs.google.com/document/d/1evE1rG91DKBuKlWnqPw45QtPxKBz0GlD_ZYrurNdvN4/edit?usp=sharing" class="action-button">
        <i class="fas fa-users"></i>
        <span>Facilitate</span>
    </a>
</div>

# Introduction

The previous chapter explored trends like access to compute, availability of data, scaffolding existing models and improving efficiency of algorithms. According to these trends we can assume that AI capabilities will continue to make progress in the upcoming years. But this still leaves open the question - why are increasing capabilities a problem?

Increasing capabilities are a problem, because as AI models get more capable, the scale of the potential risks also rise.

The first step is to get an understanding of - What exactly are the concerning scenarios? What are the likelihoods of certain harmful outcomes occurring over others?, and what aspects of current AI development accelerate these risks? In this chapter we aim to tackle these fundamental questions and provide a concrete overview of the various risks in the AI landscape.

<figure markdown="span">
![Enter image alt description](Images/TeB_Image_1.png){ loading=lazy }
  <figcaption markdown="1"><b>Figure 2.1:</b> Example of how increasing capabilities might result in different impacts at different levels.</figcaption>
</figure>

We already have identifiable pathways through which AI can be misused. This misuse can lead to catastrophic outcomes that could profoundly impact society. In addition to misuse, there is the risk that we are approaching a critical threshold where the development of dangerously advanced capabilities, such as uncontrolled self-proliferation and self-replicating AI agents, becomes a tangible reality. These capabilities could lead to scenarios where AI systems rapidly expand and evolve beyond human control, potentially causing widespread disruption and harm. This proximity to such advanced capabilities underscores the immediate need for vigilance and proactive measures. Additionally, the current regulatory landscape is beset by significant gaps, lacking comprehensive regulations governing AI development and deployment. This absence of adequate regulatory frameworks further exacerbates the risks associated with AI.

**Risk Decomposition.** The first section begins by categorizing risks into three main groups: Misuse, Misalignment, and Systemic risks. Misuse risks refer to situations where an individual or group intentionally uses AI for harmful purposes. Misalignment risks arise due to the AI systems themselves, due to inherent problems in AI design such as systems pursuing goals that are not aligned with human values. Systemic risks encompass broader issues that emerge when we consider not just an AI system in isolation but rather as just one variable in a global interaction between incentives in various complex systems such as politics, society, and economics where no single entity is liable. In addition to categorizing what causes the risk, we also distinguish between different scales of risk that an AI system could pose: catastrophic, where harm is caused to a large portion of humanity, and existential, where harm is so severe that it might be impossible for human civilization to recover.

The next few sections focus on answering the following questions: What exactly are the risks? What happens and what are we worried about?

**Risky Capabilities**.  We begin by exploring specific AI capabilities that pose significant risks**.** These include the potential of using AI to develop bioweapons and committing cyber offenses, as well as its capacity for deception and manipulation. We also consider the risks associated with AI systems that exhibit agency, autonomous replication, and advanced situational awareness. Understanding these capabilities is crucial for developing targeted risk mitigation strategies.

By understanding the nature and scope of these risks, we can develop more effective strategies for mitigating them and ensuring that the development of AI remains beneficial to humanity. The following chapters will build upon this foundation, exploring specific risk, technical solutions, and policy considerations in greater depth.

**Theoretical arguments vs specific stories**.  Very often in discussions of AI Risks and safety, we often get asked - Specifically what would happen? It's just some software on a computer, what could it actually do? Most people can have a very hard time imagining how exactly this can be dangerous or cause extreme risks. Lack of specifics causes many people to dismiss the underlying arguments altogether. Another problem is that any specific stories that we can come up with are to some extent going to sound like science fiction. Talking about technology that does not currently exist is going to be science fiction almost by definition. Alternatively, if we begin constructing a specific future scenario, the conversation and arguments get into talking about nuances of just that one particular scenario. Often with statements like - "*this one tiny particular thing is something that I don't think the AI will be able to do*", or, "*yeah, but we as humans can probably come up with technique/mitigation 'xyz' to stop this one very specific thing.*" ([Miles, 2022](https://www.youtube.com/watch?v=JVIqp_lIwZg))

While despite these hurdles we have attempted to outline specific stories, it might be best for you as the reader to come away with an intuition of the types of risks involved instead of highly detailed world states. As an example of this type of notion, imagine humanity is similar to an amateur chess player, who has discovered a brilliant new opening for a chess match. This chess player has been able to use this opening against all their other amateur chess player friends and successfully win all their matches.

They now want to bet their entire life savings in a match against Magnus Carlson (World Chess Grandmaster). We think this might be a bad idea and want to dissuade them. They ask - "But how is Magnus Carlsen going to beat me? Show me the exact move that he is going to make to counter my opening." It is a very difficult question to answer because we the authors are not Chess players. We don't really know what moves Magnus Carlsen is specifically going to make. This is akin to asking for extremely detailed specific stories on risk from transformative AI. However, we can say with high confidence that Magnus is going to be able to beat an amateur chess player, no matter how sophisticated their opening move. Similarly a highly capable general purpose AI is going to be a risk to humanity. This is the general notion that we wish to convey.

!!! quote "Yann LeCun Chief AI scientist at Meta and Turing Prize winner, May 2023 ([Heaven, 2023](https://www.technologyreview.com/2023/05/02/1072528/geoffrey-hinton-google-why-scared-ai/))"



    There is no question that machines will become smarter than humans—in all domains in which humans are smart—in the future. It's a question of when and how, not a question of if.




<div class="section-end">
    <span>❧</span>
</div>