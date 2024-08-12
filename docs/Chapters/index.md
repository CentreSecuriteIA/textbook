# The AI Safety Handbook

## FUNDAMENTALS

We encourage all readers, including those without a technical background, to read through the fundamentals section of the textbook. This entails reading Chapters 1 through 5. These chapters explain in an accessible way why it is plausible to see the emergence of human-level AI, the potential risks associated, and what solutions are currently being explored to mitigate these risks. These introductory chapters aim to provide a solid foundation for understanding the issues and challenges of AI Safety.

| Chapter 1: Capabilities |
|-------------------------|
| **Overview:** Covers current capabilities, foundation models, leveraging computation, future capabilities, timelines and anchors, and instrumental convergence. |
| <div class="button-container"> [:fontawesome-solid-book: Read](1%20-%20Capabilities/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/10fO4qjxHX3OiNnafNlp5nvF-9nLW8TOt/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 2: Risks Landscape |
|----------------------------|
| **Overview:** Explores misuses, alignment risks, and systemic risks. |
| <div class="button-container"> [:fontawesome-solid-book: Read](2%20-%20Risks%20Landscape/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/1ymYnH9MfKFw6NnufsTY5BDCAmfVhIJG6/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 3: Solutions Landscape |
|--------------------------------|
| **Overview:** Covers defense acceleration, paradigms in AI Safety, safety culture, and organizational safety. |
| <div class="button-container"> [:fontawesome-solid-book: Read](3%20-%20Solutions%20Landscape/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/1XTWrspAMg8PBNKKiBLr_bEd7yJW5wB-5/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 4: Evaluations |
|------------------------|
| **Overview:** This chapter is still being written. |
| <div class="button-container"> [:fontawesome-solid-book: Read](4%20-%20Evaluations/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](){ .md-button .md-button--disabled } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 5: Governance |
|------------------------|
| **Overview:** This chapter is still being written. |
| <div class="button-container"> [:fontawesome-solid-book: Read](5%20-%20Governance/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](){ .md-button .md-button--disabled } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

## TECHNICAL SAFETY

In this part, we dive into the specific technical challenges of AI alignment. We start with the problem of Reward Misspecification, which occurs when the reward function given to an AI agent fails to properly capture the intended goals. We explore key concepts such as optimization, Goodhart's Law, and different approaches to learning human preferences, such as learning by imitation and feedback.

Next, we address the problem of Goal Misgeneralization, where an AI agent may learn unintended goals that differ from those intended by its designers. We examine important concepts such as mesa-optimization, inner alignment, and deceptive alignment. This part aims to provide a deep understanding of the main technical challenges in AI alignment and sets the stage for exploring research paradigms in the next part.

These chapters assume some basic familiarity with Machine Learning (ML). Please take your time to understand the core concepts, *especially* Reinforcement Learning (RL). Here are some [resources](https://course.aisafetyfundamentals.com/alignment?week=0) if you are not familiar with ML yet.

| Chapter 6: Reward Misspecification |
|-------------------------------------|
| **Overview:** Explores concepts of reward, reward misspecification, optimization, Goodhart's Law, learning by imitation, and learning by feedback. |
| <div class="button-container"> [:fontawesome-solid-book: Read](6%20-%20Reward%20Misspecification/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/1my3TSNPU-gzzv48MEN763EhIYL_UvG5v/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 7: Goal Misgeneralization |
|------------------------------------|
| **Overview:** Covers optimization, mesa-optimization, inner-alignment, and deceptive alignment. |
| <div class="button-container"> [:fontawesome-solid-book: Read](7%20-%20Goal%20Misgeneralization/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/1lHSTzwlDukble7n1dXO5zoKhAybXgRYo/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 8: Scalable Oversight |
|--------------------------------|
| **Overview:** Explores the scalable oversight problem, sandwiching, task decomposition, factored cognition, iterated amplification, process supervision, debate, and critiques. |
| <div class="button-container"> [:fontawesome-solid-book: Read](8%20-%20Scalable%20Oversight/README.md){ .md-button } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/17PVzvEMM7CiOaTIP_HH5h_YUrgV0iG1F/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 8.1: Adversarial Techniques |
|--------------------------------------|
| **Overview:** Covers unrestricted adversarial training, adversarial training, red-teaming language models, interpretability for finding adversarial examples, and relaxed adversarial training. |
| <div class="button-container"> [:fontawesome-solid-book: Read](https://www.lesswrong.com/s/3ni2P2GZzBvNebWYZ/p/nz5NNAtfKJLmbtksL){ .md-button } [:fontawesome-solid-file-pdf: Download](){ .md-button .md-button--disabled } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 9.1: Interpretability: Vision |
|---------------------------------------|
| **Overview:** Explores feature visualization, saliency techniques (Grad-CAM), activation atlas, circuits, early vision, RL vision, automatic interpretability (NetDissect), and multimodal neurons. |
| <div class="button-container"> [:fontawesome-solid-book: Read](https://www.lesswrong.com/posts/XZfJvxZqfbLfN6pKh/introductory-textbook-to-vision-models-interpretability){ .md-button } [:fontawesome-solid-file-pdf: Download](){ .md-button .md-button--disabled } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 9.2: Interpretability: NLP |
|-------------------------------------|
| **Overview:** Covers Logit Lens, ROME, Probing, Induction heads, and limits of interpretability. |
| <div class="button-container"> [:fontawesome-solid-book: Read](){ .md-button .md-button--disabled } [:fontawesome-solid-file-pdf: Download](https://drive.google.com/file/d/145_PXa5XE1iaq911NmO25Res_ALAGLlE/view?usp=sharing){ .md-button } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

| Chapter 10: Agent Foundations |
|--------------------------------|
| **Overview:** This chapter is still being written. It will cover utility functions, agent AI, tool AI, True Name, Shard theory, CEV, and CIRL. |
| <div class="button-container"> [:fontawesome-solid-book: Read](https://docs.google.com/document/d/1z4CwGDUzHvPvfXNxyfDaIfh9kK1JBJWEcfdGUutfJY0/edit){ .md-button } [:fontawesome-solid-file-pdf: Download](){ .md-button .md-button--disabled } [:fontawesome-solid-video: Video](){ .md-button .md-button--disabled } [:fontawesome-solid-users: Facilitate](){ .md-button .md-button--disabled } </div> |

The field of alignment does not stop at just the concepts presented in the textbook. Many schools of thought are only briefly touched upon. To get an overview of the field, the best advice is to stay curious and try out various different viewpoints.

## Going Further

!!! tip "Other Resources"
    - For each week, there is a list of videos for each chapter: [Textbook: Videos](https://docs.google.com/document/d/19OeWv-_yhG0dUyrl6mfnHeHgZYVtyRdNt0kZQjtfSdc/edit).
    - List of old exercises: [Archived: 2022 Alignment Fundamentals Curriculum](https://docs.google.com/document/d/1mTm_sT2YQx3mRXQD6J2xD2QJG1c3kHyvX8kQc_IQ0ns/edit#heading=h.dlm795ug69gc).

!!! tip "How to Best Read This Book"
    One of the best ways to use this textbook is in a reading group consisting of students or young researchers who gather periodically. You don't need to have a large group; a friend is enough, which allows you to discuss the concepts presented in the different chapters critically. If you want to create a reading group to facilitate this course, please get in touch.

