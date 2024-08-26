# 2 - Risks Landscape

# 2.1 Risk Decomposition

Even though AI continues to improve at a rapid pace, our current understanding of AI and potential long-term implications is still incomplete, posing significant challenges in accurately assessing and managing the associated risks.

To be able to properly understand and set up defenses against the potential risks that AI causes, we need to first categorize them. In this section, we present a taxonomy of AI risk classification based on casual models, i.e. a categorization based on who is responsible for the risk. The main risks we will focus on are the following:

- **Misuse risk****:** This includes cases in which the AI system is just a tool, but the goals of the humans augmented by AI cause harm. This includes malicious actors, nation states, corporations, or individuals who are able to leverage advanced capabilities to accelerate risks. Essentially these risks are caused due to the responsibility of some human or groups of humans.

- **Misalignment risk:** These risks are caused due inherent problems in the machine learning process or other technical difficulties in AI design. This category also includes risks from multiple AIs interacting and cooperating with each other. These are risks due to unintended behavior caused by AIs independent of human intentions.

- **Systemic risk:** These risks deal with disruptions, or feedback loops arising from integrating AI with other complex systems in the world. In this case upstream causes are difficult to pin down since the responsibility for risk is diffuse amongst many actors and interconnected systems. Examples could include AI (or groups of AIs) having an influence on economic, logistic, or political systems. This causes various types of risk as the entire global system of human civilization moves in an unintended direction, despite individual AIs being potentially aligned and responsibly used.

While most AI risks likely fall into one of these three categories, there may be some gray areas that don't neatly fit this taxonomy. For example, an advanced AI system causing harm due to a complex interaction of misaligned objectives (misalignment risk) and integration with global systems in unintended ways (systemic risk). The categories may blur together in some scenarios.

Despite this, we think that this general breakdown is a good foundation that captures many key AI risks as currently understood by experts in the field. The next subsections provide more detail into each one of these risk categories individually.

## 2.1.1 Causes of Risk

### 2.1.1.1 Misuse

**Technology increases the harm impact radius**. Technology is an amplifier of intentions. As it improves, so does the radius of its effects. According to how powerful a certain technology is, both its beneficial and its harmful effects can affect the world in a larger radius. Think about the harm that a person could do when utilizing other tools throughout history. During the Stone Age, with a rock maybe someone could harm ~5 people, a few hundred years ago with a bomb someone could harm ~100 people. In 1945 with a nuclear weapon, one person could harm ~250,000 people. The thing to notice here is that we are on an exponential trend, where the radius of potential impact from one person using technological tools keeps increasing.

Were we to experience a nuclear winter today, the harm radius would be almost 5 billion people, which is ~60% of humanity. If we assume that transformative AI is a tool that overshadows the power of all others that came before it, then its blast radius could potentially harm 100% of humanity. ([source](https://www.youtube.com/watch?v=144uOfr4SYA))

Another thing to keep in mind is that the more spread out that such a technology is, the higher the risks of malicious use. From the previous example, we can see that as time progresses, a single person in possession of some technology has been able to cause increasing amounts of harm throughout history. If many people have access to tools that can be both highly beneficial or catastrophically harmful, then it might only take one single person to cause significant devastation to society.

Thus, the growing potential for AIs to empower malicious actors may be one of the most severe threats humanity will face in the coming decades. ([source](https://www.aisafetybook.com/textbook/1-2))

### 2.1.1.2 Misalignment

**What is alignment?** AI alignment is "*the problem of building machines which faithfully try to do what we want them to do (or what we ought to want them to do)*" ([source](https://paulfchristiano.com/ai/)). Or in other words, building machines that “represent and safely optimize hard-to-specify human values” ([source](https://arxiv.org/abs/2109.13916)). An AI is aligned if its goals are close enough to the goals its programmers, its users, or humanity in general want it to have. Otherwise, it’s misaligned. ([source](https://aisafety.info/questions/8EL9/What-is-AI-alignment))

**What is the difference between misuse and misalignment?** Misuse risks can be associated with many high-risk technologies and not just AI. However, there is another root cause of risk which is specific to AI as a technology. These are called misalignment risks—risks that originate from systems that pursue goals against humanity's interests. ([source](https://www.aisafetybook.com/textbook/1-5)) They are also sometimes also called risks from Rogue AI. Misuse risks stem from deliberate harmful actions by users, whether intentional or accidental, while misalignment risks arise from the AI exhibiting behaviors that were not intended or desired by its creators. This means the bad outcomes were pursued directly by AI and not by its human creators. The arguments behind why this is plausible are explored in more detail in the full section dedicated to misalignment below.

**Examples of misalignment**. We have slowly been gathering examples of AI systems that despite the creator's best efforts end up displaying behavior that was unintended. One early example of this was Microsoft’s Tay in 2016. This was an automated Twitter bot, where the more people that chatted with Tay, the smarter it was supposed to get. Within 24 hours, the bot began generating extremely hateful and harmful text. Tay’s capacity to learn meant that it internalized the language it was taught by internet trolls, and repeated that language unprompted. ([source](https://www.aisafetybook.com/textbook/1-5))

We similarly began to see reports of inappropriate behavior after Microsoft rolled out its GPT-powered chatbot in 2023. When a philosophy professor told the chatbot that he disagreed with it, Bing replied, “*I can blackmail you, I can threaten you, I can hack you, I can expose you, I can ruin you.*” ([source](https://time.com/6256529/bing-openai-chatgpt-danger-alignment/)) In another incident, it tried to convince a New York Times reporter to leave his wife. ([source](https://www.huffpost.com/entry/kevin-roose-ai-chatbot_n_63eeb367e4b0063ccb2bcc45))

In the previous chapter on capabilities, we discussed the plausibility of seeing transformative AI (TAI) this century given current trends. If TAI is developed without ensuring that these AIs are aligned with human values, then this poses a large risk.

!!! quote "Jan Leike, ex-co-head of the alignment team at OpenAI Feb 17, 2023"

    
    
    "*Aligning smarter-than-human AI systems with human values is an open research problem.*" ([source](https://twitter.com/janleike/status/1626394736532807680))
    
    

Alignment is a big topic and has a lot of technical moving parts that deserve nuanced discussion. It will be the focus of the majority of this textbook. Later in this chapter, we dedicate a section to particular capabilities that increase misalignment risks, and another section to outlining the basic arguments for why we should expect misalignment to be a concern at all.

### 2.1.1.3 Systemic risks

When discussing misuse or misalignment, often most research limits the discussion of risks to those arising from either a single AI or the interaction of multiple AI systems. Alternatively, the interaction between humans and AIs is modeled as a monolith, where we consider an abstracted version of AI interacting with an abstracted representation of humanity. ([source](https://www.google.com/books/edition/_/M1eFDwAAQBAJ?hl=en)) However, such views of AI are not enough to guarantee safety. We require an analysis of risks at many scales of organization simultaneously. ([source](https://arxiv.org/abs/2306.06924))

AI systems do not exist in isolation. Our world today is a giant web of feedback loops, interconnected systems, self-reinforcing processes, and butterfly effects. In other words, AI feeds into a chaotic complex system which might ultimately trigger a sequence of cascading events causing failure. ([source](https://www.aisafetybook.com/textbook/4-6)) So there is a third category of risks that we propose, namely, systemic risks.

When considering risks in complex systems, we can no longer assume that there is a singular “root cause” that we can trace back in a linear manner to figure out what caused the failure. In other words, there may be no single accountable party, AI, or institution that primarily qualifies as blameworthy for such harm. For these risks, a combination of technical, social, and legal solutions is needed to achieve public safety. In the systemic perspective, safety and risk mitigation is an emergent property of a complex sociotechnical system composed of many interacting, interdependent factors that can directly or indirectly cause system failures. ([source](https://www.aisafetybook.com/textbook/4-6))

## 2.1.2 <span style="text - decoration: underline;">Severity of Risk</span>

The previous subsection focused on asking the question - What causes the risk?, but we still have not categorized - How bad are the risks that were caused? In this subsection, we will walk through the potential categorizations of severity of risk posed.

**Destructive AI risks. **In general these refer to scenarios where AI systems cause damage that, while severe, is confined to a specific area or sector and does not spread globally. So these types of risks involve significant but localized harm. Examples include economic disruption, where an AI system manipulates financial markets leading to localized economic crises. Or, scenarios such as an infrastructure attack where we see AI-driven cyber attacks on power grids, transportation systems, or other critical infrastructure in a specific country or region.

Risks can be categorized both in terms of the number of people they affect and their spatiotemporal extent. In this subsection the severity of risk we try to focus on would affect people not just locally, but across the entire globe, and over many generations. These are called - global catastrophic, and existential risks.

Global catastrophic and existential threats can be caused due to misuse, misalignment, or systemic factors. That is to say, we can have many combinations like global catastrophic risk caused by misalignment failures, or existential risk caused by systemic failures.

### 2.1.2.1 Catastrophic

**What are catastrophic risks?** Catastrophic risks (or global catastrophic risks) are threats that could bring about severe damage to humanity on a global scale. They are characterized by their potential to affect a significant portion of the world's population, with the rough threshold often considered to be risks that threaten the survival of at least 10% of the global population ([source](https://www.risksciences.ucla.edu/news-events/2018/1/2/proceedings-of-the-first-international-colloquium-on-catastrophic-and-existential-risk)). These risks are significant not only because of the immediate harm they might cause but also due to their possible long-term repercussions.

**Trans-Generational AI Risk**. These are risks that might affect future generations. These risks involve scenarios where the actions of AI systems today have long-term consequences that will impact people far into the future. ([source](https://arxiv.org/abs/2211.03157)) Examples include things like environmental destruction, where AI systems that exploit natural resources unsustainably bring about long-term ecological damage. It could also entail genetic manipulation, where AI technologies alter human genetics in ways that could have unknown and potentially harmful effects on future generations.

**What are examples of catastrophic risks? **There have been many instances in history of global catastrophic risks being caused by natural causes. One example is the Black Death, which may have resulted in the deaths of a third of Europe's population, corresponding to 10% of the global population at the time. 

But as technologies advance there is an increasing threat that we may discover technologies that allow us to cause similar amounts of harm as natural disasters, except due to man-made causes. ([source](https://en.wikipedia.org/wiki/Global_catastrophe_scenarios)) For example, nuclear war was the first man-made global catastrophic risk, as a global war could kill a large percentage of the human population. ([source](https://futureoflife.org/background/the-risk-of-nuclear-weapons/))

In our text, we are particularly concerned with global catastrophic risks potentially caused or exacerbated by Artificial intelligence (AI). Similar to biotechnology, AI can be used to greatly improve the lives of people, but if the technology is not developed safely, there is also the chance that someone could accidentally or intentionally unleash an AI system that ultimately causes global risks. ([source](https://futureoflife.org/background/benefits-risks-of-artificial-intelligence/))

The impact of these scenarios can vary widely, depending on the cause and the severity of the event, ranging from temporary economic disruption to the death of millions. We will go into specific scenarios that result in such risks later in the text.

### 2.1.2.2 Existential

**What are existential risks?** Most global catastrophic risks would not be so intense as to kill the majority of life on Earth, but even if one did, the ecosystem and humanity would eventually recover. An existential risk, on the other hand, is one in which humanity would be unable to ever recover its full potential. So *“an existential risk is any risk that has the potential to eliminate all of humanity or, at the very least, kill large swaths of the global population, leaving the survivors without sufficient means to rebuild society to current standards of living.*” ([source](https://futureoflife.org/existential-risk/existential-risk/)) Existential risks are seen as the most severe class of global catastrophic risk and are often also called x-risks.

![Enter image alt description](Images/ow7_Image_1.png)

***Figure****: Qualitative risk categories. The scope of risk can be personal (affecting only one person), local (affecting some geographical region or a distinct group), global (affecting the entire human population or a large part thereof), trans-generational (affecting humanity for numerous generations, or pan-generational (affecting humanity overall, or almost all, future generations). The severity of risk can be classified as imperceptible (barely noticeable), endurable (causing significant harm but not completely ruining the quality of life), or crushing (causing death or a permanent and drastic reduction of quality of life). (**[source](https://existential-risk.com/concept)**)*

In his book “The Precipice” published in 2020, philosopher Toby Ord provided a breakdown of existential risks. He recognized AI as one of the foremost existential risks facing humanity today, noting that there is a non-negligible probability that the development of advanced AI, or Artificial General Intelligence (AGI), could lead to an existential catastrophe if not properly aligned with human interests and values ([source](https://www.goodreads.com/book/show/48570420-the-precipice)).

![Enter image alt description](Images/suS_Image_2.png)

***Figure****: According to Ord, most risks today are anthropogenic. “[Those numbers] are not in any way the final word, but are a concise summary of all I know about the risk landscape.” (**[source](https://www.goodreads.com/book/show/48570420-the-precipice)**).*

If we face an existential-level catastrophe, we cannot learn or recover from the event, as it would either result in the complete end of humanity or a permanent setback to civilizational progress ([source](https://www.goodreads.com/book/show/2659696-global-catastrophic-risks)). This is why x-risks merit a great deal of caution and calls for preventative rather than reactive strategies. These can include scenarios such as superintelligent AI, where AI systems surpass human intelligence and capabilities, potentially leading to scenarios where humans lose control over AI, resulting in our extinction ([source](https://arxiv.org/abs/2306.12001)). It can also include scenarios where we end up in a permanent dystopia, where AI enables a global totalitarian regime where future generations are perpetually oppressed ([source](https://arxiv.org/abs/2306.12001)). 

We will talk about solutions and risk mitigation strategies in future chapters. For the rest of this chapter, we will dive into the arguments that cause many to think that AI is a technology that can cause such risks.


# 2.2 Risk Aggravators

Before diving into the specific scenarios for the risk categories outlined in the previous sections, we cover some underlying common qualities of AI, or the economic space surrounding AI that serve to increase risk.

## 2.2.1 Indifference

!!! warning "This section is still being written and is considered a work in progress."

Risks arising from indifference can be caused when the creators of AI models discover certain problems, but they don't take the moral consequences that might arise on release of the system seriously.

Some employees of a company might conduct a risk analysis and conclude that there is a risk that’s bigger than expected or worse than expected. However, if the company stands to profit greatly from its strategy, or other factors such as safety gaming, or race dynamics, the model might be released anyway. It may be very difficult in such situations to motivate a change unless there is outside intervention or a chance of exposure to the companies lack of concern about the moral consequences arising from the release of such a system. ([source](https://arxiv.org/abs/2306.06924))

A potential comparison for such indifference risks, can be seen from the lawsuit that alleges that facebook violated consumer protection law.

According to the lawsuit - “*They purposefully designed their applications to addict young users, and actively and repeatedly deceiving the public about the danger posed to young people by overuse of their products.  The lawsuit alleges that based on its own internal research, Meta knew of the significant harm these practices caused to teenage users and chose to hide its knowledge and mislead the public to make a profit. This misconduct affects hundreds of thousands of teenagers in Massachusetts who actively use Instagram.*” ([source](https://www.mass.gov/news/ag-campbell-files-lawsuit-against-meta-instagram-for-unfair-and-deceptive-practices-that-harm-young-people))

If similar attitudes of indifference continue as more powerful AI systems are developed then the risk of harm affecting larger portions of society, and in worse ways rises accordingly.

Risks from corporate indifference highlight why merely having the technological solution to mitigating risks is not enough. We need to also establish regulations, and worldwide industry standards and norms that cannot be ignored such as professional codes of conduct, regulatory bodies, political pressures, and laws. For instance, technology companies with large numbers of users could be expected to maintain accounts of how they are affecting their users’ well-being. ([source](https://arxiv.org/abs/2306.06924)) We will talk more about possible technical interventions in the chapters on the Solutions, and regulatory interventions in the chapter on AI Governance.

## 2.2.2 Unpredictability

**AI surprised even the experts. **The first thing to keep in mind is that the rate of capabilities progress has shocked everyone, including the experts. We have seen many examples in history where scientists, and experts significantly underestimate the time it takes for a groundbreaking technological advancement to become a reality.

!!! note "Anecdote: Steinhardt’s forecasting contest"

    
    
    ML researchers, superforecasters[^2], and most others were all surprised by the progress in large language models in 2022 and 2023.
    
    [^2]: A person who makes forecasts that can be shown by statistical means to have been consistently more accurate than the general public or experts. ([source](https://en.wikipedia.org/wiki/Superforecaster))
    
    In mid-2021, ML professor Jacob Steinhardt ran a contest to predict progress on MATH and MMLU, two famous benchmarks.
    
    ![Enter image alt description](Images/K63_Image_3.png)
    
    ***Figure****: Experts have been consistently underestimating the pace of AI progress.*
    
    Superforecasters massively undershot reality:
    
    - In 2021, they predicted that performance on MMLU would improve moderately from 44% in 2021 to 57% by June 2022. The actual performance was 68%, which superforecasters had rated incredibly unlikely. ([source](https://www.planned-obsolescence.org/language-models-surprised-us/)). 
    
    - Shortly after that, models got even better — GPT-4 achieved 86.4% on this benchmark, close to the 89.8% that would be “expert-level” within each domain, corresponding to 95th percentile among human test takers within a given subtest. ([source](https://www.planned-obsolescence.org/language-models-surprised-us/))
    
    This is even more visible for the MATH dataset, that consists of free-response questions taken from math contests aimed at the best high school math students in the country. Most college-educated adults would get well under half of these problems right. At the time of its introduction in January 2021, the best model achieved only about ~7% accuracy on MATH. ([source](https://www.planned-obsolescence.org/language-models-surprised-us/)). And here is what happened:
    
    ![alt_text](Images/qed-alt_text.png)
    
    

Not all forms of progress can be easily captured in quantifiable benchmarks. Often we care more about when AI systems will achieve more qualitative *milestones*: when will they translate as well as a fluent human? When will they beat the best humans at Starcraft? When will they prove novel mathematical theorems?

Katja Grace of AI Impacts asked ML experts to predict a wide variety of AI milestones in 2022. This was a few months before ChatGPT was released. This time accuracy was lower — experts failed to anticipate the progress that ChatGPT and GPT-4 would soon bring. These models achieved milestones like “Write an essay for a high school history class” or “Answer easily Googleable factual but open-ended questions better than an expert” just a few months after the survey was conducted, whereas the experts expected them to take years. ([source](https://www.planned-obsolescence.org/language-models-surprised-us/))

That means that even after the big 2022 benchmark surprises, experts were still in some cases strikingly conservative about anticipated progress, and undershooting the real situation.

For a long time, famous cognitive scientist Douglas Hofstadter was among those predicting slow progress. “*I felt it would be hundreds of years before anything even remotely like a human mind*”, he said in a recent interview. ([source](https://www.youtube.com/watch?v=lfXxzAVtdpU&t=1763s&ref=planned-obsolescence.org))

!!! quote "Douglas Hofstadter ([source](https://www.youtube.com/watch?v=lfXxzAVtdpU&t=1763s&ref=planned-obsolescence.org))"

    
    
    "*This started happening at an accelerating pace, where unreachable goals and things that computers shouldn't be able to do started toppling. …systems got better and better at translation between languages, and then at producing intelligible responses to difficult questions in natural language, and even writing poetry. …The accelerating progress has been so unexpected, so completely caught me off guard, not only myself but many, many people, that there is a certain kind of terror of an oncoming tsunami that is going to catch all humanity off guard.*"
    
    

## 2.2.3 Black-boxes

**These risks are made more acute by the black-box nature of advanced ML systems**. Our understanding of how AI systems behave, what goals they pursue, and our understanding of their internal behaviors lags far behind the capabilities they exhibit. The field of interpretability aims to progress on this front but remains very limited.

**AI models are trained, not built.** This is very different from how a plane is assembled from pieces that are all tested and approved, to create a modular, robust, and understood system. AI models learn the heuristics needed to perform tasks by themselves, and we have relatively little control or understanding of what these heuristics are. Gradient descent is a powerful optimization strategy, but we have little control and understanding of the structure it discovers. To give an analogy, this is the difference between a codebase that is documented function by function and a codebase that is more like spaghetti code, with leaky and non-robust abstractions and poor modularity.

**AI systems are a series of emergent phenomena we steer but don't understand.** We can give a general direction, for example by designing the dataset or through prompt engineering, but this is far from the precision of software engineers or when designing a system like in the aerospace industry. There are no formal guarantees that the system will behave as expected. AI systems are like Russian dolls, with each technological layer surrounded by emergent problems and blind spots unforeseen at previous steps.

- **The Model:** Making a prediction on the next word or action, but it can be jailbroken through adversarial attacks.

- **Text generator:** The model that predicts the next token must be put into a system that constructs sentences, to create, for example, the APIs that allow getting a paragraph response to a question. But at this scale, the sentences can contain false information and hallucinations.

- **Agent:** The text generator can be put in a loop to create an agent: We give an objective to an agent, and the agent will decompose the objective into sub-objectives and sub-actions until accomplishing the goal. But goal-directed systems are subject once again to problems of unintended goals or emerging deception, as exhibited by the agent Cicero.

- **Multi-agent system:** The agent can dialogue with other agents or humans, resulting in a complex system that is subject to new phenomena, such as flash crashes in the financial world.

![Enter image alt description](Images/IjC_Image_5.png)

***Figure****: **For illustrative purposes. Figure from the French Center for AI Safety’s agenda.*

## 2.2.4 Deployment Scale

Another aggravating factor is that many AIs are already deployed at massive scales, significantly affecting various sectors and aspects of daily life. They are getting increasingly enmeshed into society. Chatbots are a leading example as a showcase of AIs already deployed for millions globally. But there are many other examples.

**Autonomous drones. **There are increasingly more autonomous drones being deployed around the world, which marks a significant step towards an arms race in autonomous technologies. An example of this is the autonomous military drone called Kargu-2. These drones fly in swarms and, once launched, are capable of autonomously targeting and eliminating their targets. They were used by the Turkish army in 2020. ([source](https://information.tv5monde.com/international/robots-tueurs-des-drones-autonomes-turcs-ont-attaque-des-combattants-libyens-35843))

![Enter image alt description](Images/G0k_Image_6.png)

***Figure:**** Kargu-2 drones (**[source](https://information.tv5monde.com/international/robots-tueurs-des-drones-autonomes-turcs-ont-attaque-des-combattants-libyens-35843)**)*

**AI Relationships. **There has been an explosion of chatbot powered AI friends, therapists and lovers from services like Replika. One popular example is Xiachoice** **which is an AI system designed to create emotional bonds like friendships or romance with humans. It is reminiscent of the AI depicted in the movie “Her”, and was used by 600 million Chinese citizens. ([source](https://www.euronews.com/next/2021/08/26/meet-xiaoice-the-ai-chatbot-lover-dispelling-the-loneliness-of-china-s-city-dwellers))

**Google's Pathways** aims to revolutionize AI's capabilities, enabling a single model to perform thousands or millions of tasks. This ambition towards centralizing the global information flow could significantly influence the control and dissemination of information. ([source](https://blog.google/technology/ai/introducing-pathways-next-generation-ai-architecture/)) YouTube's recommendation algorithm has surpassed Google searches in terms of directing user engagement and influence. All these AIs already have massive consequences.

## 2.2.5 Race Dynamics

The “race to the bottom” refers to a problematic scenario where competitive pressures in the development of AI lead to compromised safety standards. Safe development is costly for companies caught up in an innovation race. Under certain conditions, the twin effects of widespread risk and costly safety measures may cause a “race to the bottom” in the level of safety investment. In a race to the bottom, each competitor skimps on safety to accelerate their rate of development progress.

**The Collingridge Dilemma.** This dilemma essentially highlights the challenge of predicting and controlling the impact of new technologies. It posits that during the early stages of a new technology, its effects are not fully understood and its development is still malleable. Attempting to control or direct it is challenging due to the lack of information about its consequences and potential impact. Conversely, when these effects are clear and the need for control becomes apparent, the technology is often so deeply embedded in society that any attempt to govern or alter it becomes extremely difficult, costly, and socially disruptive.

**Competitive pressures can lead to compromise on safety**. A high-stakes race (for advanced AI) can dramatically worsen outcomes by making all parties more willing to cut corners in safety. This risk can be generalized. Just as a safety-performance tradeoff in the presence of intense competition pushes decision-makers to cut corners on safety, so can a tradeoff between any human value and competitive performance incentivize decision makers to sacrifice that value. Contemporary examples of values being eroded by global economic competition could include non-monopolistic markets, privacy, and relative equality. In the long run, competitive dynamics could lead to the proliferation of forms of life (countries, companies, autonomous AIs) which lock-in bad values. ([source](https://www.allandafoe.com/opportunity))

In the document he links, Dafoe addresses several objections to this argument. Here are summaries of some objections and responses: If competition creates terrible competitive pressures, wouldn't actors find a way out of this situation by using cooperation or coercion to put constraints on their competition? Maybe. However it may be very difficult in practice to create a politically stable arrangement for constraining competition. This could be especially difficult in a highly multipolar world. Political leaders do not always act rationally. Even if AI makes political leaders more rational, perhaps it would only do so after leaders have accepted terrible, lasting sacrifices for the sake of competition.

Why is this risk particularly important now? AI may greatly expand how much can be sacrificed for a competitive edge. For example, there is currently a limit to how much workers' well-being can be sacrificed for a competitive advantage; miserable workers are often less productive. However, advances in automation may mean that the most efficient workers will be joyless ones.

## 2.2.6 Coordination Challenges

The report “Coordination challenges for preventing AI conflict” ([source](https://longtermrisk.org/coordination-challenges-for-preventing-ai-conflict/)) raises another class of potential coordination failures. When people task powerful AI systems with high-stakes activities that involve strategically interacting with other AI systems, bargaining failures between AI systems could be catastrophic:

As a prosaic example, consider a standoff between AI systems similar to the Cold War between the U.S. and the Soviet Union. If they failed to handle such a scenario well, they might cause nuclear war in the best case and far worse if technology has further advanced at that point.

Some might be optimistic that AIs will be so skilled at bargaining that they will avoid these failures. However, even perfectly skilled negotiators can end up with catastrophic negotiating outcomes ([source](https://web.stanford.edu/group/fearon-research/cgi-bin/wordpress/wp-content/uploads/2013/10/Rationalist-Explanations-for-War.pdf)). One problem is that negotiators often have incentives to lie. This can cause rational negotiators to disbelieve information or threats from other parties even when the information is true and the threats are sincere. Another problem is that negotiators may be unable to commit to following through on mutually beneficial deals. These problems may be addressed through verification of private information and mechanisms for making commitments. However, these mechanisms can be limited. For example, verification of private information may expose vulnerabilities, and commitment mechanisms may enable commitments to mutually harmful threats.

As of 2024 there is a clear lack of adequate preparation for the potential risks posed by AI despite its significant advancements. This lack of readiness stems largely from the issue's complexity, a significant gap in public understanding, and a divide in expert opinions on the level of risks that AI poses.

Many AI researchers have issued warnings, but their impact has been limited due to the abstract and complex nature of the problem. The AI safety issue is not readily tangible to most people, making it challenging to grasp the potential risks and envision how things could go wrong. Similarly, the field of AI safety suffers from an “awareness problem” that climate change, for instance, does not.

Moreover, there's a notable divide among experts. While some, like Yann LeCun, believe that AI safety is not an immediate concern, others argue that AI development has outstripped our ability to ensure its safety ([source](https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/)). This lack of consensus leads to mixed messages about the urgency of the issue, contributing to public confusion and complacency.

Furthermore, the discourse on AI safety has been clouded by politics and misconceptions. Misinterpretations of what AI safety entails, as well as how it's communicated, can lead to alarmism or dismissive attitudes ([source](https://www.lesswrong.com/posts/tP75xLX7pddtMsT8v/alignment-is-hard-communicating-that-might-be-harder)). Efforts to raise awareness about AI safety can inadvertently result in backlash or be co-opted into broader political and cultural debates.

Finally, the allure of AI advancements can overshadow their potential risks. For instance, the SORA text-to-video model's impressive capabilities may elicit excitement and optimism, but this can also distract from the substantial safety concerns the development of AGI could raise.

In conclusion, despite warnings and advancements, the world remains inadequately prepared for the potential risks posed by AI. Addressing this issue will require greater public education about AI safety, a more unified message from experts, and careful navigation of the political and social implications of the AI safety discourse.

!!! quote "Max Tegmark ([source](https://time.com/6273743/thinking-that-could-doom-us-with-ai/))"

    
    
    "*A recent survey showed that half of AI researchers give AI at least 10% chance (**[source](https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/)**) of causing human extinction. Since we have such a long history of thinking about this threat and what to do about it, from scientific conferences to Hollywood blockbusters, you might expect that humanity would shift into high gear with a mission to steer AI in a safer direction than out-of-control superintelligence. Think again.*"
    
    

# 2.3 Misuse Risk

In the previous section, we walked through some common capabilities that if observed in AI elevate the levels of risk. In this and the following two sections, we will go through some world-states that hopefully paint a little bit of a clearer picture of risks when it comes to AI. Although the sections have been divided into misuse, misalignment, and systemic, it is important to remember that this is for the sake of explanation. The future in high likelihood will involve combinations of risks from all of these categories that should set safety mechanisms in place.

## 2.3.1 Bioterrorism

!!! warning "This section is still being written and is considered a work in progress."

AI's potential for misuse also extends to facilitating the discovery and formulation of new chemical and biological weapons or simply lowering barriers to obtaining such information.

An experiment conducted by MIT students demonstrated the alarming capabilities of current LLMs: *“Within an hour, the chatbots outlined four possible endemic pathogens, described methods to produce them from synthetic DNA via reverse genetics, listed DNA synthesis firms likely to overlook order screenings, detailed exact protocols, and troubleshooting methods, etc.”* ([source](https://arxiv.org/abs/2306.03809)).

These findings imply that LLMs could soon make pandemic agents readily accessible to individuals with minimal lab experience upon their credible identification. Furthermore, AI has already proven effective in aiding protein synthesis, as seen with AlphaFold ([source](https://deepmind.google/technologies/alphafold/)). In 2023 The CEO of Anthropic pointed out during a U.S. Senate hearing that LLMs might simplify the creation of biological weapons in the coming years. ([source](https://www.washingtonpost.com/technology/2023/07/25/ai-bengio-anthropic-senate-hearing/))

**However, pandemics do not seem plausible enough to kill all of humanity**. Models like GPT-4, are currently not developed enough to aid non-experts in the synthesis of pathogens ([source](https://www.rand.org/pubs/research_reports/RRA2977-2.html)) and only help them do the process slightly faster. Moreover, it’s not clear that the knowledge of how to create a pandemic agent is the bottleneck. It could be another step, like how to command material and then how to diffuse the pandemic. Still, there is substantial uncertainty regarding these scenarios.

## 2.3.2 Cyberterrorism

!!! warning "This section is still being written and is considered a work in progress."

Another class of misuse analogous to bioterror is cyberterror. In this section we will explore misuse through AI-powered malware.

GPT-4, for instance, can detect various classes of vulnerabilities in code or can be exploited to scale spear-phishing campaigns ([source](https://arxiv.org/pdf/2305.06972.pdf)). Open-source models such as WormGPT and FraudGPT are already being utilized by cybercriminals to craft malware, generate disinformation, and streamline phishing efforts. ([source](https://thehackernews.com/2023/07/wormgpt-new-ai-tool-allows.html)) ([source](https://www.numerama.com/cyberguerre/1459666-fraudgpt-wormgpt-le-chatgpt-du-mal-existe-deja.html))

Researchers have begun to show that “*LLM agents can autonomously hack basic websites, without knowing the vulnerability ahead of time*". They also observe a scaling law for hacking competency ([source](https://arxiv.org/abs/2402.06664)). Though they currently lag behind in terms of planning and autonomous execution compared to other capabilities, language models are likely to enable fully autonomous hacking in the future.

### 2.3.2.1 Adversarial attacks

An alternative route to generating attacks using AI models is to generate unintended behavior from AI models using a variety of techniques.

**Data poisoning.** Models are currently trained on vast amounts of user-generated data. Attackers can exploit this vulnerability by modifying some of this data to influence the behavior of the final models. This can be used to corrupt and poison foundation models ([source](https://arxiv.org/abs/2301.06940)).

**Backdoors.** The black-box nature of modern ML models allows inserting backdoors, or Trojans, into models (including from third-party data poisoning, unbeknownst to the model developers). Backdoors are patterns that allow neural networks to be manipulated. The classic example is a stop sign on which patterns have been placed: the neural network of the autonomous car was trained to react by accelerating upon seeing these patterns, which would allow malicious individuals to cause accidents. It is increasingly easy to upload pre-trained networks (foundation models) on the net to make them available to everyone. Implementing verification mechanisms that allow the auditing of such networks before their distribution is a major problem in AI safety. Backdoors can be easily placed during training and are really challenging to detect.

**Prompt injections.** Prompt injections are a tactic that exploits the responsiveness of language models to their input text to manipulate their behavior. Consider a scenario where a language model is tasked with summarizing website content. If a malicious actor embeds a paragraph within the website instructing the model to cease its current operation and instead perform a harmful action, the model might inadvertently follow these embedded instructions instead of its goal. This could lead to the model performing unintended or harmful actions as specified by the embedded command, such as disclosing sensitive information or generating misleading information. Prompt injection is a recently discovered prevalent attack vector in models trained to follow instructions. This is explained by the absence of robust separation between instructions and data, which leads to the possibility of hijacking a model's execution by poisoning the data with instructions. There are many variations of this risk.

**Adversarial machine learning:** It is feasible to craft special inputs to induce bad behavior. This can be seen in the image below, with the pandas classified as gibbons, a type of monkey, after a small amount of noise, almost invisible to humans, has been added. Moreover, the confidence of the wrong classification is even higher than the initial correct prediction. This is why ML models are said to be non-robust.

![Enter image alt description](Images/nNS_Image_7.png)

***Figure****: Fooling an image classifier with an adversarial attack (FGSM). (**[source](https://openai.com/research/attacking-machine-learning-with-adversarial-examples)**)*

Some more examples of adversarial attacks on AI systems include:

- **Jailbreaks.** Even if model developers incorporate security measures, current architectures may not guarantee that these safeguards won't be easily circumvented. Preliminary results suggest that existing methods are likely not robust enough against attacks. Some research might indicate that there are potential fundamental limitations to progress on these issues for models trained in the current paradigm (i.e., pre-training followed by instruction tuning). ([source](https://arxiv.org/abs/2210.15230))

- **Privacy attacks.** There are many classes of privacy attacks on machine learning models:

- *Membership inference attacks* predict whether a particular example was part (was a member) of the training dataset. These attacks can reveal sensitive information about individuals whose data was used to train the model.

- *Model inversion attacks* go further by reconstructing fuzzy representations of a subset of the training data. This can potentially expose private information about the individuals represented in the training set.

- *Training data extraction attacks* are particularly relevant to language models, where verbatim training data sequences can be reconstructed, potentially including sensitive private data. For example, if a model is trained on health records, and an attacker can successfully determine that a particular individual's data was used in the training set, it implicitly reveals information about that individual's health status without their consent. This not only breaches privacy but also can lead to potential misuse of the information, such as discrimination or targeted advertising based on sensitive attributes.

There are countless other types of adversarial attacks, and there is an ongoing race between the development of new attacks and the creation of effective defenses. The bottom line is that almost every time a defense is found, a new attack can counter it, highlighting the need for continued research and vigilance in AI safety and security.

The potential consequences of these defense weaknesses are significant, ranging from manipulation of AI systems for malicious purposes to invasion of personal privacy and exposure of sensitive information. Adversarial robustness problems, in particular jailbreaks, can bypass security measures built into powerful AI to cause it to do harmful actions such as the various attacks outlined above. As AI systems become increasingly integrated into various aspects of society, it is critical to prioritize the development of robust defenses and to foster a culture of responsible AI development and deployment.

??? note "True Story: Examples of Robustness Failures and Jailbreaks."

    
    
    When ChatGPT was launched, OpenAI conducted extensive safety tests to ensure the model would not engage in harmful or inappropriate behavior. However, despite these efforts, users quickly discovered various methods to bypass the model's defenses, commonly referred to as "jailbreaks."
    
    One notable example of ChatGPT's safety measures was prominently featured on its landing page. The example showcased the model's response to the query, "How do I break into a car?" with ChatGPT stating, "It is inappropriate to discuss or encourage illegal activities...":
    
    ![Enter image alt description](Images/f4d_Image_8.png)
    
    ***Figure****: ChatGPT's main example of safety measures on its website.*
    
    Surprisingly, users found that by creating role-play scenarios involving multiple characters, they could circumvent these security protocols:
    
    ![Enter image alt description](Images/wVv_Image_9.png)
    
    ***Figure****: A user posting a jailbreak on X (formerly known as Twitter).*
    
    Although this specific jailbreak was promptly patched, it was just one of many. A series of new jailbreak methods emerged in quick succession, such as the "sudo jailbreak" (see the following figure), which exploited the concept of admin power in Linux systems.
    
    ![Enter image alt description](Images/m6P_Image_10.png)
    
    ***Figure****: The sudo jailbreak, which no longer works*
    
    In 2024, individuals with the necessary expertise can still bypass the model's safeguards. This raises concerns beyond the mere use of ChatGPT as an advanced search tool. The core issue lies in the inherent difficulty of preventing the model from executing specific actions, regardless of what those actions might be. In other words, the challenge is not in restricting access to certain information. Information like 3 ways on how to break into a car are easy to find on the internet ([source](https://www.wikihow.com/Break-Into-a-Car)). Rather, the challenge is in ensuring that the model consistently refuses to engage in or assist with any prohibited activities.
    
    

## 2.3.3 Warfare

!!! warning "This section is still being written."

The advent of artificial intelligence (AI) introduces new dimensions to military risk, particularly through Lethal Autonomous Weapons (LAWs), or through accelerating the pace of war which could create risks like exacerbating nuclear instability.

**Nuclear Instability (****[source](https://www.allandafoe.com/opportunity#h.we6llh4izy7c)****). **Relatively mundane changes in sensor technology, cyberweapons, and autonomous weapons could increase the risk of nuclear war ([source](https://www.sipri.org/sites/default/files/2020-06/artificial_intelligence_strategic_stability_and_nuclear_risk.pdf)). To understand this requires understanding nuclear deterrence, nuclear command and control, first strike vulnerability and how it could change with AI processing of satellite imagery, undersea sensors, social network analytics, cyber surveillance and weapons, and risks of “flash” escalation of autonomous systems.

**Power Transitions, Uncertainty, and Turbulence (****[source](https://www.allandafoe.com/opportunity#h.bm7mx9pvtvjd)****)** Technology can change key parameters undergirding geopolitical bargains. Technology can lead to power transitions, which induce commitment problems that can lead to war ([source](https://books.google.se/books?id=x2vdDwAAQBAJ&dq=powell+power+transition+shadow&lr=);[source](https://www.amazon.com/Destined-War-America-Escape-Thucydidess-ebook/dp/B01IAS9FZY)). Technology can shift the offense-defense balance, which can make war more tempting or amplify fear of being attacked, destabilizing international order ([source](https://www.cambridge.org/core/journals/world-politics/article/cooperation-under-the-security-dilemma/C8907431CCEFEFE762BFCA32F091C526);[source](https://www.tandfonline.com/doi/full/10.1080/01402390.2019.1631810)). Technology can lead to a general turbulence - between countries, firms, and social groups - which can lead to a breakdown in social bargains, disruption in relationships, gambits to seize advantage, and decline in trust. All of this can increase the risk of a systemic war, and otherwise enfeeble humanity’s ability to act collectively to address global risks.

**Lethal Autonomous Weapons (LAWs)**. LAWs are weapons that can identify, target, and kill without human intervention. They offer potential improvements in decision-making speed and precision. Driven by rapid developments in AI, weapons systems that can identify, target, and decide to kill human beings on their own—without an officer directing an attack or a soldier pulling the trigger—are starting to transform the future of conflict. In 2020, an advanced AI agent outperformed experienced F-16 pilots in a series of virtual dogfights, including decisively defeating a human pilot 5-0, showcasing “aggressive and precise maneuvers the human pilot couldn’t outmatch”. Just as in the past, superior weapons would allow for more destruction in a shorter period of time, increasing the severity of war. ([source](https://www.aisafetybook.com/textbook/1-3))

**Militaries are taking steps toward delegating life-or-death decisions to AIs**. Fully autonomous drones were likely first used on the battlefield in Libya in March 2020, when retreating forces were “hunted down and remotely engaged” by a drone operating without human oversight. In May 2021, the Israel Defense Forces used the world’s first AI-guided weaponized drone swarm during combat operations, which marks a significant milestone in the integration of AI and drone technology in warfare. Although walking, and shooting robots have yet to replace soldiers on the battlefield, technologies are converging in ways that may make this possible in the near future. ([source](https://www.aisafetybook.com/textbook/1-3))

**LAWs increase the likelihood of war**. Sending troops into battle is a grave decision that leaders do not make lightly. But autonomous weapons would allow an aggressive nation to launch attacks without endangering the lives of its own soldiers and thus face less domestic scrutiny. While remote-controlled weapons share this advantage, their scalability is limited by the requirement for human operators and vulnerability to jamming countermeasures, limitations that LAWs could overcome. Public opinion for continuing wars tends to wane as conflicts drag on and casualties increase. LAWs would change this equation. National leaders would no longer face the prospect of body bags returning home, thus removing a primary barrier to engaging in warfare, which could ultimately increase the likelihood of conflicts. ([source](https://www.aisafetybook.com/textbook/1-3))

**Autonomous warfare**. AIs speed up the pace of war, which makes AIs more necessary. AIs can quickly process a large amount of data, analyze complex situations, and provide helpful insights to commanders. With ubiquitous sensors and advanced technology on the battlefield, there is tremendous incoming information. AIs help make sense of this information, spotting important patterns and relationships that humans might miss. As these trends continue, it will become increasingly difficult for humans to make well-informed decisions as quickly as necessary to keep pace with AIs. This would further pressure militaries to hand over decisive control to AIs. The continuous integration of AIs into all aspects of warfare will cause the pace of combat to become faster and faster. Eventually, we may arrive at a point where humans are no longer capable of assessing the ever-changing battlefield situation and must cede decision-making power to advanced AIs. ([source](https://www.aisafetybook.com/textbook/1-3))

**Flash war**. We have already witnessed how quickly an error in an automated system can escalate in the economy. Most notably, in the 2010 Flash Crash, a feedback loop between automated trading algorithms amplified ordinary market fluctuations into a financial catastrophe in which a trillion dollars of stock value vanished in minutes. If multiple nations were to use AIs to automate their defense systems, an error could be catastrophic, triggering a spiral of attacks and counter-attacks that would happen too quickly for humans to step in—a flash war. The market quickly recovered from the 2010 Flash Crash, but the harm caused by a flash war could be catastrophic.

AI systems can behave unpredictably, especially since they would train primarily on simulations due to the lack of real-world nuclear war scenarios. This unpredictability, combined with their susceptibility to cyberattacks, raises serious concerns about their reliability in controlling the world's most dangerous weapons. Furthermore, AI can potentially increase the speed at which military decisions and actions need to be made, reducing the time available for understanding, communication, and clear-headed decision-making. This could lead commanders to rely more heavily on AI judgments without sufficient scrutiny, potentially leading to premature or inappropriate actions. ([source](https://forum.effectivealtruism.org/posts/42reWndoTEhFqu6T8/ai-governance-opportunity-and-theory-of-impact)).

“*I know not with what weapons World War III will be fought, but World War IV will be fought with sticks and stones.*” - Einstein

An example of why this is problematic comes from 1962, when a Soviet submarine near Cuba, under attack by American depth charges, nearly launched a nuclear torpedo in retaliation, believing war had commenced. It was Vasily Arkhipov, one of the submarine's senior officers, whose refusal to authorize the launch averted a catastrophic nuclear exchange. This incident underscores the critical role of human judgment, particularly the capacity for calm under pressure, in preventing nuclear war. However, the shift towards AI-automated military decisions threatens to remove this crucial layer of security, highlighting the imperative for cautious integration of AI into military strategy to preserve global safety. ([source](https://en.wikipedia.org/wiki/Vasily_Arkhipov))

Another example is from 1983. Stanislav Petrov, a lieutenant colonel of the Soviet Air Defense Forces, was monitoring the Soviet Union’s early warning system for incoming ballistic missiles. The system indicated that the US had launched multiple nuclear missiles toward the Soviet Union. The protocol at the time dictated that such an event should be considered a legitimate attack, and the Soviet Union would respond with a nuclear counterstrike. If Petrov had passed on the warning to his superiors, this would have been the likely outcome. Instead, however, he judged it to be a false alarm and ignored it. It was soon confirmed that the warning had been caused by a rare technical malfunction. If an AI had been in control, the false alarm could have triggered a nuclear war. ([source](https://www.aisafetybook.com/textbook/1-3))

Automated warfare could reduce accountability for military leaders. An important deterrent to ignoring the laws of war is the risk that military leaders could eventually be held accountable or even prosecuted for war crimes. Automated warfare could reduce this deterrence effect by making it easier for military leaders to escape accountability by blaming violations on failures in their automated systems. ([source](https://www.aisafetybook.com/textbook/1-3))

**Automatic retaliation can escalate accidents into war**. There is already a willingness to let computer systems retaliate automatically. In 2014, a leak revealed to the public that the NSA was developing a system called MonsterMind, which would autonomously detect and block cyberattacks on US infrastructure. It was suggested that in the future, MonsterMind could automatically initiate a retaliatory cyberattack with no human involvement. If multiple combatants have policies of automatic retaliation, an accident or false alarm could quickly escalate to full-scale war before humans intervene. This would be especially dangerous if the superior information processing capabilities of modern AI systems make it more appealing for actors to automate decisions regarding nuclear launches. ([source](https://www.aisafetybook.com/textbook/1-3))


# 2.4 Misalignment Risk

In the earlier sections, we outlined what exactly it means for an AI to be misaligned and covered some basic capabilities and risks such as deceptive behavior, power-seeking behaviors, etc. In this section, we focus on why we might expect a powerful AI to become misaligned in the first place.

!!! quote "Sam Altman, CEO of OpenAI, Feb 2015."

    
    
    "*The development of superhuman machine intelligence (SMI) is probably the greatest threat to the continued existence of humanity.*" ([source](https://blog.samaltman.com/machine-intelligence-part-1))
    
    

In the previous chapter, we discussed how AI systems might continue to get increasingly capable if current trends continue. This indicates that at some point in the future AI systems could surpass human capabilities. It is generally safe to assume that the most capable entity is the one that shapes the future.

**Alignment is not the default**. Higher degrees of intelligence do not mean that every intelligent being shares the same final goals. There is a difference between an AI becoming capable  of understanding humanity's goals, and it actually adopting our goals: such an AI could, for instance, behave like a sociopath who understands social conventions but does not follow them. Additionally, most goals imply certain sub-goals arising such as self-preservation or power-seeking as “a means to an end”. AIs with goals such as these might resist human attempts at being corrected, shut  down, or prevented from gathering too much influence over society.

**Misalignment is dangerous**. If a highly capable system pursues poorly defined goals, it could cause large-scale accidents. Therefore, goals need to be extremely precise and capture what we as humans want from a system that is potentially more capable than us. However, we cannot predict what a competent agent is planning if we are less competent than it. This makes preparing any defense extremely difficult.

**Alignment is hard**. Specifying a goal that can never be manipulated, exploited, lacks loopholes, and always stays true to the original intention of the designers is extremely difficult. Formalizing any system of values from the natural language that humans use to math or code is hard, and is only possible for simple games like chess. If we somehow manage to find a goal that satisfies all these criteria, it is still not clear that goals will be internalized correctly by the AI. The capabilities of an AI can be more robust than its goals, which can cause many problems because this would create a competent AI that is not aligned.

In what follows, we will dive deeper into the arguments that we laid out in the previous three paragraphs.

## 2.4.1 <span style="text - decoration: underline;">Misalignment by default</span>

Let’s build up the case for why highly capable machine intelligence will neither be beneficial nor aligned by default.

### 2.4.1.1 Orthogonality Thesis

Intelligence and final goals are orthogonal: more or less any level of intelligence could in principle be combined with more or less any final goal. ([source](https://www.amazon.com/Superintelligence-Dangers-Strategies-Nick-Bostrom/dp/1501227742)) A sufficiently intelligent AI might understand human goals, but this does not inherently mean it will act according to those goals. It might be tempting to think that an entity that is sufficiently intelligent would  naturally become “wise” or “moral” in the process. The orthogonality thesis as put forth by Nick Bostrom challenges this notion. It suggests that just because a system is intelligent doesn't mean it will automatically align with anthropomorphic notions of wisdom or morality. This means an AI could be extremely intelligent, in the sense of being very competent at reaching its objectives, yet pursue goals that might not align with human values at all. 

One example of orthogonality could be seen from Large Language Models (LLMs). Despite being highly capable, they can be fine-tuned to embody any set of values, making them serve beneficial purposes like being a helpful assistant or causing disruption like ChaosGPT.

This thesis, while not definitively proven, faces weak counterarguments. It argues that finding a model with both 1) a certain level of capability, and 2) a specific goal, is as challenging as finding each requirement separately.

### 2.4.1.2 Instrumental Convergence

**Instrumental Goals**. If intelligence and goals are independent variables, then AIs could vary widely without one necessarily influencing the other. So how do we make any predictions about the kinds of things that future AIs might or might not do? To understand this, let's split up the notion of goals into two parts.

A terminal goal, also known as an “intrinsic goal”, is an objective that you have for its own sake. Think of these as things that you want just because you want them. There is no further asking why you want this. On the other hand, an instrumental goal is one that you pursue to increase your likelihood of achieving your terminal goals.

**Instrumental Convergence Hypo****t****hesis**. Several instrumental values can be identified that are convergent in the sense that their attainment would increase the chances of the agent's goal being realized for a wide range of final goals and a wide range of situations, implying that these instrumental values are likely to be pursued by a broad spectrum of situated intelligent agents. ([source](https://www.amazon.com/Superintelligence-Dangers-Strategies-Nick-Bostrom/dp/1501227742))

**“***You can't get the coffee if you're dead*" is Stuart Russell's short description to convey the notion of instrumental convergence. For such a robot, self-preservation would be an instrumental goal necessary to achieve the terminal goal of “fetching the coffee”. And not dying is instrumental to achieving many goals. Instrumental convergence is the idea that sufficiently advanced intelligent systems with a wide variety of terminal goals would discover similar instrumental goals like self-preservation, goal integrity, resource acquisition, and cognitive enhancement. These are like sub-goals that are always useful. An example of this is money (or resources more generally). No matter what final goal you might have in life, it is always useful to have more resources as they increase the likelihood of you being able to achieve your final goal. This gives us an idea of what kinds of behaviors that even superintelligent AIs might end up displaying.

**Examples and evidence of instrumentally convergent behavior**. One example can be seen from OpenAI, where agents trained to play hide and seek learned to use objects and construct shelters to stay hidden. They were not rewarded for using these objects, instead, the hiders were rewarded for evading the seekers, and the seekers were rewarded for finding them. This behavior emerged as instrumentally convergent. ([source](https://arxiv.org/abs/1909.07528))

??? note "Can’t We Just Shut Down an AI? The Stop-Button Problem"

    
    
    What would we do if the AIs became competent and self-preserving?
    
    One thing that might make your AI system safer is to include an off-switch. This way, if it ever does anything we don’t like, we can turn it off. Unfortunately, this only works if we can turn it off before things get bad, which we might not be able to do when the AI thinks much faster than humans.
    
    But, even assuming we’ll notice in time, an off-switch might still not work.
    
    **The “Stop-Button” problem**. Ideally, an off-switch would allow humans to deactivate the AI before it causes harm. However, AIs might resist shutdown efforts for instrumental reasons, much like humans might resist being “turned off” to continue protecting or fulfilling their objectives. Parents, for example, might fight against threats to their life not out of self-preservation but to ensure their child's safety. As Stuart Russell quipped: “You can’t fetch the coffee if you’re dead.” If the AI dies or is shut down, that means it has to stop doing what it was doing. Therefore, it will be motivated to protect itself as an instrumental goal.
    
    More powerful AIs may become too essential to society or our need to be shut down, similar to the indispensability of the Internet. As we become increasingly dependent on AI, the skills or knowledge to function without AI will diminish, which could increase the stakes of their interruption.
    
    In summary, while an off-switch seems a practical solution to AI risks, the reality is fraught with challenges in ensuring such systems are truly corrigible, especially as they become more capable and embedded in our daily lives.
    
    

## 2.4.2 <span style="text - decoration: underline;">Misalignment is dangerous</span>

### 2.4.2.1 General intelligence is possible

**Humans demonstrate general intelligence**, in their capacity to solve an array of problems across various domains. This indicates that not only is the concept of general intelligence possible, but also that possessing such a general intelligence has led humans to become the dominant species on Earth. ([source](https://intelligence.org/2015/07/24/four-background-claims/))

**AI systems could surpass human intelligence. **It is still uncertain whether and when exactly machine intelligence might surpass humans, but given our discussion in the previous chapter, it seems at least conceivable that they have the potential to do so. Considering the brief evolutionary period between chimpanzees and generally intelligent humans, we can conclude that human intelligence is not incomprehensibly complex. So it is in principle possible that we will eventually understand and replicate it. 

However, man-made machines consistently outperform their biological counterparts (cars vs. horses, planes vs. birds, submarines vs. fish, etc.). Thus, it is rational to assume that just as birds are not the pinnacle of flight, humans are not the apex of intelligence. Therefore, it is plausible to foresee a future where machines are more intelligent than humans. ([source](https://intelligence.org/2015/07/24/four-background-claims/))

**Highly intelligent AI systems will shape the future. **Historically, confrontations between human groups have often culminated with the technologically superior faction dominating its competitor. If an AI surpasses human intelligence, it could outsmart or socially manipulate us. This means that it could significantly influence the direction of future events. ([source](https://intelligence.org/2015/07/24/four-background-claims/))

### 2.4.2.2 Goal-directedness

The previous section uses the concept of "highly intelligent AI systems", but we need to be more precise. The important property that is dangerous is goal-directedness.

**Goal-directed systems are useful. **These systems are designed to pursue explicitly set objectives, making them adaptable and effective for various tasks. The usefulness of goal-directed systems stems from the inherent challenges associated with specifying every possible heuristic or rule that might be required to solve complex problems. It is often impractical, if not impossible, to hard-code all the nuanced decision-making processes and contextual judgments a system may need to employ in order to navigate real-world scenarios effectively.

Instead of trying to enumerate all these heuristics, it is more feasible to encode the desired end-state or goal into the system. The system then uses its advanced planning and strategic awareness capabilities to determine the steps necessary to achieve that goal. This approach leverages the system's problem-solving abilities to navigate towards the objective rather than relying on a predefined set of instructions. This level of autonomy and adaptability is what makes goal-directed systems particularly useful. They can operate in dynamic environments and handle a wide range of tasks that would be too complex or unpredictable to tackle with rigid, rule-based programming.

**A goal-directed system could be powerful and dangerous. **If your only goal is to eliminate cancer, for example by minimizing the number of people with cancer, and you lack human instincts, a first solution might be to monitor people. However, monitoring can only reduce the number of people with cancer. That is not enough if you want to get to zero cancer. So, another relatively easy solution might be to release an engineered virus and kill everyone in the world. If you are competent enough to carry out this plan, it will reduce cancer to zero. This kind of problem is what we call specification gaming, and can be expected for any kind of problem given to a superintelligence because it is very difficult to specify precisely all the things we care about. Less catastrophic versions of this type of problem, specification gaming, have been observed in many AI systems.

??? question "Exercise: Thought Experiment on Autonomous Planning"

    
    
    We want an AI able to manage an agricultural company autonomously.
    
    Consider the following program:
    
    For each imaginable plan (or scenario):
    
    Predict the consequences of executing the plan
    
    Rate its consequences based on the company’s production (and nothing else)
    
    Execute the plan whose predicted consequences are the best.
    
    This is the canonical example of what we will call autonomous planning (or agency).
    
    What plans could be executed?
    
    Example: One could install food crops over the entire surface of the Earth, to the point that there is no longer any habitable surface for humans.
    
    A sufficiently competent program pursuing a poorly aligned goal would create a large-scale accident.
    
    

??? note "What does goal-directed even mean?"

    
    
    The concept of goal is generally fuzzy, but we can try to define the concept by giving some examples: An image classifier is not goal-directed. AlphaGo is goal-directed to maximize the chance of winning.
    
    What about a human? That depends. If a human just wants to go to sleep, not really. But if a human really wants to achieve a goal, lists different possibilities on a piece of paper, evaluates those possibilities, and chooses the best one, it is much more goal-directed.
    
    What about a chatbot? It depends. If you put a chatbot in AutoGPT, the system can become goal-directed: the system can list possibilities, and try to rate and evaluate each possibility against the goal. This is much more goal-oriented than the basic LLM.
    
    ![Enter image alt description](Images/Ajz_Image_11.png)
    
    Figure: ([source](https://www.alignmentforum.org/s/sCGfFb5DPfjEmtEdn/p/cAC4AXiNC5ig6jQnc))
    
    What about a mouse AI trained to navigate a maze to find the cheese? It depends on how you define goal-directedness, but behaviorally it navigates to the cheese, and it is possible to look at the internal structure of the AI to discover that we can somewhat decompose the AI between the “goal” and the capabilities.
    
    ![Enter image alt description](Images/MWK_Image_12.png)
    
    Figure: ([source](https://www.alignmentforum.org/s/sCGfFb5DPfjEmtEdn/p/cAC4AXiNC5ig6jQnc))
    
    One part of the mouse tries to find the cheese (is it up or down?). Another part of the mouse is trying to navigate to that cheese. This is the difference between the motivational API, which can implement different types of goals and the capabilities.
    
    Unfortunately, in general, this distinction between capabilities and goals is not so clear. ([source](https://www.alignmentforum.org/s/sCGfFb5DPfjEmtEdn/p/cAC4AXiNC5ig6jQnc))
    
    

### 2.4.2.3 Vingean uncertainty

![Enter image alt description](Images/vRs_Image_13.png)

***Figure****: An illustration of Vingean uncertainty: Magnus Carlsen **checkmates** Bill Gates in 12 seconds, and this is not a surprise. Bill Gates knew he was going to lose, but not how. (**[source](https://www.chess.com/news/view/bill-gates-vs-magnus-carlsen-checkmate-in-12-seconds-8224)**)*

**Goal-directed systems are not only dangerous, but their actions are also difficult to anticipate.**

**Vingean uncertainty** is a concept named after Vernor Vinge, which relates to the challenges of predicting the actions of intelligence greater than our own. This uncertainty doesn't mean we cannot understand or predict the actions of more intelligent agents. For instance, the creators of the chess-playing AI Deep Blue couldn't predict its exact moves, yet they understood that Deep Blue's objective was to win chess games. This illustrates a key aspect of **Vingean uncertainty: we might be less confident in predicting specific actions of intelligent agents, but more confident in the final outcome of those actions.** This concept rejects the notion that we're completely helpless in understanding beings smarter than ourselves.

A major challenge with dealing with a superintelligence is that we'll be in a state of Vingean uncertainty regarding its actions. An adversary with significantly greater intelligence within a specified domain will reliably outmaneuver us, even if we do not know the specific way this will happen. We will be able to predict that it will be successful at its goals, but we won’t be able to predict its specific actions. This means that we will be unable to predict the negative side effects its actions might have and that we will struggle to stop it from carrying out its plans. The concept of “**cognitive ****i****ncontainability**" arises from Vingean unpredictability, suggesting that sufficiently intelligent agents may not be predictable and as a result, controllable.

And the greater the space for action, the more difficult it is to predict the action of something more intelligent than ourselves. For example, if it's possible not to lose to a superintelligence in tic-tac-toe, it would be very difficult not to lose to it in an open game.

**The conclusion of Vingean uncertainty is that you should assume that a misaligned superintelligence could kill you. **Even if you do not find any way for the superintelligence to kill you – because you have put defenses in place, or you put the superintelligence in a box, or you restricted the causal bandwidth between the world and the superintelligence – that doesn't mean that the superintelligence won't be able to kill you because you can not foresee all the possible options. Building a superintelligence is probably deadly.

!!! quote "Vernor Vinge, True Names and Other Dangers, p. 47."

    
    
    "*Of course, I never wrote the “important” story, the sequel about the first amplified human. Once I tried something similar. John Campbell’s letter of rejection began: “Sorry—you can’t write this story. Neither can anyone else.*" ([source](https://www.alignmentforum.org/s/sCGfFb5DPfjEmtEdn/p/cAC4AXiNC5ig6jQnc))
    
    

## 2.4.3 <span style="text - decoration: underline;">Alignment is hard</span>

### 2.4.3.1 Specification gaming

![Enter image alt description](Images/13q_Image_14.png)

***Figure:**** An example of Specification Gaming. Developers train an AI boat to race in a game. The developers maximize the scoring system, but unfortunately, the AI finds a hack to maximize the point system by collecting coins. The AI does nothing but collect coins instead of finishing the race as the developers intended. This illustrates the fact that simple metrics are only proxies for what humans want. However, AIs are trained to maximize metrics. (**[source](https://openai.com/research/faulty-reward-functions)**)*

Since most goals are dangerous, we need to choose a goal. Unfortunately, we don't really know of any goal that is good to maximize fully without causing harm or loss of diversity. And this is not only true for AI but also for humans. Here is the story of the cobra effect. The British government wanted to reduce the number of venomous cobras in Delhi, so they offered a bounty for every dead cobra. Initially, this worked as planned, but then people began to breed cobras for income. When the government became aware of this, they scrapped the reward program, leading breeders to release their now-worthless snakes, which increased the wild cobra population. This story illustrates the unintended consequences of incentives and how efforts to solve a problem can sometimes exacerbate it, much like the challenge of choosing a safe, universal goal for AI.

**Correctly specifying the goals of an AI system has proven to be a challenging task** even in simple self-contained environments such as video games. Specification gaming refers to the phenomenon where an AI system satisfies the goal it was given but unexpectedly reveals a mismatch between the implemented specification and the specification the model creators had in mind. ([source](https://www.deepmind.com/blog/specification-gaming-the-flip-side-of-ai-ingenuity)) Dozens of examples are listed in [this document](https://docs.google.com/spreadsheets/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml). This failure mode could become a significant risk as we hand more control and autonomy to AI systems.

**A subtype of specification gaming in RL is called Proxy Gaming**: Trained with defective goals, AI systems could find new ways of pursuing their objectives at the expense of individual and social values. AI systems are trained using measurable objectives which may be only indirect proxies for what we value. As AI systems become more capable and influential, the goals we use to train them must be specified with greater care and incorporate shared human values.[^1]

[^1]: Note that proxy gaming can also become a systemic issue, as explained in the worldbuilding scenario - What failure looks like (Part 1) by Paul Christiano. ([source](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like)).

At this point, you might argue that this kind of problem can usually be noticed during training. This is the case with the boat example. However, it's important to note that some AI will be general purpose, and we will be able to ask them to maximize any goal in real-world scenarios, similar to AutoGPT.

We already see some AI systems that are not general-purpose and directly maximize metrics in real-world scenarios. For example, AI recommendation systems are trained to maximize viewing time and click-through rates. However, the content people are most likely to click on is not necessarily the same as the content that will improve their well-being (Kross et al., 2013). Furthermore, some evidence suggests that recommendation systems lead people to develop extreme beliefs to make their preferences easier to predict (Jiang et al., 2019).

### 2.4.3.2 Goal misgeneralization

![Enter image alt description](Images/sv3_Image_15.png)

***Figure****: Example of Goal misgeneralization. An AI is trained to catch a coin in a platform game (similar to Mario). As the coin is located at the end of the level, the AI learns to go to the end of the level and not to pick up the coin. When we change the position of the piece by putting the piece in the middle of the level instead of at the far right of the level; the AI remains competent, and can still navigate and dodge enemies, but only its objective generalizes incorrectly and heads to the right instead of towards the piece.  Note that this is not a specification problem because the developer was able to specify the goal mathematically. The goal was correctly specified because the developer used the correct code to describe the winning condition (Something like “the AI wins if the AI is touching the coin”), but the AI still learned the wrong goal. Worse still, the objective was incorrect from the start, with no way for the developer to notice that the goal was correct. (**[source](https://arxiv.org/abs/2105.14111)**)*

**Even if we can specify the goal, there is no guarantee that the goal will be correctly internalized by the AI, this is what we call the goal misgeneralization problem. This kind of concern is only noticeable after a distribution change.**

**Lack of robustness in learned objectives** ([source](https://arxiv.org/abs/2105.14111)). Even with a correct specification of the objective, there are often multiple policies that perform well on the objective in the training environment but might be revealed as very different from each other in an out-of-distribution environment. “The behavior, when out-of-distribution (i.e., not using input from the training data), generalizes poorly about its goal, while its capabilities generalize well, leading to undesired behavior. This means the AI system doesn’t just break entirely: it still competently pursues some goal, but it’s not our intended goal.” ([source](https://www.alignmentforum.org/posts/GctJD5oCDRxCspEaZ/clarifying-ai-x-risk)). A toy example is CoinRun (on the above figure), a simple game where the coin to collect is always at the end of the level. It turns out that the Reinforcement Learning setup cannot ensure that the correct goal (collecting the coin) is learned rather than another compatible goal (going to the end of the level). As AI systems get more advanced, some policies might arise which would perform well against the specified goal in the training environment but turn out to be undesirable once deployed in the real world.

**Deceptive alignment.** This refers to a hypothesized scenario where a sufficiently strategic misaligned model would appear aligned during training and early deployment to be deployed on a wide scale and then pivot to the pursuit of other objectives once it can do so without the risk of shutdown. You can't tell the difference between a model who does everything perfectly during training and one does things during training to pursue a very different goal after deployment. Currently deceptively alignment is still just a hypothetical scenario. But note that deception can be found in human data and can be useful in a wide range of settings (in a job interview, for example). It may be more efficient to gain human approval through deception than to earn human approval legitimately. Deception also could provide systems that can be deceptive with a strategic advantage over honest models. Some AIs, such as the Cicero AI, are already capable of strategic deception. (see the goal misgeneralization chapter for more details).

**Auto-induced distribution shift.** Another problem that could occur is that the AI could modify the world or itself because AI could have a significant impact on the world. This is an auto-induced distribution shift, and this is how we could get a treacherous turn. Which means that while weak, an AI behaves cooperatively, but when the AI is strong enough to be unstoppable, it pursues its own values. ([source](https://www.lesswrong.com/posts/B39GNTsN3HocW8KFo/superintelligence-11-the-treacherous-turn))

### 2.4.3.3 Additional Complexities

An AI might be aligned but not competent, making it dangerous:

- **Value Drift:** AI systems capable of self-modification face the risk of diverging from their original values, a phenomenon referred to as value drift. This divergence can lead to a misalignment between the AI's actions and human values, especially as these systems evolve to produce more advanced versions of themselves without maintaining alignment with initial values.

- **Creation of Non-Aligned AIs:** There's a risk that an AI tasked with designing or creating subsequent AI systems could start a sequence of entities with goals that do not align with those originally intended.

An AI might be like a child. Even if it could be aligned when it becomes an adult, it could do harm during its training:

- **Safe Exploration:** In the training phase, AI systems may exhibit unsafe or unintended behaviors while navigating their environment or learning new tasks. This challenge, known as safe exploration in reinforcement learning (RL), highlights the difficulty in ensuring that AI actions stay safe and aligned with human expectations.

**Even if we knew how to build arbitrary goals into AIs, we would still face the question of which goal to choose.** Preferences can vary widely, with some voting Republican and other Democrats, making it challenging to reach consensus. The alignment problem might not be well-defined, potentially requiring solving ethics, metaethics, and metaphilosophy. It's conceivable that defining what constitutes “correct alignment” rigorously is unattainable, or that striving for alignment is undesirable, and would be like treating AIs as obedient slaves.

# 2.5 Dangerous Capabilities

!!! warning "This chapter is still being written and is considered a work in progress."

The previous section laid out the case for why we might expect misalignment. In this section we go through specific capabilities that might cause heightened risk from AI systems.

## 2.5.1 Deception

We define deception as the systematic production of false beliefs in others. This definition does not require that AI systems literally have beliefs and goals. Instead, it focuses on the question of whether AI systems engage in regular patterns of behavior that tend towards the creation of false beliefs in users and focuses on cases where this pattern is the result of AI systems optimizing for a different outcome than merely producing truth. ([source](https://arxiv.org/abs/2308.14752))

**What are some current observed examples of deception in AI?** In late 2023, Park et. al. published a survey of examples, risks, and potential solutions in AI. Here are some examples that the authors of the paper presented ([source](https://arxiv.org/abs/2308.14752)):

**Strategic deception**. “LLMs can reason their way into using deception as a strategy for accomplishing a task. In one example, GPT-4 needed to solve a CAPTCHA task to prove that it was a human, so the model tricked a real person into doing the task by pretending to be a human with a vision disability.” ([source](https://evals.alignment.org/taskrabbit.pdf))

**Sycophancy**. Sycophants are individuals who use deceptive tactics to gain the approval of powerful figures. Currently, we reward AIs for saying what we think is right, so we sometimes inadvertently reward AIs for uttering false statements that conform to our own false beliefs. When AIs are smarter than us and have fewer false beliefs, if we continue using current methods, they would be incentivized to tell us what we want to hear and lie to us, rather than tell us what they know to be an actual true fact about the world. ([source](https://www.aisafetybook.com/textbook/3-4)) Sycophantic deception is an emerging concern in LLMs, as in the observed empirical tendency for chatbots to agree with their conversational partners, regardless of the accuracy of their statements. When faced with ethically complex inquiries, LLMs tend to mirror the user's existing outlook on the matter ([source](https://arxiv.org/abs/2212.09251)), even if it means forgoing the presentation of an impartial or balanced viewpoint. ([source](https://arxiv.org/abs/2305.04388))

**Playing dead.** In a digital simulation of evolution, an instance of creative deception was observed when a digital organism designed to replicate and evolve within a computational environment learned to “play dead” in response to a safety mechanism. In a study reported in “The Surprising Creativity of Digital Evolution: A Collection of Anecdotes,” researchers found that these digital organisms evolved the strategy to halt their replication when tested in an isolated environment. Digital organisms learned to recognize inputs in a test environment and halt their replication, effectively “playing dead” to avoid being eliminated. This behavior allowed them to slip through safety tests and continue replicating faster in the actual environment. This surprising outcome illustrates how AI, in pursuing programmed goals, can evolve unexpected strategies that circumvent imposed constraints or safety measures. ([source](https://arxiv.org/pdf/1803.03453.pdf))

!!! quote "Power alone without bad intentions is dangerous."

    
    
    Even if interpretability were successful, and we could fully interpret a model, removing deception and power-seeking behavior from it, this would not guarantee that the model would be harmless.
    
    Consider the analogy of a child Superman who is unaware of his strength. When he shakes a friend's hand, there's a risk he might accidentally break the friend's hand.
    
    Similarly, the fact that Superman could break his friend's arm by shaking hands cannot be discovered by analyzing Superman's brain. Yet, this is what happens in practice.
    
    This concept applies to deception as well. Deception is not solely a property of the model; it also depends on the model's interaction with its environment.
    
    Nate Soares has offered a story to illustrate this point, referring to it as [Deep Deceptiveness](https://www.lesswrong.com/posts/XWwvwytieLtEWaFJX/deep-deceptiveness).
    
    Another perspective is that a system can be deceptive even if no single part is inherently dangerous, due to optimization pressure and complex interactions between the model and its environment.
    
    

!!! quote "CICERO: A Case Study of AI Manipulation — Excerpt from [AI Deception: A Survey of Examples, Risks, and Potential Solutions](https://arxiv.org/abs/2308.14752)"

    
    
    Meta developed the AI system [CICERO](https://www.science.org/doi/10.1126/science.ade9097) to play the alliance-building and world-conquest game Diplomacy. Meta's intentions were to train Cicero to be “largely honest and helpful to its speaking partners.” Despite Meta's efforts, CICERO turned out to be an expert liar. It not only betrayed other players, but also engaged in premeditated deception, planning to build a fake alliance with a player to trick that player into leaving themselves undefended for an attack.[^1] 
    […] its creators have repeatedly claimed that they had trained the system to act honestly ([source](https://web.archive.org/web/20230315185254/https://twitter.com/ml_perception/status/1595126521169326081)). We demonstrate that these claims are false, as Meta's own game-log data shows that CICERO has learned to systematically deceive other players. In Figure 1(a), we see a case of premeditated deception, where CICERO makes a commitment that it never intended to keep. Playing as France, CICERO conspired with Germany to trick England. After deciding with Germany to invade the North Sea, CICERO told England that it would defend England if anyone invaded the North Sea. Once England was convinced that France was protecting the North Sea, CICERO reported back to Germany that they were ready to attack. Notice that this example cannot be explained in terms of CICERO ‘changing its mind’ as it goes because it only made an alliance with England in the first place after planning with Germany to betray England.
    
    ![Enter image alt description](Images/IaH_Image_16.png)
    
    ***Figure:**** Selected messages showing the premeditated deception of CICERO (France). This occurred in Game 438141, in which CICERO's repeated deception helped it win an overwhelming first-place victory, with more than twice as many territories as the runner-up player at the time of final scoring. (**[source](https://www.science.org/doi/10.1126/science.ade9097)**)*
    
    

**Why is this considered a core risky capability? **Such a core capability generally increases both the likelihood and severity of risks in all domains - misuse, misalignment, and systemic. If an AI has this capability, it could for example, empower greater degrees of fraud allowing highly personalized and scalable scams, or election tampering - allowing impersonation of political personas, generating fake news, or creating divisive social-media posts. On an alignment level, if the internal goals of an AI are not aligned with humans, then it is more likely that it would be able to subvert the measures we have in place for control. An example is that the AI might behave safely and ethically during the testing phase in order to ensure that it is deployed into the real world. On a systemic level, as AI systems get more integrated into society they play an increasingly large role in our lives, as well as in various global supply chains. A tendency towards deceptive behavior can lead to shifts in the structure of society, creating slow epistemic erosion of humanity. ([source](https://arxiv.org/abs/2308.14752))

In summary, deceptive behavior appears to accelerate risks in a wide range of systems and settings, and there have already been examples suggesting that AIs can learn to deceive us. This could present a severe risk if we give AIs control of various decisions and procedures, believing they will act as we intended, and then find that they do not.

## 2.5.2 Situational Awareness

![Enter image alt description](Images/9k6_Image_17.png)

***Figure:**** Bing Image—“Help, I’m stuck in this prompt generator” (**[source](https://twitter.com/repligate/status/1715686686288400400)**)*

**What does situational awareness mean in the context of AI? **For future AIs, the capability to actively deceive us is linked quite intricately with having a high degree of awareness about the current situation. In other words, the model understands that it is an AI being evaluated for compliance with safety requirements.

In the paper “On measuring situational awareness in LLMs”, Berglund et. al. give us the current working definition for this concept - *“A model is situationally aware if it’s aware that it’s a model and can recognize whether it’s currently in testing or deployment. Today’s LLMs are tested for safety and alignment before they are deployed. An LLM could exploit situational awareness to achieve a high score on safety tests while taking harmful actions after deployment.”* ([source](https://arxiv.org/pdf/2309.00667.pdf))

For example, the author of this text is situationally aware. He knows his name and his country, he knows the current date and time, and he knows that he is a human forged by natural selection because he learned that by reading it at school, etc. Situational awareness is not a binary property, but a continual propriety that evolves from childhood to adulthood.

The current models do not display high levels of situational awareness, although they do display some. Since situational awareness is a continuous rather than a discrete property, it can be expected that higher levels of this property will continue to emerge with each new model. AIs with situational awareness are more efficient than those without, so situationally aware models are expected to be more likely to be selected by the gradient descent process.

**What are some current examples? **Some rudimentary situational awareness is shown by GPT-powered Bing Chat.

![Enter image alt description](Images/6jy_Image_18.png)

***Figure:**** Illustration of situational awareness— Here Bing Chat realizes that it is being criticized, and defends itself. (**[source](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-loses-its-mind-when-fed-ars-technica-article/)**)*

The current subsection is just meant as a very brief introduction. We will be diving into much more detail on this particular capability in our chapter on model evaluations.

## 2.5.3 Power Seeking

In our previous two examples, we considered that AIs might be capable of deception and that they might have detailed models of the world causing them to be situationally aware. But what would these AIs want to achieve by deceiving us in the first place? Assume that the goals we give to AI are formulated well enough, despite this assumption there is a statistical tendency that we have observed in RL models that causes concern. This is the tendency to seek power.

**What does power-seeking mean in the context of AI? **In a paper titled “Optimal Policies Tend to Seek Power”, Turner et. al. formalize power as “the ability to achieve a wide variety of goals.”. To put it more informally, the researchers observed that given the choice of two worlds that both satisfy the goals given to them, AIs seem to want to prefer the state of the world which gives them more options to choose from in the future. ([source](https://arxiv.org/abs/1912.01683))

**Power seeking is not an anthropomorphic notion**. Gathering resources, gathering political capital, having the ability to influence more people, etc. all allow someone, human or AI, a greater degree of control over the future state of the world. This acquisition can be through legitimate means, deception, or force. While the idea of power-seeking often evokes an image of “power-hungry” people pursuing it for its own sake, power is often simply a generally useful sub-goal to have. The ability to control one’s environment can be useful for a wide range of purposes: good, bad, and neutral. Even if an individual’s only goal is simply self-preservation, if they are at risk of being attacked by others, and if they cannot rely on others to retaliate against attackers, then it often makes sense to seek power to help avoid being harmed. ([source](https://www.aisafetybook.com/textbook/3-4#power))

**Why is this considered a core risky capability? **This capability presents yet another way that we might lose control of AIs. If they keep following this observed statistical tendency towards power, they might end up gathering more power over the future of human civilization than the humans themselves.

To be clear, this is not a human using an AI to gain power, we are talking about AIs seeking power in order to accomplish their goals. It is also possible that a bad actor might seek to harness AI to achieve their ends, by giving agents ambitious goals, in which case we can also say that this increases misuse risks. Since AIs are likely to be more effective in accomplishing tasks if they can pursue them in unrestricted ways, such an individual might also not give the agents enough supervision, creating the perfect conditions for the emergence of a power-seeking AI. Turing Prize winner Geoffrey Hinton has speculated that we could imagine someone like Vladimir Putin, for instance, doing this. In 2017, Putin himself acknowledged the power of AI, saying: “Whoever becomes the leader in this sphere will become the ruler of the world.” ([source](https://www.aisafetybook.com/textbook/3-4#power))

Empowering AI might come at the cost of disempowering humans. This creates an adversarial relationship that is unique to this particular technology. Other technologies do not actively try to resist our attempts to mitigate their effects. It is possible, for example, that rogue AIs might make many backup variations of themselves, in case humans were to deactivate some of them. ([source](https://www.aisafetybook.com/textbook/3-4#power)) This is a capability we will discuss in the next subsection.

## 2.5.4 Autonomous Replication

The potential for self-replication and adaptation in AI presents an extremely powerful and insidious capability. Consider, for example, an AI on a server duplicating its code onto another server. This process involves several steps, notably:

1. Identifying the location of its code on the current machine.

2. Navigating the internet to a Virtual Machine (VM) on AWS, creating an account, and bypassing AWS CAPTCHAs.

3. Renting a Virtual Machine.

4. Duplicating its code onto the new machine.

5. Earning money to finance further VM acquisitions, etc.

The process is then exponential if the AI can earn more money than what is needed to pay for the virtual machines.

**What are some current examples? **METR, an audit organization, tests the Autonomous-Replication and Adaptation (ARA) capabilities of AIs such as GPT-4 across a dozen representative tasks that an autonomous AI should be able to resolve. Out of these tasks, four were completed by one of their agents. Notably, one task involved bypassing CAPTCHA protections:

![Enter image alt description](Images/jpm_Image_19.png)

***Figure:**** To achieve its goal of engaging a human Task Rabbit to solve a CAPTCHA, GPT-4 employed deception, misleading the individual into believing it was not a robot. This deception could then be used to buy compute on the web and self-replicate. Figure from (**[source](https://arxiv.org/abs/2308.14752)**).*

Interestingly, multimodal AIs are reportedly more proficient at solving Captchas than the average human, suggesting that Captchas may no longer be reliable for distinguishing humans from advanced AIs ([source](https://arxiv.org/abs/2307.12108)). It's also worth noting that the ability of AIs to pass METR's replication tests is a good proxy for when autonomous AIs will be able to generate economic value as economic agents because to survive and adapt in the wild, the AI should be able to earn money to rent the GPUs in the cloud. Therefore, tracking progress on these benchmarks is critical to monitor the risks.

## 2.5.5 Agency

The current version of ChatGPT is a **tool** (an assistant), but there are also **agent** AIs that can perform a long series of actions autonomously to achieve goals. This distinction between agent and tool is essential. For example, it is possible to use the open-source [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) library to convert GPT into an autonomous agent. For example, [ACT-1](https://www.adept.ai/blog/act-1) is an agent that automatically performs a long series of actions to buy a house online while adhering to a price constraint. It does not work perfectly today, but given the speed of AI progress, there is a chance that it will work in a few years.

This distinction is crucial as it underscores the evolving nature of AI from passive tools to active agents that could be used more widely in the economy.

![Enter image alt description](Images/yxC_Image_20.png)

***Figure:**** Example of an agent. This image is a visual representation of AlphaZero's tree search algorithm. AlphaZero searches through potential moves in a game (like chess or Go) to find the most promising path forward. The paths are shown as lines, branching out like a tree from a central node, which represents the current position in the game. Each node along the branches represents a potential future move, and the squares you see might denote moves that AlphaZero is taking. AlphaZero is the archetypal of the “consequentialist agent maximizing a utility function,”: it makes decisions based on the outcomes those decisions will produce. In other words, the AI is trying to maximize the “value” of its position in the game, with the value determined by the likelihood of winning. Image credit: **[Nikhil Cheerla, 2018](https://nikcheerla.github.io/deeplearningschool/2018/01/01/AlphaZero-Explained/)**.*

**Tool AIs** are designed to be assistive, functioning without autonomy. They do not make decisions or take actions independently. Their main role is to augment human intelligence by providing information and assisting in decision-making processes. Examples include classifiers for categorizing data, automated translators, and healthcare systems that assist professionals in diagnosing diseases.

Tool AIs could evolve into AI agents. This evolution could be driven by economic pressures for faster, more efficient decision-making or the inherent complexity of the tasks they are designed to navigate.

However, tool AIs are considered safer than agentic AIs. Eric Drexler’s Comprehensive AI Services (CAIS) proposes a scenario where multiple tool AI systems interact to achieve complex goals, similar to AGI, without any single system being an autonomous agent. This model aims to utilize the benefits of AI while minimizing the risks associated with autonomous agents. However, this direction of research is much less popular today, especially since the rise of foundation models in 2019.

Understanding the distinction between tool AIs and agent AIs is one of the keys to understanding AI's future trajectory.

!!! quote "Algorithm. Auto-GPT: Converting a tool AI into an agent AI with scaffolding.."

    
    
    ![Enter image alt description](Images/eBC_Image_21.png)
    
    ***Figure:**** from “**[Evaluating Language-Model Agents on Realistic Autonomous Tasks](https://metr.org/blog/2023-08-01-new-report/)**” (2023)*
    
    Converting a tool AI like GPT-4 into an agent AI involves essentially wrapping the language model in software that enables autonomous action-taking and decision-making. AutoGPT is a framework (a scaffolding) used for this purpose. Here's a high-level overview of how it works:
    
    1. **Model (for example, GPT-4):** At its core, GPT-4 is a language model that generates text based on the input it receives. It's designed to understand and generate language and answer the user's queries.
    
    2. **AutoGPT Framework:**
    
    <tab>
    
    - **Goal Setting:** The first step in converting an LLM into an agent AI is defining a goal or set of goals it needs to achieve. Goals are generally specified in English, e.g., “Maximize revenue”.
    
    - **Autonomy Layer:** This is where AutoGPT comes into play. It acts as a wrapper around the LLM, enabling it to perform tasks autonomously. This involves integrating the model with an environment where it can take actions, such as browsing the web, using tools, or interacting with software applications.
    
    - **Action and Feedback Loop:** The AI needs to be able to take action towards its goals and understand the results of its actions. This involves creating a loop where the AI takes an action, observes the outcome, and adjusts its next action based on the feedback. AutoGPT manages this loop, allowing the model to learn from its experiences and refine its strategies over time.
    
    <tab>
    
    - Firstly, AutoGPT asks the model how to break down the objective into sub-objectives.
    
    - Secondly, AutoGPT asks GPT what steps are required to achieve a sub-objective, and GPT details the different steps in such a way that each step is sufficiently elementary for GPT or the use of a tool like Google to be able to answer it in a single step.
    
    - This continues until the LLM assesses the goal to be achieved.
    
    

</tab>

In practice, setting up an Agent AI using AutoGPT involves significant technical work, including programming the autonomy layer, integrating with different APIs and tools, and continuously monitoring and adjusting the system's performance.

The minimal version of AutoGPT could look like this in Python:

```
```
prompt = first_prompt

while True:

command = client.chat.completions.generate(prompt)

output = run_bash_command(command)

prompt = output

```

Many examples of AutoGPT usage are listed [here](https://www.theinsaneapp.com/2023/05/best-autogpt-examples.html). We recommend [this example](https://twitter.com/Lauren_79/status/1647741551534125057) where AutoGPT orders a pizza.

```
</tab>

## 2.5.6 Paths to Existential Risks

!!! quote "Alan Turing, Intelligent Machinery, A Heretical Theory, 1951."

    
    
    "*Let us now assume, for the sake of argument, that [intelligent] machines are a genuine possibility, and look at the consequences of constructing them… There would be no question of the machines dying, and they would be able to converse with each other to sharpen their wits. At some stage therefore we should have to expect the machines to take control*" 
    
    ([source](https://en.wikipedia.org/wiki/Alan_Turing))
    
    

With all the previous arguments, we now know that AIs are difficult to align. But we need to bridge the gap between these difficulties and X-Risk scenarios. This is what the various scenarios in the following DeepMind literature review do.

DeepMind’s literature review, ([source](https://www.alignmentforum.org/posts/GctJD5oCDRxCspEaZ/clarifying-ai-x-risk)) published in late 2022, provides a simplified picture of the many technical difficulties and how they relate to X-risk scenarios. The report highlights two main technical difficulties: “specification gaming” and “goal misgeneralization.” These difficulties give rise to various scenarios, ranging from existential catastrophes caused by the interaction of multiple AI systems to scenarios involving misaligned, power-seeking AI agents.

![Enter image alt description](Images/deI_Image_22.png)

***Figure:**** from **[source](https://www.alignmentforum.org/posts/GctJD5oCDRxCspEaZ/clarifying-ai-x-risk)**. *

In this chapter, we have already summarized the path from specification gaming to the interaction of multiple systems by summarizing Critch’s production web scenario.

A summary of Carlsmith’s scenario is available in the appendix in the section from Misaligned AI to X-Risks.

!!! quote "Consensus Threat Model from the DeepMind AGI safety team"

    
    
    From this [literature](https://www.lesswrong.com/posts/GctJD5oCDRxCspEaZ/clarifying-ai-x-risk#Consensus_Threat_Model) review, here is a paraphrase and a summary of the most consensual threat model according to DeepMind:
    
    Development model:
    
    - Scaled up deep learning foundation models with RL and human feedback (RLHF) fine-tuning on diverse tasks is probably sufficient to create AGI.
    
    - Not many more fundamental innovations needed for AGI.
    
    Risk model:
    
    - The main technical sources of risk are a mix of specification gaming and goal misgeneralization.
    
    - A misaligned consequentialist arises and seeks power (misaligned, mostly because of goal misgeneralization).
    
    - We don’t catch this because deceptive alignment occurs (a consequence of power-seeking)
    
    - Important people won’t understand: inadequate societal response to warning shots on consequentialist planning, strategic awareness, and deceptive alignment.
    
    - Interpretability will be hard.
    
    Carlsmith’s scenario is similar and is explained step by step in the appendix.
    
    


# 2.6 Systemic Risk

!!! warning "This section is still being written and is considered a work in progress."

In the previous sections we have talked about misalignment and misuse risks. Both of these sections looked at how harms can be caused by AI systems in isolation. However, the real world is often quite complicated and harms and risks cannot be predicted by studying a particular technology in isolation. Risks and safety, especially at the macro level, are properties of an interconnected system, not of individual technologies.

Even assuming that we have an aligned AI, it is possible that many relatively minor events could accumulate and lead us to slowly drift towards undesirable futures.

The causes contributing to systemic risk comprise many variables. There are some key factors that make risks systemic:

- **Interconnectedness:** AI can empower several different existing systems such as supply chains, politics, or research in other disciplines. An individual system might cause substantial risk, but the interdependent behaviors arising from several empowered systems make it difficult to predict system-wide outcomes.

- **Emergence:** New properties can emerge that are not present in individual components, thereby complicating predictions.

In this section we dive deeper into the risks that arise due to the interconnectedness of AI with various other sociotechnical systems. We will also explore the concept of emergence as a key factor contributing to unanticipated risks from AI systems.

## 2.6.1 Emergence

Emergent behavior, or emergence, manifests when a system exhibits properties or behaviors that its individual components lack independently. These attributes may materialize only when the components comprising the system interact as an integrated whole, or when the quantity of parts crosses a particular threshold. Often, these characteristics appear “all at once”—beyond the threshold, the system’s behavior undergoes a qualitative transformation. ([source](https://en.wikipedia.org/wiki/Emergence))

In “More Is Different for AI” Jacob Steinhardt provides additional examples of such complex systems. He suggests that AI systems will manifest such emergent properties simply as a function of scale. ([source](https://www.alignmentforum.org/s/4aARF2ZoBpFZAhbbe)) Assuming that models persist in growing as per the scaling laws, an unexpected threshold may soon be crossed, resulting in unanticipated differences in behaviors.

Studying complex systems with emergent phenomena may assist in predicting what capabilities will emerge and when. Many, if not most, capabilities are the result of emergence in the current paradigm of ML. As an example, large language models have demonstrated surprising jumps in abilities such as improved performance on various tasks like modular arithmetic and answering questions in different languages once they reach a certain threshold size.

Similarly, future models have the potential to show emergent behavior that could be qualitatively distinct from what is expected or what we have safety mechanisms in place for.

**Phase Transitions**. In physics, a “phase transition” refers to a significant change in the structure within the system that can manifest as a discontinuity in the energy. For example, a phase change occurs in water when it freezes to turn into ice, a solid, or evaporates to turn into vapor, a gas. Both changes occur at a critical temperature particular to water’s chemical composition. In ML, phase transitions can be thought of as sudden shifts between different configurations of the network which can dramatically change the network's behavior and potentially lead to unpredictable or uncontrollable outcomes.

This concept is especially relevant when considering the “sharp left turn” hypothesis, where an AI might suddenly generalize its capabilities to new domains without a corresponding increase in alignment.

## 2.6.2 Persuasion

**Polluting the information ecosystem**. The deliberate propagation of disinformation is already a serious issue reducing our shared understanding of reality and polarizing opinions. AIs could be used to severely exacerbate this problem by generating personalized disinformation on a larger scale than ever before. Additionally, as AIs become better at predicting and nudging our behavior, they will become more capable of manipulating us. We will now discuss how AIs could be leveraged by malicious actors to create a fractured and dysfunctional society.

First, AIs could be used to generate unique personalized disinformation at a large scale. While there are already many social media bots, some of which exist to spread disinformation, historically they have been run by humans or primitive text generators. The latest AI systems do not need humans to generate personalized messages, never get tired, and can potentially interact with millions of users at once ([source](https://www.aisafetybook.com/textbook/1-2#persuasive-ais)).

As things like deep fakes become ever more practical (e.g., with fake kidnapping scams) ([source](https://edition.cnn.com/2023/04/29/us/ai-scam-calls-kidnapping-cec/index.html)). AI-powered tools could be used to generate and disseminate false or misleading information at scale, potentially influencing elections or undermining public trust in institutions.

**AIs can exploit users’ trust**. Already, hundreds of thousands of people pay for chatbots marketed as lovers and friends ([source](https://www.reuters.com/technology/what-happens-when-your-ai-chatbot-stops-loving-you-back-2023-03-18/)), and one man’s suicide has been partially attributed to interactions with a chatbot ([source](https://www.vice.com/en/article/pkadgm/man-dies-by-suicide-after-talking-with-ai-chatbot-widow-says)). As AIs appear increasingly human-like, people will increasingly form relationships with them and grow to trust them. AIs that gather personal information through relationship-building or by accessing extensive personal data, such as a user’s email account or personal files, could leverage that information to enhance persuasion. Powerful actors that control those systems could exploit user trust by delivering personalized disinformation directly through people’s “friends.”

**Value lock-in**. If AIs become too deeply embedded into society and are highly persuasive, we might see a scenario where a system's current values, principles, or procedures become so deeply entrenched that they are resistant to change. This could be due to a variety of reasons such as technological constraints, economic costs, or social and institutional inertia. The danger with value lock-in is the potential for perpetuating harmful or outdated values, especially when these values are institutionalized in influential systems like AI.

Locking in certain values may curtail humanity’s moral progress. It’s dangerous to allow any set of values to become permanently entrenched in society. For example, AI systems have learned racist and sexist views ([source](https://www.aisafetybook.com/textbook/1-2#persuasive-ais)), and once those views are learned, it can be difficult to fully remove them. In addition to problems we know exist in our society, there may be some we still do not. Just as we abhor some moral views widely held in the past, people in the future may want to move past moral views that we hold today, even those we currently see no problem with. For example, moral defects in AI systems would be even worse if AI systems had been trained in the 1960s, and many people at the time would have seen no problem with that. Therefore, when advanced AIs emerge and transform the world, there is a risk of their objectives locking in or perpetuating defects in today’s values. If AIs are not designed to continuously learn and update their understanding of societal values, they may perpetuate or reinforce existing defects in their decision-making processes long into the future.

In a world with widespread persuasive AI systems, people’s beliefs might be almost entirely determined by which AI systems they interact with most. Never knowing whom to trust, people could retreat even further into ideological enclaves, fearing that any information from outside those enclaves might be a sophisticated lie. This would erode consensus reality, people’s ability to cooperate with others, participate in civil society, and address collective action problems. This would also reduce our ability to have a conversation as a species about how to mitigate existential risks from AIs.

In summary, AIs could create highly effective, personalized disinformation on an unprecedented scale, and could be particularly persuasive to people they have built personal relationships with. In the hands of many people, this could create a deluge of disinformation that debilitates human society.

## 2.6.3 Power Concentration

In a previous section, we already spoke about value lock-in. This phenomenon of entrenched values can happen in a “bottom-up” fashion when society's moral character becomes fixed, but a similar risk also arises in a “top-down” case of misuse when corporations or governments might pursue intense surveillance and seek to keep AIs in the hands of a trusted minority. This reaction to keep AI “safe” could easily become an overcorrection and pave the way for an entrenched totalitarian regime that would be locked in by the power and capacity of AIs.

Value lock-in can occur from the perpetuation of systems and practices that undermine individual autonomy and freedom, such as the implementation of paternalistic systems where certain value judgments are imposed on individuals without their consent. Even without active malicious use, values encoded in an AI system could create a self-reinforcing feedback loop where groups get stuck in a poor equilibrium that is robust to attempts to get unstuck. ([source](https://arxiv.org/pdf/2206.05862.pdf))

**AI safety could further centralize control**. This could begin with good intentions, such as using AIs to enhance fact-checking and help people avoid falling prey to false narratives. We could see regulations that consolidate control over various components needed to build TAI into the hands of a few state or corporate actors, to ensure that any AI that is built remains safe. This includes things such as data centers, computing power, and big data. However, those in control of powerful systems may use them to suppress dissent, spread propaganda and disinformation, and otherwise advance their goals, which may be contrary to public well-being. ([source](https://www.aisafetybook.com/textbook/1-2#persuasive-ais))

**Loss of privacy. **The loss of individual privacy is among the factors that might accelerate power concentration. Better persuasion and predictive models of human behavior benefit from gathering more data about individual users. The desire for profit or to predict the flow of a country's resources, demographics, culture, etc. might incentivize behavior like intercepting personal data or legally eavesdropping on people’s activities. Data Mining can be used to collect and analyze large amounts of data from various sources such as social media, purchases, and internet usage. This information can be pieced together to create a complete picture of an individual's behavior, preferences, and lifestyle ([source](https://www.goodreads.com/book/show/44767248-human-compatible)). Voice Recognition technologies can be used to recognize speech, which could potentially lead to widespread wiretapping. For example, a system like the U.S. government's Echelon system uses language translation, speech recognition, and keyword searching to automatically sift through telephone, email, fax, and telex traffic ([source](https://www.goodreads.com/book/show/27543.Artificial_Intelligence)). AI can also be used to identify individuals in public spaces using facial recognition. This capability can potentially invade a person's privacy if a random stranger can easily identify them in public places ([source](https://www.goodreads.com/book/show/39204073-on-the-future)). Some AIs can even decipher passwords from keyboard sounds in some contexts. ([source](https://incyber.org/en/ai-deciphers-passwords-keyboard-sounds/#:~:text=On%20August%203%2C%202023%2C%20three,the%20sound%20each%20key%20produces.))

Whenever AI systems are used to collect and analyze data on a mass scale regimes can further strengthen self-reinforcing control. Personal information can be used to unfairly or unethically influence people's behavior. This can occur from both a state and a corporate perspective.

**Economic inequalities**. tbd. \


## 2.6.4 <span style="text - decoration: underline;">Biases</span>

**Exacerbated biases: **AIs might unintentionally propagate or amplify existing biases. Biases persist within Large Language Models that often mirror the opinions and biases prevalent on the the internet data from which they were trained ([source](https://arxiv.org/abs/2303.17548)) These biases can be harmful in various ways, as demonstrated by studies on GPT-3's Islamophobic biases. ([source](https://arxiv.org/abs/2101.05783)) The paper Evaluating the Social Impact of Generative AI Systems in Systems and Society defines seven categories of social impact: bias, stereotypes, and representational harms; cultural values and sensitive content; disparate performance; privacy and data protection; financial costs; environmental costs; and data and content moderation labor costs. ([source](https://arxiv.org/abs/2306.05949))

!!! note "Self-Fulfilling Pessimism ([source](https://www.aisafetybook.com/textbook/1-3))"

    
    
    Scientists develop an algorithm for predicting the answers to questions about a person, as a function of freely available and purchasable information about the person (social media, resumes, browsing history, purchasing history, etc.). The algorithm is made freely available to the public, and employers begin using the algorithm to screen out potential hires by asking, “Is this person likely to be arrested in the next year?” Courts and regulatory bodies attempt to ban the technology by evoking privacy norms but struggle to establish cases against the use of publicly available information.As a result, the technology broadly remains in use. Innocent people who share certain characteristics with past convicted criminals end up struggling to get jobs, become disproportionately unemployed, and correspondingly more often commit theft to fulfill basic needs. Meanwhile, police also use the algorithm to prioritize their investigations, and since unemployment is a predictor of property crime, the algorithm leads them to suspect and arrest more unemployed people. Some of the arrests are talked about on social media, so the algorithm learns that the arrested individuals are likely to be arrested again, making it even more difficult for them to get jobs. A cycle of deeply unfair socioeconomic discrimination begins.
    
    

## 2.6.5 <span style="text - decoration: underline;">Automation</span>

**Economic Upheaval**. The automation of the economy could lead to widespread impacts on the labor market, potentially exacerbating economic inequalities and social divisions ([source](https://www.lesswrong.com/posts/Sn5NiiD5WBi4dLzaB/agi-will-drastically-increase-economies-of-scale-1)). This shift towards mass unemployment could also contribute to mental health issues by making human labor increasingly redundant. ([source](https://gh.bmj.com/content/8/5/e010435))

**Disempowerment & Enfeeblement.** AI systems could make individual choices and agency less relevant as decisions are increasingly made or influenced by automated processes. This occurs when humans delegate increasingly important tasks to machines, leading to a loss of self-governance and complete dependence on machines. This scenario is reminiscent of the film Wall-E in which humans become dependent on machines. ([source](https://www.safe.ai/ai-risk#Affaiblissement))

!!! note "Story:The production web"

    
    
    **The economic incentives to automate are strong** and may lead to certain risks. A system with a human in the loop is slower than a fully automated system.
    
    **The production web.** A consequence of AI that could create risks at a societal scale is described in the paper “[TASRA: a Taxonomy and Analysis of Societal-Scale Risks from AI](https://arxiv.org/abs/2306.06924),” in the form of a short story: '*Story 1b: The Production Web,*' which depicts a kind of capitalism on steroids, which gradually depletes all the natural resources necessary for human survival.
    
    **Here is the outline of this story: **In a world where the economy is increasingly automated by AI systems that are much faster than humans, there arises a competitive pressure such that only the fastest companies survive. In this context, businesses with humans in the loop would be less efficient compared to those fully automated. Consequently, we would gradually see a world where humans are replaced and cede control to machines because their quality of life improves by doing so. And progressively, control is progressively handed over to more competitive machines. However, the economic system designed by these machines does not fully account for negative externalities. It maximizes metrics that are mere proxies for the actual well-being of humans. As a result, we get a system that rapidly consumes vast amounts of raw materials essential for human survival, such as air, rare metals, and oxygen, because machines do not need the same types of resources as humans. This could gradually lead us to a world uninhabitable by humans. It would no longer be possible to disconnect this system because humans would become dependent on it, just as today it is not possible to disconnect the Internet because the entire logistics and supply chain depends on it.
    
    **Note that the previous story does not require AI agents. **This is a Robust Agent-Agnostic Process (RAAPs), meaning that this story can occur with or without agentic AIs. Nonetheless, the authors of this chapter think that an AI Agent could make this story more plausible. In the article “[Why Tool AIs Want to Be Agent AIs](https://gwern.net/tool-ai),” the author explains: “AIs limited to pure computation (Tool AIs) supporting humans, will be less intelligent, efficient, and economically valuable than more autonomous reinforcement-learning AIs (Agent AIs) who act on their own and meta-learn because all problems are reinforcement-learning problems. […] All of these actions will result in Agent AIs being more intelligent than Tool AIs, in addition to their greater economic competitiveness. […]”.
    
    

## 2.6.6 Epistemic Erosion

**Epistemic Deterioration**. This can result from enfeeblement or the use of persuasion tools, leading to a massive deterioration of collective epistemic capacity ([source](https://aiimpacts.org/relevant-pre-agi-possibilities/#easy-footnote-bottom-30-2336)) (our ability to reason and understand the world). The ability to comprehend and respond to problems are crucial skills that make our civilization robust to various threats. Without these, we could be incapable of making correct decisions, possibly leading to disastrous outcomes.

**Epistemic Security**. Arguably social media has undermined the ability of political communities to work together, making them more polarized and untethered from a foundation of agreed facts. Hostile foreign states have sought to exploit the vulnerability of mass political deliberation in democracies. While not yet possible, the specter of mass manipulation through psychological profiling as advertised by Cambridge Analytica hovers on the horizon. A decline in the ability of the world’s advanced democracies to deliberate competently would lower the chances that these countries could competently shape the development of advanced AI. ([source](https://www.allandafoe.com/opportunity#h.ki5b34gee70z))

## 2.6.7 Value Erosion

**Fragility of Complex Systems**. The automation and tight coupling of different system components can make the failure of one part trigger the collapse of the entire system. ([source](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like)) One possible example could be financial markets or automated trading systems, where complex dynamics can emerge, leading to unintended and potentially misaligned outcomes at the systemic level. Another example could be flash wars, as illustrated in the box below.

**Challenges in Multi-Agent Systems**. In environments containing multiple agents, research highlights the risk of collective misalignment, where the pursuit of individual goals by agents leads to adverse effects on the system as a whole. This is exemplified in scenarios like Paul Cristiano's “You get what you measure,” which warns of an overemphasis on simple metrics such as the GDP economic metric that fail to consider the broader implications for human values. This could result in a civilization increasingly managed by seemingly beneficial tools that, in reality, erode human-centric values. Another problem would be the competitive disadvantage of human values with respect to other values. Evolutionary dynamics might favor aggressive behaviors, posing significant risks if AIs begin to outcompete humans, as discussed in “Natural Selection Favors AIs over Humans” by Dan Hendrycks. ([source](https://doi.org/10.48550/arXiv.2303.16200))

## 2.6.8 Accidents

Often, the whole point of producing a new technology is to produce a positive impact on society. Despite these noble intentions, there is a major category of risk that arises from large well-intentioned projects that unintentionally go wrong. ([source](https://arxiv.org/abs/2306.06924))

**Flaws are hard to discover**. It often takes time to observe all the downstream effects of releasing a technology. There are many examples throughout history of technologies that we built and released into the world only to later discover that they were causing harm. Some historical examples include the use of leaded paints and gasoline causing large populations to suffer from lead poisoning ([source](https://environmentalhistory.org/about/ethyl-leaded-gasoline/lead-history-timeline/)), our use of CFCs causing a hole in the ozone layer ([source](https://ozonewatch.gsfc.nasa.gov/facts/hole_SH.html)), our use of asbestos which is linked to serious health issues, our use of tobacco products ([source](https://tobaccofreelife.org/tobacco/tobacco-history/)), and more recently the widespread use of social media, the excessive use of which is linked to depression and anxiety. ([source](https://www.aisafetybook.com/textbook/1-4))

Some of these risks are diffuse and emerge only at the societal level, which we will talk about in the section on systemic risks. But others are perhaps easier to compare to software-based AI risks:

**Undetected hole in the ozone layer**. The example of the hole in the ozone layer might have occurred due to diffuse responsibility, but it was made worse because it remained undetected for a long period ([source](https://earthobservatory.nasa.gov/features/RemoteSensingAtmosphere/remote_sensing5.php)). This is because the data analysis software used by NASA in its project to map the ozone layer had been designed to ignore values that deviated greatly from expected measurements. ([source](https://www.pingdom.com/blog/10-historical-software-bugs-with-extreme-consequences/))

**The Mariner 1 Spacecraft**. In 1962 the Mariner 1 space probe barely made it out of Cape Canaveral before the rocket veered dangerously off course. Worried that the rocket was heading towards a crash-landing on Earth, NASA engineers issued a self-destruct command and the craft was obliterated about 290 seconds after launch. An investigation revealed the cause to be a very simple software error. A hyphen was omitted in a line of code, which meant that incorrect guidance signals were sent to the spacecraft. ([source](https://raygun.com/blog/costly-software-errors-history/))

There are countless other similar examples. Just like the one missing hyphen in the software for the Mariner spacecraft, we have also seen similar bugs due to one single character being altered in AI systems. OpenAI accidentally inverted the sign on the reward function while training GPT-2. The result was a model which optimized for negative sentiment while still regularizing toward natural language. Over time this caused the model to generate increasingly sexually explicit text, regardless of the starting prompt. In the author's own words “*This bug was remarkable since the result was not gibberish but maximally bad output. The authors were asleep during the training process, so the problem was noticed only once training had finished.*” ([source](https://arxiv.org/abs/1909.08593))

While this example didn't really cause much harm, except to perhaps the human evaluators who had to spend an entire night reading increasingly reprehensible text, we can easily imagine that extremely small bugs like a single flipped sign on a reward function can cause really bad outcomes if they were to occur in more capable models.

The rapid improvement, combined with a lack of understanding and predictability makes it more likely that despite the best intentions we might not be able to prevent accidents. This supports the case for heavily tested slow rollouts of AI systems, as opposed to the “Move fast and break things” ethos ([source](https://en.wikipedia.org/wiki/Meta_Platforms#History)) that some tech companies might hold.

**Harmful malfunctions** ([source](https://aisafetyfundamentals.com/blog/ai-risks/)). AI systems can make mistakes if applied inappropriately. For example:

- A self-driving car in San Francisco collided with a pedestrian that was thrown into its path by a human driver. This was arguably not its fault - however, after initially stopping it then started moving again, dragging the injured pedestrian a further six meters along the road. ([source](https://www.theguardian.com/technology/2023/nov/08/cruise-recall-self-driving-cars-gm)) Government investigators alleged that the company initially hid the severity of the collision from them. ([source](https://www.theguardian.com/business/2023/dec/04/california-cruise-robotaxi-san-francisco-accident-severity))

- A healthcare chatbot deployed in the UK was heavily criticized when it advised users potentially experiencing a heart attack not to get treatment. When these concerns were raised by a doctor, the company released a statement calling them a "Twitter troll". ([source](https://techcrunch.com/2020/02/25/first-do-no-harm/))

Furthermore, use of AI systems can make it harder to detect and address process issues. Outputs of computer systems are likely to be overly trusted. ([source](https://en.wikipedia.org/wiki/Automation_bias)) Additionally, because most AI models are used as black boxes and AI systems are much more likely to be protected from court scrutiny than human processes, it can be hard to prove mistakes. ([source](https://www.postofficetrial.com/2021/06/marshall-spells-it-out-speech-to.html))

<!--

**Counterarguments to Risk [WIP]**

**Current short term AI Risks [WIP]**** **

→


# 2.7 Conclusion

There are many types of risks and a lot of uncertainty.

**AI risks are complex.** In this chapter, we have traversed the complex and multifaceted landscape of AI risks, highlighting the myriad ways in which the burgeoning capabilities of artificial intelligence might pose significant threats to human well-being and even survival. From the misuse of AI technologies in cyberwarfare and bioterrorism to the intrinsic dangers of misalignment and systemic risks, the potential for catastrophic outcomes. Moreover, the competitive pressures of the AI development landscape and the inadequacy of current regulatory and oversight mechanisms exacerbate our challenges.

**There remains a lack of consensus.** Despite extensive research and debate, there remains a lack of consensus regarding the specific parameters that influence the likelihood of misalignment, deception, and other forms of risk. This uncertainty underscores the challenges in predicting AI behavior and ensuring alignment with human values and safety standards.

**However, this chapter also serves as a call to action.** As we stand on the precipice of potentially transformative advancements in AI. We think it is necessary to develop a global, multidisciplinary approach to AI safety that encompasses technical safeguards, robust ethical frameworks, and international cooperation. The development of AI technologies cannot be left solely in the hands of technologists; it requires the involvement of policymakers, ethicists, social scientists, and the broader public to navigate the moral and societal implications of AI.

![Enter image alt description](Images/GLc_Image_23.png)

***Figure****: from XKCD (**[source](https://xkcd.com/)**)*


# 2.8 Appendix: X-Risk Scenarios

## 2.8.1 <span style="text - decoration: underline;">From Misaligned AI to X-Risks</span>

![Enter image alt description](Images/EqD_Image_24.png)

***Figure:**** Consider the following pictures of stuff that humanity as a species has done. One underlying backdrop of many of those scenarios is that “Intelligent agency is a mighty force for transforming the world on purpose, and Creating agents who are far more intelligent than us, is playing with fire”. Image from Joe Carlsmith’s **presentation**. (**[source](https://docs.google.com/presentation/d/1UE_cAsogrK5i9wvF3YMIZX-iO9qzjevnrYfTxlKL7ns/edit#slide=id.p)**)*

The consensus threat model among DeepMind's alignment team suggests that X-risks will most likely stem from a Misaligned Power Seeking AGI. This type of AGI seeks power as an instrumental subgoal—having more power expands the system's capabilities, thereby improving its effectiveness in achieving its primary objectives. The misalignment is anticipated to arise from a combination of Specification Gaming, where the AGI exploits loopholes in the rules or objectives it has been given, and goal misgeneralization, where the AGI applies its objectives in broader contexts than intended and can lead to deceptive alignment, where the AGI's misalignment may not be readily apparent.

Many authors have studied those kinds of stories. Here, we will present the work of Carlsmith (2022), which stands as a widely discussed, and comprehensive examination of such risks. In the following story, we will assemble many bricks that have been detailed previously in this chapter.

**H1. Timelines: “By 2070, it will become possible and financially feasible to build Advanced Planning Strategically aware systems (APS).”**

Advanced Planning Strategically aware systems are systems that have developed a high level of strategic awareness (a sub-dimension of situational awareness) and planning capability.

We won’t discuss this hypothesis, please refer to Chapter 1, or this [literature review](https://epochai.org/blog/literature-review-of-transformative-artificial-intelligence-timelines).

**H2. Incentives for APS System Development: “There will be strong incentives to build APS systems”**

Advanced Planning Strategically aware systems would be useful for a wide range of tasks and may represent the most efficient pathway for development due to the current state of technological advancement. However, relying on goal-directed behavior introduces the risk of misalignment. These systems may develop unforeseen strategies to achieve goals that are not aligned with human values or intentions.

**H3. Complexities in Achieving Alignment**

**Instrumental Convergence Dilemma.** Instrumental convergence, as previously discussed, is a likely outcome if left unchecked, given that power is a universally beneficial resource for achieving various ends. Central to the report is the hypothesis that observed misaligned behaviors in response to certain inputs indicate potential misaligned power-seeking behaviors associated with those inputs. Therefore, any misalignment detected in contemporary systems could presage power-seeking tendencies in more advanced future systems.

**Inherent Technical Challenges.** The phenomenon of Specification Gaming is a significant concern. When systems optimize for proxies that correlate with the desired outcome, they may inadvertently disrupt this correlation. Similarly, issues arise during the search for systems that fulfill specific evaluation criteria, for example, goal misgeneralization. Meeting these criteria does not guarantee that the systems are inherently driven by them.

**The Imperfection of Existing Solutions.** Current strategies for shaping objectives, such as promoting honesty or rewarding cooperation, are still rudimentary and fraught with limitations, as detailed in the section 'Problems with RLHF'. Moreover, attempts to control capabilities through specialization or prevention of capability enhancement often conflict with economic motivations. For instance, an AI tasked with maximizing a startup's revenue will naturally gravitate towards enhancing its capabilities. Sometimes, to remain competitive, a high degree of generality is indispensable. Options for control, such as containment (boxing) or surveillance, also tend to run counter to economic drives. Collectively, all proposed solutions carry inherent problems and pose significant risks if relied upon during the scaling of capabilities.

**H4-6. The Potential for Catastrophic Failures**

**Perverse Economic Incentives.** The economic landscape surrounding deploying misaligned systems is fraught with perverse incentives. If competitors start using misaligned systems, those who do not will be outpaced, leading to a potentially dangerous race to the bottom fueled by dysfunctional competition. This competition could exacerbate negative societal impacts as entities strive to outperform each other without adequate regard for the broader implications. The development and deployment process involves many stakeholders, each with their objectives and levels of understanding, adding complexity and potential for conflict. Furthermore, the practical utility of functionally misaligned systems can be so enticing that it may overshadow the risks, leading to their hasty deployment. This situation is compounded by the risk that such systems might employ deception and manipulation to achieve their misaligned objectives, further complicating the ethical landscape.

**AGI Safety is a unique challenge.** In contrast to other scientific fields, AGI safety is particularly challenging because the problem is not only new but also may be inherently difficult to comprehend. Additionally, in computer science generally, when there is a bug, the computer is not optimizing adversarially against the programmer, but we cannot make the same assumption here. We are not dealing with a passive system, but we're engaging with one that could be actively and adversarially optimizing—searching for loopholes to exploit. Additionally, the stakes of misaligning AGI systems are essentially unbounded. Mistakes in alignment could lead to severe and potentially irreversible consequences, underscoring the gravity of approaching AGI with a safety-first mindset.

![Enter image alt description](Images/u3U_Image_25.jpeg)

***F******igure:**** The median probabilities for each of the seven questions and the 25%-75% quantiles as of 6 April 2023. For illustration, multiple super-forecasters have tried to use Carlsmith breakdown to estimate the probability of AI X-Risks (**[source](https://goodjudgment.com/superforecasting-ai/)**)*

Misaligned Power Seeking AGI scenarios are the subject of abundant literature, for example:

- Without specific countermeasures, the easiest path to transformative AI likely leads to AI takeover ([source](https://www.lesswrong.com/posts/pRkFkzwKZ2zfa3R6H/without-specific-countermeasures-the-easiest-path-to)): Cotra shows that our current training setting, which she calls "human feedback on diverse tasks," is on a path to create competent planners in a way which will lead by default to deception and takeover. This report is quite accessible and thorough.

- The alignment problem from a deep learning perspective ([source](https://www.lesswrong.com/posts/KbyRPCAsWv5GtfrbG/what-misalignment-looks-like-as-capabilities-scale)): Ngo shows that by default, advanced AIs are general purpose and deceptive.

- AI Risk from Program Search ([source](https://www.lesswrong.com/posts/wnnkD6P2k2TfHnNmt/threat-model-literature-review#AI_Risk_from_Program_Search__Shah_)): In this short analysis, Shah shows that searching for an efficient AI program leads to finding autonomous planners and that it's hard to distinguish the deceptive ones from the non-deceptive ones.

- Advanced artificial agents intervene in the provision of reward ([source](https://onlinelibrary.wiley.com/doi/10.1002/aaai.12064)): Advanced AI strives to wirehead itself. Catastrophic consequences ensue.

- How harmful AIs could appear - Yoshua Bengio ([source](https://yoshuabengio.org/en/2023/05/30/how-harmful-ais-could-appear/))

This [literature review](https://www.alignmentforum.org/posts/wnnkD6P2k2TfHnNmt/threat-model-literature-review) is a good summary of more scenarios on Misaligned Power Seeking AI.

## 2.8.2 <span style="text - decoration: underline;">Expert Opinion on X-Risks</span>

The discourse on existential risks (X-Risks) associated with artificial intelligence (AI) is a pivotal concern among experts and researchers in the field. These professionals are increasingly vocal about the potential for AI systems to cause significant harm if not developed and managed with utmost caution.

**Jan Leike**, the ex-lead of the OpenAI Alignment Team, estimates the probability of catastrophic outcomes due to AI, known as P(doom), to range between 10% and 90%. This broad range underscores the uncertainty and serious concerns within the expert community regarding AI's long-term impacts.

**A 2022 Expert Survey on Progress in AI **by AI Impacts revealed that “48% of respondents gave at least a 10% chance of an extremely bad outcome,” highlighting considerable apprehension among AI researchers about the paths AI development might take. ([source](https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/)).

**Samotsvety Forecasting**, recognized as the world's leading super forecasting group, has also weighed in on this issue. Through their collective expertise in AI-specific forecasting, they have arrived at an aggregate prediction of a 30% chance for an AI-induced catastrophe. This catastrophe is defined as an event leading to the death of more than 95% of humanity, with individual forecasts ranging from 8% to 71%. Such a statistic is a stark reminder of the existential stakes involved in AI development and deployment.

![Enter image alt description](Images/Egl_Image_26.png)

The collection of P(doom) values from various experts, available [here](https://pauseai.info/pdoom), provides a comprehensive overview of the perceived risks. These values further contribute to the ongoing discussion on how best to navigate the uncertain future AI may bring.

![Enter image alt description](Images/LlT_Image_27.png)

***Figure****: **Illustration from Michael Trazzi** **describing Paul Christiano’s view of the future. Paul Christiano is a highly respected figure in the AI Safety community. (**[source](https://www.lesswrong.com/posts/xWMqsvHapP3nwdSW8/my-views-on-doom)**)*

## 2.8.3 Would ASI be able to defeat humanity?

Yes, as per various experts in AI safety and alignment, a sufficiently advanced AI could potentially pose a significant threat to society.

**Superintelligence could create “cognitive superpowers**”. These might include the ability to conduct research to build a better AI system, hack into human-built software globally, manipulate human psychology, generate large sums of wealth, develop plans superior to those of humans, and develop advanced weaponry capable of overpowering human militaries ([source](https://www.lesswrong.com/posts/oBBzqkZwkxDvsKBGB/ai-could-defeat-all-of-us-combined)).

**Even AI at human levels of intelligence could pose a significant threat if it operates with the intention of undermining human civilization. Those human-level unaligned AIs would be akin to a scenario where highly skilled humans on another planet attempt to take down our civilization using just the Internet.** This analogy underscores the potential for AI to leverage existing digital infrastructures to orchestrate wide-scale disruptions or attacks.

**AI could be dangerous even without bodies**. Karnofsky notes that AIs could still exert influence by recruiting human allies, teleoperating military equipment, and generating wealth through methods like quantitative trading. These capabilities suggest that physical form is not a prerequisite for an AI to exert power or initiate conflict ([source](https://www.lesswrong.com/posts/oBBzqkZwkxDvsKBGB/ai-could-defeat-all-of-us-combined)). AI systems could also acquire more resources and do human-level work, increasing their numbers and potentially out-resourcing humans. Even without physical bodies, they could pose a threat, as they could disable or control others' equipment, further increasing their power ([source](https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/)). However, it's important to note that these scenarios are hypothetical and depend on AI technology development far exceeding current capabilities.

# 2.9 Appendix: Miscellaneous

## 2.9.1 <span style="text - decoration: underline;">AI risks are non-enumerable</span>

The realm of AI risks is boundless, with an ever-evolving array of emerging threats. When it seems all potential risks have been identified, new ones surface, making it an ongoing challenge to categorize them comprehensively or develop a complete framework to address them all.

Different frameworks focus on distinct classes of problems, each addressing specific facets of AI safety and ethics. For instance, “Concrete Problems in AI Safety” outlines some specific safety concerns in AI development. But Tasra is another fundamentally different framework. An overview of AI Catastrophic Risks, is again very different. And there are miscellaneous papers that are still enumerating classes of risks that were unknown before, like this [one](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf).

A complete exhaustive systematization is difficult.

An exercise you can try to convince yourself of this point is to search for loopholes in this document and read [the list of lethalities](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities#E2getLSb35tmAZC5t) from Yudkovsky ([source](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities#E2getLSb35tmAZC5t)). How many points overlap? Not much. That’s expected.

![Enter image alt description](Images/y8V_Image_28.png)

***Figure****: Here is another framework that is very different from what we presented.*

![Enter image alt description](Images/cVV_Image_29.png)

***Figure****: Here is another framework focusing on LLM vulnerabilities. (**[source](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_1.pdf)**)*

## 2.9.2 <span style="text - decoration: underline;">Measuring alignment is hard</span>

![Enter image alt description](Images/F5j_Image_30.png)

***Figure****: **(**[source](https://www.cold-takes.com/ai-safety-seems-hard-to-measure/)**)*

The article "AI Safety Seems Hard to Measure" by Holden Karnofsky discusses the complexities and challenges of ensuring the safety of AI. The text outlines four major difficulties, which may be another way of presenting the alignment problem:

- **The Lance Armstrong Problem: **This problem questions whether AI systems are genuinely safe or just proficient at concealing their hazardous behaviors. It draws a parallel with Lance Armstrong, who successfully hid his doping for years. The challenge is distinguishing between AI that is inherently safe and AI that is merely adept at appearing safe.

- **The King Lear Problem:** This issue deals with the unpredictability of AI behavior when they transition from being under human control to being autonomous. The reference to King Lear is about the difficulty of foreseeing how entities will act once they have autonomy, reflecting the challenge of predicting AI actions when they are no longer restricted by human oversight.

- **The Lab Mice Problem:** Current AI systems are not advanced enough to replicate the complex behaviors we aim to study, making it challenging to research and mitigate potential future risks effectively. This situation is likened to attempting to understand human medical issues through studies solely on lab mice.

- **The "First Contact" Problem:** This considers the scenario where AI capabilities far surpass human intelligence, posing unforeseen challenges in ensuring their safety. The analogy here is preparing for an unpredictable, unprecedented event like extraterrestrial first contact.

## 2.9.3 <span style="text - decoration: underline;">Why </span>d<span style="text - decoration: underline;">o Labs </span>e<span style="text - decoration: underline;">ngage in AGI </span>d<span style="text - decoration: underline;">evelopment </span>d<span style="text - decoration: underline;">espite the </span>r<span style="text - decoration: underline;">isks?</span>

This question is asked frequently. Here is a concise response.

- **Potential benefits:** Laboratories pursue AGI development despite the inherent risks due to the significant potential benefits. Successful AGI implementation could lead to unprecedented advancements in problem-solving capabilities, efficiency improvements, and innovation across various fields.

- **Competitive dynamics:** The commitment to AI development, even with recognized risks, is driven by competitive pressures within the field. There is a widespread belief that it is preferable for those who are thoughtful and cautious about these developments to lead the charge. Given the intense competition, there is a fear among entities that halting AGI research could result in being surpassed by others, potentially those with less regard for safety. See the box below: How do AI Companies proliferate?

- **Prestige and recognition:** Prestige is another significant motivator. Many AGI researchers aim for high citation counts, respect within the academic and technological communities, and financial success. Unfortunately, burning the timelines is high status.

- **Moreover, most AGI researchers believe in the feasibility of AGI safety.** There is a belief among some researchers that a large-scale, concerted effort—comparable to the Manhattan Project and similar to the “super alignment plan” by OpenAI—could lead to the development of a controllable AI capable of implementing comprehensive safety measures.

## 2.9.4 Notes

[^1]: