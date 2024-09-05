# The AI Safety Atlas

## FUNDAMENTALS

We encourage all readers, including those without a technical background, to read through the fundamentals section of the textbook. This entails reading Chapters 1 through 5. These chapters explain in an accessible way why it is plausible to see the emergence of human-level AI, the potential risks associated, and what solutions are currently being explored to mitigate these risks. These introductory chapters aim to provide a solid foundation for understanding the issues and challenges of AI Safety.

### Chapter 1: Capabilities

First in the series on fundamentals is a chapter on capabilities. Capabilities are specific, measurable abilities of artificial intelligence systems across various domains. These can be abilities on specific quantifiable tasks (e.g., performance on standardized benchmarks) or more complex, fuzzy abilities (e.g., persuasion or situational awareness).

Our first chapter examines the evolution of AI capabilities over recent decades, focusing on why today's leading AI models can perform such remarkable tasks. This chapter also clarifies essential terminology used throughout the book. We introduce concepts like the Bitter Lesson and the AI production function, which explain the factors driving AI performance improvements. We also explore potential bottlenecks in AI development, including limitations in data availability, algorithmic advancements, model size, and computational resources.

We explore various potential paths to Artificial General Intelligence (AGI). This includes approaches using Large Language Models (LLMs) and Reinforcement Learning (RL) agents.

The core objective of this chapter is to examine trends, key capability thresholds, and potential development trajectories, to lay a solid foundation for the subsequent chapters of this textbook. Only when we have a solid understanding based on trends, can we begin to discuss the risks, and then potential solutions in the following chapters.

[:fontawesome-solid-book: Read](01/README.md){ .md-button } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/10fO4qjxHX3OiNnafNlp5nvF-9nLW8TOt/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 2: Risks Landscape

The second chapter in the fundamentals series explores the landscape of AI safety risks. Building upon the potential paths to AGI outlined in the first chapter, we map out how these paths lead to corresponding paths to risk.

We decompose these risks into three main groups: Misuse, Misalignment, and Systemic risks. We explain misuse risks such as bioterrorism, cyberterrorism, and warfare. We introduce the concept of (mis)alignment, discussing why it's a particularly challenging problem, with brief overviews of issues like specification gaming and goal misgeneralization. We also discuss systemic risks, including those arising from accidents, persuasion, power concentration, and epistemic erosion. Additionally, we explore factors that may exacerbate all these risks, such as indifference, race dynamics, unpredictability, and large-scale deployment.

The goal of this chapter is to provide a concrete, comprehensive overview of AI-related risks and their underlying factors. This foundation is crucial for understanding the governance and technical solutions discussed in later chapters, as each of these solutions aims to address one or more of the risks introduced here.

[:fontawesome-solid-book: Read](02/README.md){ .md-button } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/1ymYnH9MfKFw6NnufsTY5BDCAmfVhIJG6/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 3: Solutions Landscape

The third chapter in the foundations series examines paths to various solutions for the risks identified in the previous chapters. Building on the first chapter's exploration of paths to AGI and the second chapter's examination of paths to risk from AGI, we now delve into strategies for mitigating these risks.

We explore risk mitigation strategies corresponding to the categories identified in the previous chapter. For misuse risks, we discuss approaches such as monitored APIs, defense acceleration, and addressing risks from current AI systems.

We explore solutions to AGI and ASI alignment separately. These cover exploring naive strategies, while also delving into sophisticated approaches like AI control, transparent thoughts, automating alignment research, and designing inherently safe systems.

To understand proposed solutions to broader systemic risks, we explore AI governance frameworks, organizational safety measures, and the cultivation of a robust safety culture within the AI development community.

Overall, this chapter serves as a stepping stone to future chapters, which will cover each solution mentioned here in greater individual depth. It provides a crucial link between understanding risks and implementing practical safety measures.

[:fontawesome-solid-book: Read](03/README.md){ .md-button } 
[:fontawesome-solid-download: Download](){ .md-button .md-button--disabled } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 4: Evaluations

This chapter is currently still being written.

It will explore the critical role of evaluations in AI safety, presenting a comprehensive taxonomy of evaluation types and methods. The chapter will cover:

- A detailed classification of evaluation types, including capability evaluations, propensity evaluations, and internal evaluations.
- The evaluation process, including methods of elicitation, generation techniques, and analysis approaches.
- Strategies for interpreting and using evaluation outputs effectively.
- Challenges and limitations of current evaluation methods, particularly for advanced AI systems.
- Introduction to meta-evaluations and understanding-based safety assessments.
- The dynamic nature of AI evaluation and the need for continuous refinement of methods.

This chapter will aim to provide readers with a comprehensive understanding of how to assess and ensure the safety of AI systems as they grow increasingly complex and capable.

[:fontawesome-solid-book: Read](04/README.md){ .md-button } 
[:fontawesome-solid-download: Download](){ .md-button .md-button--disabled } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 5: Governance

This chapter is currently still being written.

We chose this chapter to be the conclusion of the fundamentals section because it ties together capabilities, risks, and solutions. The conversation around AI governance gives every reader actionable steps regardless of technical background, allowing more voices to participate in ongoing debates to the development of safe AI.

We will explain the full landscape of AI governance across corporate, national, and international levels. The chapter will cover:

- Unique challenges posed by AI development and deployment, including rapid capability emergence and proliferation risks.
- Key governance functions and levers, with a focus on the role of compute as a critical resource.
- Critical issues complicating AI governance efforts, such as competition dynamics, uncertainty in predicting AI impacts, accountability challenges, and distributive consequences.
- Analysis of specific governance initiatives and policy options at corporate, national, and international levels.
- Exploration of adaptive governance approaches and novel mechanisms like algorithmic governance.
- Lessons from governance efforts in other fields and their potential application to AI.

[:fontawesome-solid-book: Read](05/README.md){ .md-button } 
[:fontawesome-solid-download: Download](){ .md-button .md-button--disabled } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

## TECHNICAL SAFETY

In this part, we dive into the specific technical challenges of AI alignment. We explore key concepts and methodologies crucial for ensuring the safe development and deployment of advanced AI systems. These chapters build upon the foundational knowledge established in the earlier sections, providing a deeper understanding of the technical intricacies involved in AI safety.

These chapters assume some basic familiarity with Machine Learning (ML). Please take your time to understand the core concepts, *especially* transformers in Natural Language Processing (NLP), and Reinforcement Learning (RL).

In structuring the chapters we tried to follow the paradigm of - present the problem in detail, and then present the solutions to the problem in detail. So each chapter begins with an exploration of what exactly the problem is, why this a problem, and then how exactly are researchers trying to solve this problem as well as potential limitations of the proposed solutions.

### Chapter 6: Reward Misspecification

The first chapter in the technical safety series addresses a fundamental challenge in AI alignment: the problem of reward misspecification. We explore how reward functions given to reinforcement learning agents can fail to capture intended goals, leading to unintended behaviors. The chapter covers key concepts such as reinforcement learning fundamentals, optimization pitfalls including Goodhart's Law, and various reward-related challenges. We then examine alternative approaches like imitation learning and inverse reinforcement learning. Finally, we discuss advanced techniques such as Reinforcement Learning from Human Feedback (RLHF) and its extensions, including their limitations and potential solutions like Direct Preference Optimization (DPO).

[:fontawesome-solid-book: Read](06/README.md){ .md-button } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/1my3TSNPU-gzzv48MEN763EhIYL_UvG5v/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 7: Goal Misgeneralization

The second chapter in the technical safety series, addresses Goal Misgeneralization. This is the problem of AI systems pursuing targets that differ from those intended by the developers. We explore why exactly cross distribution generalization is a difficult problem and covers concepts such as mesa-optimization, inner alignment, and deceptive alignment.

[:fontawesome-solid-book: Read](07/README.md){ .md-button } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/1lHSTzwlDukble7n1dXO5zoKhAybXgRYo/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 8: Scalable Oversight

This chapter follows up from the chapter on specification gaming. It introduces the problem of providing effective supervision even when the outputs of AI become too complex for human evaluators. We explore approaches such as task decomposition, process-based oversight, and debate.

[:fontawesome-solid-book: Read](08/README.md){ .md-button } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/17PVzvEMM7CiOaTIP_HH5h_YUrgV0iG1F/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 9.1: Interpretability: Vision

This chapter is currently still being written.

This chapter focuses on interpretability techniques for vision models. We cover various methods including feature visualization, attribution techniques, and automatic interpretability.

[:fontawesome-solid-book: Read](https://www.lesswrong.com/posts/XZfJvxZqfbLfN6pKh/introductory-textbook-to-vision-models-interpretability){ .md-button } 
[:fontawesome-solid-download: Download](){ .md-button .md-button--disabled } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 9.2: Interpretability: NLP

This chapter is currently still being written.

Complementing the previous chapter on vision interpretability, this section focuses on transformer mechanistic interpretability. We explore techniques to understand the inner workings of language models, including methods like the Logit Lens, knowledge editing, and concept erasure.

[:fontawesome-solid-book: Read](){ .md-button .md-button--disabled } 
[:fontawesome-solid-download: Download](https://drive.google.com/file/d/145_PXa5XE1iaq911NmO25Res_ALAGLlE/view?usp=sharing){ .md-button } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

### Chapter 10: Agent Foundations

This chapter is currently still being written.

The final chapter covers fundamental theoretical concepts in AI agent design, tying together many of the ideas explored in previous chapters. We examine key topics such as utility functions, decision theory, the distinction between agent AI and tool AI, natural abstractions, selection theorems, and various theories of value learning.

[:fontawesome-solid-book: Read](https://docs.google.com/document/d/1z4CwGDUzHvPvfXNxyfDaIfh9kK1JBJWEcfdGUutfJY0/edit){ .md-button } 
[:fontawesome-solid-download: Download](){ .md-button .md-button--disabled } 
[:fontawesome-solid-headphones: Listen](){ .md-button .md-button--disabled } 
[:fontawesome-solid-video: Watch](){ .md-button .md-button--disabled } 
[:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled }

The field of alignment does not stop at just the concepts presented in the textbook. Many schools of thought are only briefly touched upon. To get an overview of the field, the best advice is to stay curious and try out various different viewpoints.

!!! tip "How to Best Read This Book"
    One of the best ways to use this textbook is in a reading group consisting of students or young researchers who gather periodically. You don't need to have a large group; a friend is enough, which allows you to discuss the concepts presented in the different chapters critically. If you want to create a reading group to facilitate this course, please get in touch.

This book is a project from CeSIA.

<img src="Images/CeSIA.png" alt="CeSIA - Centre pour la Sécurité de l'IA" style="width: 35%;" />
