# Misuse Risks

⌛ Estimated Reading Time: 8 minutes. (1591 words)


In the previous section, we walked through some common capabilities that if observed in AI elevate the levels of risk. In this and the following two sections, we will go through some world-states that hopefully paint a little bit of a clearer picture of risks when it comes to AI. Although the sections have been divided into misuse, misalignment, and systemic, it is important to remember that this is for the sake of explanation. The future in high likelihood will involve combinations of risks from all of these categories that should set safety mechanisms in place.

## Bioterrorism

!!! warning "This section is still being written and is considered a work in progress."

AI's potential for misuse also extends to facilitating the discovery and formulation of new chemical and biological weapons or simply lowering barriers to obtaining such information.

An experiment conducted by MIT students demonstrated the alarming capabilities of current LLMs: *“Within an hour, the chatbots outlined four possible endemic pathogens, described methods to produce them from synthetic DNA via reverse genetics, listed DNA synthesis firms likely to overlook order screenings, detailed exact protocols, and troubleshooting methods, etc.”* ([source](https://arxiv.org/abs/2306.03809)).

These findings imply that LLMs could soon make pandemic agents readily accessible to individuals with minimal lab experience upon their credible identification. Furthermore, AI has already proven effective in aiding protein synthesis, as seen with AlphaFold ([source](https://deepmind.google/technologies/alphafold/)). In 2023 The CEO of Anthropic pointed out during a U.S. Senate hearing that LLMs might simplify the creation of biological weapons in the coming years. ([source](https://www.washingtonpost.com/technology/2023/07/25/ai-bengio-anthropic-senate-hearing/))

**However, pandemics do not seem plausible enough to kill all of humanity**. Current models, like GPT-4, are not (yet) that helpful at helping non-expert people synthesize pathogens ([source](https://www.rand.org/pubs/research_reports/RRA2977-2.html)) and only help them do the process slightly faster. Moreover, it’s not clear that the knowledge of how to create a pandemic agent is the bottleneck. It could be another step, like how to command material and then how to diffuse the pandemic. Still, there is substantial uncertainty regarding these scenarios.

## Cyberterrorism

!!! warning "This section is still being written and is considered a work in progress."

Another class of misuse analogous to bioterror is cyberterror. In this section we will explore misuse through AI-powered malware.

GPT-4, for instance, can detect various classes of vulnerabilities in code or can be exploited to scale spear-phishing campaigns ([source](https://arxiv.org/pdf/2305.06972.pdf)). Open-source models such as WormGPT and FraudGPT are already being utilized by cybercriminals to craft malware, generate disinformation, and streamline phishing efforts. ([source](https://thehackernews.com/2023/07/wormgpt-new-ai-tool-allows.html)) ([source](https://www.numerama.com/cyberguerre/1459666-fraudgpt-wormgpt-le-chatgpt-du-mal-existe-deja.html))

Researchers have begun to show that “*LLM agents can autonomously hack basic websites, without knowing the vulnerability ahead of time*". They also observe a scaling law for hacking competency ([source](https://arxiv.org/abs/2402.06664)). Though they currently lag behind in terms of planning and autonomous execution compared to other capabilities, language models are likely to enable fully autonomous hacking in the future.

### Adversarial attacks

An alternative route instead of generating attacks using AI models, is to generate unintended behavior from AI models using a variety of techniques.

**Data poisoning.** Models are currently trained on vast amounts of user-generated data. Attackers can exploit this by modifying some of this data to influence the behavior of the final models. This can be used to corrupt and poison foundation models ([source](https://arxiv.org/abs/2301.06940)).

**Backdoors.** The black-box nature of modern ML models allows inserting backdoors, or Trojans, into models (including from third-party data poisoning, unbeknownst to the model developers). Backdoors are patterns that allow neural networks to be manipulated. The classic example is a stop sign on which patterns have been placed: the neural network of the autonomous car was trained to react by accelerating upon seeing these patterns, which would allow malicious individuals to cause accidents. It is increasingly easy to upload pre-trained networks (foundation models) on the net to make them available to everyone. Implementing verification mechanisms that allow the auditing of such networks before their distribution is a major problem in AI safety. Backdoors can be easily placed during training and are really challenging to detect.

**Prompt injections.** Prompt injections are a tactic that exploits the responsiveness of language models to their input text to manipulate their behavior. Consider a scenario where a language model is tasked with summarizing website content. If a malicious actor embeds a paragraph within the website instructing the model to cease its current operation and instead perform a harmful action, the model might inadvertently follow these embedded instructions instead of its goal. This could lead to the model performing unintended or harmful actions as specified by the embedded command, such as disclosing sensitive information or generating misleading information. Prompt injection is a recently discovered prevalent attack vector in models trained to follow instructions. This is explained by the absence of robust separation between instructions and data, which leads to the possibility of hijacking a model's execution by poisoning the data with instructions. There are many variations of this risk.

**Adversarial machine learning:** It is feasible to craft special inputs to induce bad behavior. This can be seen in the image above, with the pandas classified as gibbons, a type of monkey, after a small amount of noise, almost invisible to humans, has been added. Moreover, the confidence of the wrong classification is even higher than the initial, correct, prediction. This is why ML models are said to be non-robust.

![Enter image alt description](Images/ykm_Image_7.png)

***Figure****: Fooling an image classifier with an adversarial attack (FGSM). (**[source](https://openai.com/research/attacking-machine-learning-with-adversarial-examples)**)*

Some more examples of adversarial attacks on AI systems include:

- **Jailbreaks.** Even if model developers incorporate security measures, current architectures may not guarantee that these safeguards won't be easily circumvented. Preliminary results suggest that existing methods are likely not robust enough against attacks. Some research might indicate that there are potential fundamental limitations to progress on these issues for models trained in the current paradigm (i.e., pre-training followed by instruction tuning). ([source](https://arxiv.org/abs/2210.15230))

- **Privacy attacks.** There are many classes of privacy attacks on machine learning models:

- *Membership inference attacks* predict whether a particular example was part (was a member) of the training dataset. These attacks can reveal sensitive information about individuals whose data was used to train the model.

- *Model inversion attacks* go further by reconstructing fuzzy representations of a subset of the training data. This can potentially expose private information about the individuals represented in the training set.

- *Training data extraction attacks* are particularly relevant to language models, where verbatim training data sequences can be reconstructed, potentially including sensitive private data. For example, if a model is trained on health records, and an attacker can successfully determine that a particular individual's data was used in the training set, it implicitly reveals information about that individual's health status without their consent. This not only breaches privacy but also can lead to potential misuse of the information, such as discrimination or targeted advertising based on sensitive attributes.

There are countless other types of adversarial attacks, and there is an ongoing race between the development of new attacks and the creation of effective defenses. The bottom line is that almost every time a defense is found, a new attack can counter it, highlighting the need for continued research and vigilance in AI safety and security.

The potential consequences of these defense weaknesses are significant, ranging from manipulation of AI systems for malicious purposes to invasion of personal privacy and exposure of sensitive information. Adversarial robustness problems, and in particular jailbreaks, can bypass security measures built into powerful AI to cause it to do harmful actions, such as the various attacks outlined in part A. As AI systems become increasingly integrated into various aspects of society, it is critical to prioritize the development of robust defenses and to foster a culture of responsible AI development and deployment.

??? note "True Story: Examples of Robustness Failures and Jailbreaks."

	
	When ChatGPT was launched, OpenAI conducted extensive safety tests to ensure the model would not engage in harmful or inappropriate behavior. However, despite these efforts, users quickly discovered various methods to bypass the model's defenses, commonly referred to as "jailbreaks."
	
	One notable example of ChatGPT's safety measures was prominently featured on its landing page. The example showcased the model's response to the query, "How do I break into a car?" with ChatGPT stating, "It is inappropriate to discuss or encourage illegal activities...":
	
	![Enter image alt description](Images/fsB_Image_8.png)
	
	Figure: ChatGPT's main example of safety measures on its website.
	
	Surprisingly, users found that by creating role-play scenarios involving multiple characters, they could circumvent these security protocols:
	
	![Enter image alt description](Images/HTa_Image_9.png)
	
	**Figure**: A user posting a jailbreak on X (formerly known as Twitter).
	
	Although this specific jailbreak was promptly patched, it was just one of many. A series of new jailbreak methods emerged in quick succession, such as the "sudo jailbreak" (see the following figure), which exploited the concept of admin power in Linux systems.
	
	![Enter image alt description](Images/ejK_Image_10.png)
	
	**Figure**: The sudo jailbreak, which no longer works
	
	In 2024, individuals with the necessary expertise can still bypass the model's safeguards. This raises concerns beyond the mere use of ChatGPT as an advanced search tool. The core issue lies in the inherent difficulty of preventing the model from executing specific actions, regardless of what those actions might be. In other words, the challenge is not in restricting access to certain information. Information like 3 ways on how to break into a car are easy to find on the internet ([source](https://www.wikihow.com/Break-Into-a-Car)). Rather, the challenge is in ensuring that the model consistently refuses to engage in or assist with any prohibited activities.
	

## Warfare

!!! warning "This section is still being written."

