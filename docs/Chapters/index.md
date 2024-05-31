
# The AI Safety Handbook

### **PART 1 : SAFETY FUNDAMENTALS**

We encourage all readers, including those without a technical background, to read through the fundamentals section of the textbook. This entails reading Chapters 1 through 5. These chapters explain in an accessible way why it is plausible to see the emergence of human-level AI, the potential risks associated, and what solutions are currently being explored to mitigate these risks. These introductory chapters aim to provide a solid foundation for understanding the issues and challenges of AI Safety.

---

#### [Chapter 1: **Capabilities**](01 - Capabilities/README.md/)

Concepts covered: Current Capabilities, Foundation Models, Leveraging Computation, Future Capabilities, Timelines and Anchors, Instrumental Convergence.

#### [Chapter 2: **Risks Landscape**](02 - Risks/README.md/)

Concepts covered: Misuses, Alignment risks, Systemic risks.

#### [Chapter 3: **Solutions Landscape**](03 - Solutions/README.md/)

Defense acceleration, Paradigms in AI Safety, Safety culture, Organizational safety.

#### [Chapter 4: **Evaluations**](04 - Evaluations/README.md/)

!!! warning "This chapter is still being written, it will be uploaded soon."

#### [Chapter 5: **Governance**](05 - Governance/README.md/)

!!! warning "This chapter is still being written, it will be uploaded soon."

---

### **TECHNICAL SAFETY**


In this part, we dive into the specific technical challenges of AI alignment. We start with the problem of Reward Misspecification, which occurs when the reward function given to an AI agent fails to properly capture the intended goals. We explore key concepts such as optimization, Goodhart's Law, and different approaches to learning human preferences, such as learning by imitation and feedback.

Next, we address the problem of Goal Misgeneralization, where an AI agent may learn unintended goals that differ from those intended by its designers. We examine important concepts such as mesa-optimization, inner alignment, and deceptive alignment. This part aims to provide a deep understanding of the main technical challenges in AI alignment and sets the stage for exploring research paradigms in the next part.

These chapters assume some basic familiarity with Machine Learning (ML). Please take your time to understand the core concepts, *especially* Reinforcement Learning (RL). Here are some [resources](https://course.aisafetyfundamentals.com/alignment?week=0) if you are not familiar with ML yet.

---

#### [Chapter 6: **Reward Misspecification**](06 - Reward Misspecification/README.md)

Reward, Reward Misspecification, Optimization, Goodhart's Law, Learning by imitation, Learning by Feedback.


Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=nKJlF-olKmg)

#### [Chapter 7: **Goal Misgeneralization**](07 - Goal Misgeneralization/README.md)

Concepts covered: Optimization, Mesa-optimization, Inner-Alignment, Deceptive Alignment.

Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=bJLcIBixGj8)

#### [Chapter 8.1: **Task Decomposition**](https://www.lesswrong.com/s/3ni2P2GZzBvNebWYZ/p/FFz6H35Gy6BArHxkc)

Scalable Oversight Problem, Sandwiching, Task decomposition, Factored cognition, Iterated Amplification, amplification in modern LLMs, Process Supervision.

Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=v9M2Ho9I9Qo)

#### [Chapter 8.2: **Debate**](https://www.lesswrong.com/s/3ni2P2GZzBvNebWYZ/p/WP4fciGn3rNtmq3tY)

Debate, obfuscated arguments problem, AI-written critiques, problems with debate.

#### [Chapter 8.3: **Adversarial Techniques**](https://www.lesswrong.com/s/3ni2P2GZzBvNebWYZ/p/nz5NNAtfKJLmbtksL)

Unrestricted adversarial training, adversarial training, red-teaming language models, interpretability for finding adversarial examples, relaxed adversarial training.

Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=wIX00bZ173k)

#### [Chapter 9.1: **Interpretability: Vision**](https://www.lesswrong.com/posts/XZfJvxZqfbLfN6pKh/introductory-textbook-to-vision-models-interpretability)

Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=cqMe9E4p7fE).

Feature visualization, saliency techniques (Grad-CAM), activation atlas, circuits, early vision, RL vision, automatic interpretability (NetDissect), multimodal neurons.

#### [Chapter 9.2: **Interpretability: NLP**](https://drive.google.com/file/d/145_PXa5XE1iaq911NmO25Res_ALAGLlE/view?usp=sharing)

Logit Lens, ROME, Probing, Induction heads, limits of interpretability.

#### [Chapter 10: **Agent Foundations**](https://docs.google.com/document/d/1z4CwGDUzHvPvfXNxyfDaIfh9kK1JBJWEcfdGUutfJY0/edit)

!!! warning "This chapter is still being written, the link is a very early draft."

Utility functions, agent AI, tool AI, True Name, Shard theory, CEV, CIRL.


The field of alignment does not stop at just the concepts presented in the textbook. Many schools of thought are only briefly touched upon. To get an overview of the field, the best advice is to stay curious and try out various different viewpoints.

## Going Further

!!! tip "Other Resources"
    - For each week, there is a list of videos for each chapter: [Textbook: Videos](https://docs.google.com/document/d/19OeWv-_yhG0dUyrl6mfnHeHgZYVtyRdNt0kZQjtfSdc/edit).
    - List of old exercises: [Archived: 2022 Alignment Fundamentals Curriculum](https://docs.google.com/document/d/1mTm_sT2YQx3mRXQD6J2xD2QJG1c3kHyvX8kQc_IQ0ns/edit#heading=h.dlm795ug69gc).

!!! tip "How to Best Read This Book"
    One of the best ways to use this textbook is in a reading group consisting of students or young researchers who gather periodically. You don't need to have a large group; a friend is enough, which allows you to discuss the concepts presented in the different chapters critically. If you want to create a reading group to facilitate this course, please get in touch.

