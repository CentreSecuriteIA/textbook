---
title: Home
---
# **The Handbook** of **AI Safety**

<h2 align="left">A comprehensive guide</h2>

![AI Safety](https://lh7-us.googleusercontent.com/XuuImYOYY7YElHDnooD6S7k1tf11JAV_a7LQZ6IUXbItUbPp0p7sAgDp1EjHJAuuHvZ_cJ-pj7rGq7SLxb0O4Xe9OkyRIEKh4R8TwoUwERq8TJxKRMQdixUPBjXXwVEjog_AqBgNiCwvE9QHEHlr_rk)

!!! info "About This Guide"
    *This document contains all the useful resources for the AISF (previously named AGISF). It will be updated regularly.*

    This textbook summarizes some key notions and papers in modern AI Safety, requiring minimal familiarity with the other materials covered. We tried to connect the various articles within a unified framework and coherent narrative.

    The alignment problem is a pre-paradigmatic problem, and there is no consensus on some of the concepts presented. So please read critically and feel free to add feedback on this [form](https://docs.google.com/forms/d/e/1FAIpQLSe-UI2pt99SHaH2RFPVbDdmo8nuiRBZcxl49rBh67Guj6_p5Q/viewform) on the various chapters if something seems unclear. Some weeks start with a gentle introduction, which you should follow if you are unfamiliar with the concepts.

    This textbook is an adaptation of the [course](https://www.master-mva.com/cours/seminaire-turing/) held at ENS Paris-Saclay in Paris during March 2023, and offered by [EffiSciences](https://ia.effisciences.org/) and was used and appreciated during the [ML4Good](https://www.lesswrong.com/posts/DkDy2hvkwbQ54GM9u/introducing-effisciences-ai-safety-unit-1) bootcamps in Paris and Germany.

---

!!! warning "Note"
    This textbook is still under construction.

## **Contact**

!!! info "Contact Information"
    This textbook was created by Charbel-Raphael Segerie, Markov, Jeanne Salle, and Vincent Corruble. We are actively looking for funding. Please consider upvoting us on [Manifund](https://manifund.org/projects/ai-safety-textbook) if you like our work.

    Contacts: [Charbel-Raphael Segerie](mailto:crsegerie@gmail.com), [agisf_textbook.0fh6l@slmail.me](mailto:agisf_textbook.0fh6l@slmail.me), [jeanne.salle@yahoo.fr](mailto:jeanne.salle@yahoo.fr)

## **Curriculum**

The textbook is currently written as a list of chapters. Some chapters contain a list of quizzes on key resources. Reading carefully each chapter of the textbook should take 1-2 hours.

### **PART 1 : FUNDAMENTALS**

We encourage all readers, including those without a technical background, to read through Chapters 1, 2, and 3. These chapters explain in an accessible way why it is plausible to see the emergence of human-level AI in the next few years, what are the potential risks associated with these advanced AIs, and what solutions can be put in place to mitigate these risks. These introductory chapters aim to provide a solid foundation for understanding the issues and challenges of AI Safety.

---

#### Week 0: **Artificial Intelligence**

The rest of this textbook assumes familiarity with Machine Learning (ML). Please take your time to understand the core concepts, *especially* Reinforcement Learning (RL). Here are some [resources](https://course.aisafetyfundamentals.com/alignment?week=0) if you are not familiar with ML yet.

??? abstract "Concepts covered"
    Basics of Machine Learning, Basics of Reinforcement Learning, Basics of the Transformer Architecture.

#### Week 1: **Human-Level AI, What, How and When?**

📖 [Chapter](Chapters/1-Capabilities/2-Overview.md)

??? abstract "Concepts covered"
    Current Capabilities, Foundation Models, Leveraging Computation, Future Capabilities, Timelines and Anchors, Instrumental Convergence.

#### Week 2: **AI Risks Landscape**

📖 [Chapter](Chapters/2-Risks/2-Introduction.md)

??? abstract "Concepts covered"
    Misuses, Alignment risks, Systemic risks.

#### Week 3: **Solutions Landscape**

📖 [Chapter](https://docs.google.com/document/d/1WTyLHyaJ_NEDEu49U_hh7oz0-AOQfp7uOJKLck-7A78/edit)

??? abstract "Concepts covered"
    API, defense acceleration, AI alignment main paradigms, safety culture, and organizational safety.

### **PART 2 : TECHNICAL PROBLEMS**

In this part, we dive into the specific technical challenges of AI alignment. We start with the problem of Reward Misspecification, which occurs when the reward function given to an AI agent fails to properly capture the intended goals. We explore key concepts such as optimization, Goodhart's Law, and different approaches to learning human preferences, such as learning by imitation and feedback.

Next, we address the problem of Goal Misgeneralization, where an AI agent may learn unintended goals that differ from those intended by its designers. We examine important concepts such as mesa-optimization, inner alignment, and deceptive alignment. This part aims to provide a deep understanding of the main technical challenges in AI alignment and sets the stage for exploring research paradigms in the next part.

---

#### Week 4: **Reward Misspecification**

👉 Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=nKJlF-olKmg).

📖 [Chapter](https://docs.google.com/document/d/1niRLuFX1FfsMrlMLJtbOm4m_yK8dTdXi3gKmkENp-ss/edit?usp=sharing)

??? abstract "Concepts covered"
    Reward, Reward Misspecification, Optimization, Goodhart's Law, Learning by imitation, Learning by Feedback.

#### Week 5: **Goal Misgeneralization**

👉 Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=bJLcIBixGj8).

📖 [Chapter](https://docs.google.com/document/d/1K52KgxyveZWw4p4rzMqw9mu6FvJC7ulSYxvaXQc5p10/edit?usp=sharing)

??? abstract "Concepts covered"
    Optimization, Mesa-optimization, Inner-Alignment, Deceptive Alignment.

### **PART 3 : RESEARCH PARADIGMS**

In this part, we explore the main research paradigms proposed to address the challenges of AI alignment. We start with task decomposition techniques for Scalable Oversight, such as iterated amplification and process supervision. Next, we examine adversarial techniques for Scalable Oversight, including debate and adversarial training. We dedicate an entire chapter to interpretability, covering both interpretability techniques for computer vision and transformers used in natural language processing. We also delve into Agent Foundations and examine more theoretical research paradigms. Finally, we also give an overview of AI Governance.

This part aims to give readers an overview of the main research approaches in the field of AI alignment and inspire them to contribute to this crucial domain.

---

#### Week 6: **Task Decomposition for Scalable Oversight**

👉 Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=v9M2Ho9I9Qo).

📖 [Chapter](https://docs.google.com/document/d/1k6rlyBCZJw8xbUx0dzd-4sOhlzj-xzsmwi_OIZY1-3M/edit)

??? abstract "Concepts covered"
    Scalable Oversight Problem, Sandwiching, Task decomposition, Factored cognition, Iterated Amplification, amplification in modern LLMs, Process Supervision.

#### Week 7: **Adversarial Techniques for Scalable Oversight**

👉 Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=wIX00bZ173k).

📖 [Chapter - Debate](https://docs.google.com/document/d/1KXEWXHKwgeu-0NX5iirGS1h5zsh1skYMadZN3ZoVMAI/edit?usp=sharing) & [Chapter - Adversarial training](https://docs.google.com/document/d/1bsHau2v9EPoVGXc9iRZvVUF-kjfLb3D0CKEKik_J4tQ/edit)

??? abstract "Concepts covered"
    Debate, obfuscated arguments problem, AI-written critiques, problems with debate.
    Unrestricted adversarial training, adversarial training, red-teaming language models, interpretability for finding adversarial examples, relaxed adversarial training.

#### Week 8: **Interpretability**

**Vision**

👉 Gentle introduction: [Youtube Video](https://www.youtube.com/watch?v=cqMe9E4p7fE).

📖 [Chapter](https://www.lesswrong.com/posts/XZfJvxZqfbLfN6pKh/introductory-textbook-to-vision-models-interpretability)

??? abstract "Concepts covered"
    Feature visualization, saliency techniques (Grad-CAM), activation atlas, circuits, early vision, RL vision, automatic interpretability (NetDissect), multimodal neurons.

**Transformers (Bonus, after vision)**

📖 [Chapter](https://drive.google.com/file/d/145_PXa5XE1iaq911NmO25Res_ALAGLlE/view?usp=sharing)

??? abstract "Concepts covered"
    Logit Lens, Rome, Probing, Induction heads, limits of interpretability.

#### Week 9: **Agent Foundations**

📖 [Chapter](https://docs.google.com/document/d/1z4CwGDUzHvPvfXNxyfDaIfh9kK1JBJWEcfdGUutfJY0/edit)

??? abstract "Concepts covered"
    Utility functions, agent AI, tool AI, True Name, Shard theory, CEV, CIRL.

#### Week 10: **Governance**

📖 WIP, for the moment, please follow [Bluedot Impact's](https://course.aisafetyfundamentals.com/alignment?session=6) course which is already great.

## Going Further

??? tip "Other Resources"
    - Detailed list of articles: [Alignment Course](https://course.aisafetyfundamentals.com/alignment).
    - The old long list of individual summaries: [AGISF 2023 Summaries](https://docs.google.com/document/d/1m94jGvbdhU4FJQr6v4knSg7MoaKgiO64Mr5P7I8kBPs/edit#).
    - For each week, there is a list of videos for each chapter: [Textbook: Videos](https://docs.google.com/document/d/19OeWv-_yhG0dUyrl6mfnHeHgZYVtyRdNt0kZQjtfSdc/edit).
    - List of bonus exercises: [Archived: 2022 Alignment Fundamentals Curriculum](https://docs.google.com/document/d/1mTm_sT2YQx3mRXQD6J2xD2QJG1c3kHyvX8kQc_IQ0ns/edit#heading=h.dlm795ug69gc).

    The field of alignment does not stop at just the concepts presented in the textbook. Many schools of thought are only briefly touched upon. To get an overview of the field, the best advice is to stay curious and try out various different viewpoints.

??? tip "How to Best Read This Book"
    One of the best ways to use this textbook is in a reading group consisting of students or young researchers who gather periodically. You don't need to have a large group; a friend is enough, which allows you to discuss the concepts presented in the different chapters critically. If you want to create a reading group to facilitate this course, please get in touch.
