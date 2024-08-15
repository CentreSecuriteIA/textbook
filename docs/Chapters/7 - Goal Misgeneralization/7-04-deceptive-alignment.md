# 7.4 Deceptive alignment

⌛ Estimated Reading Time: 14 minutes. (2763 words)

!!! warning "This section is still being written and is considered a work in progress."

???+ note "Deceptive Alignment - Video Introduction"

    
    
    <iframe width="1280" height="720" src="https://www.youtube.com/embed/IeWljQw3UgQ" title="Deceptive Misaligned Mesa-Optimisers? It&#39;s More Likely Than You Think..." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    
    !!! warning "This video is optional and not necessary to understand the text."
    
    

This section focuses on further exploring the concept of mesa-optimizers. There are various different types of mesa-optimizers that can result at the end of the training process. Ajeya Cotra in her post “[Why AI alignment could be hard with modern deep learning](https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/)” provided an intuitive example by exploring three archetypes that an AI might embody. She explains this through the analogy of a young child (humanity) who has inherited a company to run and has a choice of the following three types of candidates (AIs) to hire to run the inherited company:

1. **Saints** are those who genuinely just want to help manage your estate well and look out for your long-term interests.

2. **Sycophants** want to do whatever it takes to make you short-term happy or satisfy the letter of your instructions regardless of long-term consequences. They want to see the child be happy even if it means lying. Sycophants would provide false facts about the world to convince the child that things are going well, but they don't have some long-term ulterior motives. Sycophants are an example of deception/dishonesty but they are not deceptively aligned.

3. **Schemers** have their own agendas and want to get access to the company and all its wealth and power so they can use it however they want. These are examples of deceptive alignment. Schemers have some ulterior motive (mesa-objective) that they want to accomplish.

During training, Sycophants and Schemers are behaviorally indistinguishable from Saints. Once a schemer is deployed or is otherwise safe from modification, it can "defect" and begin to pursue its true objective. Risks from learned optimization uses a slightly different vocabulary to convey the same concept. Following are the behaviorally indistinguishable types of mesa-optimizers that might be seen at the end of the training process:

**Internally aligned mesa-optimizer**: These AIs want exactly the same things as humans, because they have the same values and exactly the same way of thinking about the world. 

!!! info "Definition: Internally aligned mesa-optimizer"

    
    
    *An internally aligned mesa-optimizer is a robustly aligned mesa-optimizer that has internalized the base objective in its mesa-objective.*
    
    - Hubinger et. al. (Jun 2019) “[Risks from Learned Optimization (Glossary)](https://intelligence.org/learned-optimization/)”
    
    

**Corrigibly** **aligned mesa-optimizer**: These AIs don’t have an exact copy of human values, but they do have instead a desire to really understand human values. They then take action based on this understanding.

!!! info "Definition: Corrigibly aligned mesa-optimizer"

    
    
    *A corrigibly aligned mesa-optimizer is a robustly aligned mesa-optimizer that has a mesa-objective that “points to” its epistemic model of the base objective.*
    
    - Hubinger et. al. (Jun 2019) “[Risks from Learned Optimization (Glossary)](https://intelligence.org/learned-optimization/)”
    
    

**Deceptively ****aligned**** mesa-optimizer**: These AIs have their own desires independent of human values. But they also don't want to be shut off, or their values get trained away. So they act aligned until such fears are not relevant.

!!! info "Definition: Deceptively aligned mesa-optimizer"

    
    
    *A deceptively aligned mesa-optimizer is a pseudoaligned mesa-optimizer that has enough information about the base objective to seem more fit from the perspective of the base optimizer than it actually is.*
    
    - Hubinger et. al. (Jun 2019) “[Risks from Learned Optimization (Glossary)](https://intelligence.org/learned-optimization/)”
    
    

To understand deceptive alignment slightly more formally, imagine that an RL agent is trying to optimize for mesa-objective/reward (R) instead of the base objective (R*). Assume that this agent eventually develops some understanding of the training process. During training, the myopic strategy would be to just greedily choose the maximizing action for R immediately. However, since the model has an understanding of gradient descent it ‘knows’ that its parameters will get changed to focus on some other reward function (R*). Therefore the optimal course is to choose the action that instead maximizes R* to avoid parameter updates. As long as R* is being maximized during training, there is no reason to update or look for a ‘truly internally aligned model’. After training concludes, the agent is free to choose actions that maximize R as many times as it likes without the risk of being modified, resulting in an overall greater reward. Such type of behavior, where a deceptively aligned mesa-optimizer might purposefully act in ways that cause gradient descent to update (or not) it in some specific way is called gradient hacking.

!!! info "Definition: Gradient Hacking"

    
    
    *"Gradient hacking" describes the phenomenon wherein a deceptively aligned mesa-optimizer might be able to purposefully act in ways which cause gradient descent to update it in a particular way. - *Evan Hubinger (2019)* “*[Gradient hacking](https://www.alignmentforum.org/posts/uXH4r6MmKPedk8rMA/gradient-hacking)*”*
    
    

## 7.4.1 Prerequisites

Risks From Learned Optimization lists three prerequisites for an AI to become deceptively aligned. These conditions must be fulfilled during the training phase for an AI to develop internal goals, as well as the ability and desire to deceive the training process:



*Situational awareness*

The model must have a good enough understanding of the world to understand what humans “really want” and how it is different from what the AI wants (i.e. an understanding of the base objective). This is because in order to be successfully deceptive, the model still has to give the humans what they want during training. Additionally, it needs an understanding of the fact that it is part of a training process and some understanding of the technical details of how stochastic gradient descent (SGD) works. As an example, an agent tasked with forecasting stock performance in the tech sector might be given data about the entire world, including current AI technology in order to improve its performance. This information might also allow it to learn about its own situation. There is a lot of ongoing research and formalizing and detecting situational awareness in models.

***Long-term planning***

A model might be explicitly encouraged during training to acquire long-term planning capabilities to optimize its base objective. This might be, for example, because it was trained to take action in an environment where actions can have permanent consequences, or because of reasoning abilities. The possibility of permanently altering its environment means that the model has to consider the implications of its actions across longer time periods and training update cycles. Once it gains significant capabilities in long-term planning, it can use this ability to optimize for its own mesa-objective.

How could a model tell if it is training or deployment? RSA-2048

***Expectation of distribution shift***

The model must expect that at some point in the future, the threat of objective modification will go away. This means that the model thinks that training either has to end at some point, or that the trainer (SGD) does not need to update the behavior of the model because it is already performing well enough on the given task.

There are some dynamics of the gradient descent training process that might make the emergence of prerequisites like situational awareness and long term planning more or less likely. The next couple of sections explain machine learning training dynamics like inductive biases and path dependence. The subsequent section then uses this understanding to make an argument for the likelihood of deceptive alignment.

## 7.4.2 Inductive Priors

Inductive biases represent the constraints and influence how and what ML models learn. An inductive prior represents the initial state before any evidence has been observed. Here are some examples:

- **Complexity Bias**: It might be the case that the ML process prefers simpler models over more complex ones. The intuition behind this is Occam's razor, which suggests that the simplest explanation (or in this case, model) is often the “correct” one.

- **Smoothness Bias**: It could also be possible that smoother target functions are easier to find in search space than those that are erratic. In other words, small changes in the input should not produce large changes in the output.

- **Speed Bias**: Similarly, it could be the case that functions that can be computed quickly are more desirable.

There are many more inductive biases that the current machine learning process might have. The above are only a couple of examples. So depending on the inductive bias, gradient descent might just always simply find either the simplest, fastest, or smoothest model that fits the data. Which means that given the same dataset, all paths converge on essentially the same generalization.

Both inductive biases and path dependence can significantly influence the learning process and the final outcome of a machine learning model. A model's inductive priors can set it on a certain 'path', and then path dependence can further shape how the model learns and adapts as it travels down that path.

## 7.4.3 Path Dependence

*Path dependence refers to the update path that gradient descent follows through parameter space.*

Path dependence studies the effects of changes in the training procedure on the path that gradient descent follows while searching for the optimal learned algorithm. This includes things like the sequence of training data, the order of training, etc…

**High path dependence** means that significantly different learned models emerge at the end of the training process. **Low path dependence** means that similar learned models emerge across multiple training runs with the same model on the same data. 

This means that not only the emergence of mesa-optimizers but also overall levels of alignment could be sensitive to changes in the training procedure, which could make it harder to implement and enforce exact training procedures across different labs.

*High path dependence*

If gradient descent is highly path-dependent, then that would mean that different training runs can converge to very different models. This essentially means that the learned algorithm is very sensitive to the particular parameter update path that is taken through model space. To understand the types of expected learned algorithms, the path itself must also be understood.

There is some empirical evidence to suggest that many ML models might have high path dependence. The paper “[BERTs of a feather do not generalize together](https://arxiv.org/abs/1911.02969)” showed that different versions of the fine-tuned BERT models resulted in differing generalizations on downstream tasks, even with the same training data. This sort of path dependence is especially prevalent in reinforcement learning (RL) models, where an identical setup can be run multiple times, sometimes getting good performance and sometimes terrible performance.

*Low path dependence*

In this type of process, similar training processes converge to essentially the same simple solution, regardless of early training dynamics. In this case, inductive priors play a much larger role in what type of algorithm you might end up with.

Ajeya Cotra provided a simple example of low path dependence in her post “[Why AI alignment could be hard with modern deep learning](https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/)”. The AI model was trained to be a shape detector. She defined a “thneeb” as one of the two shapes shown in the image below. Multiple models are trained to distinguish between two distinct types of shapes.

![Enter image alt description](Images/srO_Image_10.png)

**Figure**: Thneeb

![Enter image alt description](Images/09X_Image_11.png)

**Figure**: Thneebs with colors changed

Source: Cotra, Ajeya (Sep 2021) [Why AI alignment could be hard with modern deep learning](https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/)

However, in addition to the shapes in each cluster being similar, one shape was always blue, and the other was always red. During training, the model performed well at recognizing the shapes. During testing, the colors were swapped and it turned out that the model was only looking at the colors and not considering the shapes. On running the training process multiple times with random initialization points, it might be expected that at least one of the times the ML model generalizes to look for shapes instead of looking for colors. However, the paper “[ImageNet-trained CNNs are biased towards texture](https://arxiv.org/abs/1811.12231)” found that neural networks (or gradient descent) are consistently biased towards colors over shapes when given the choice.

Overall, there is no consensus on whether advanced machine learning models have high or low path dependence since there is evidence for both. The next section explores the likelihood of deceptively aligned mesa-optimizers emerging in both low and high-path dependent training scenarios.

## 7.4.4 Deception =/= Deceptive Alignment

!!! warning "This section is still being written and is considered a work in progress."

[https://www.lesswrong.com/posts/a392MCzsGXAZP5KaS/deceptive-ai-deceptively-aligned-ai](https://www.lesswrong.com/posts/a392MCzsGXAZP5KaS/deceptive-ai-deceptively-aligned-ai)

## 7.4.5 Likelihood

Since the objective is to analyze the emergence of deceptive alignment, this section assumes the emergence of a mesa-optimizer during training. The focus is more on “which type” of mesa-optimizer (aligned, corrigible, or deceptive) is most likely to be found using current ML training methods.

A couple of further assumptions: First, there is a relatively complex base objective such as human values. Second, training environments are diverse enough with enough situations to get the models to robustly understand what humans want.

During training, ML models always start with a seemingly random proxy objective. To improve performance Gradient descent can do two things:

- **Better Proxies**: The model can improve its understanding of the objective

- **Better World Models**: The model can improve its ability to act on its existing understanding of the objective

*High Path Dependence Scenario*

If gradient descent is highly path-dependent, then depending on the path followed either the world model or the proxy could be perfected first. Which indicates that there could be the following different types of scenarios:

1. If the proxy objective is perfected to match the base objective before the world model is perfected, then the model is internally aligned.

2. If the world model is perfected before the proxy objective, then the world model is also perfect enough to simulate gradient descent. Since the world model is perfect the base objective also exists within the world model. In which case, one of two things can happen:

1. The mesa-optimizer ‘throws out’ the proxy objective and replaces it with a pointer to gradient descent’s base objective.

2. **T**he mesa-optimizer just makes the current proxy objective a long-term goal (crystallizes it), which means that the mesa-optimizer is now free to maximize the base objective.

In all three of these cases, at the end of training gradient descent returns a model that optimizes the base objective. All three are functionally indistinguishable.

*Low Path Dependence Scenarios*

If training has low path dependence then the inductive priors come into play.

The simplicity inductive bias is an analysis of the algorithm's Kolmogorov complexity. In all three - internally, corrigibly, and deceptively aligned types of models the world model is exactly the same. The main difference between the models is the mesa objective, i.e. the complexity of the objective given to the model to learn and optimize. The simplest internally aligned mesa-objective is the base objective. So for internal alignment, the complexity class is the full complexity of the base objective. The simplest corrigibly aligned mesa-objective is a specification for how to point to the base objective. The simplest deceptively aligned mesa-objective is literally any long-term objective. So as far as deceptively aligned AI is concerned, the most complexity cost paid is just the simplest long-term objective that gradient descent can find. In other words, the deceptively aligned one has the lowest complexity cost out of the three alignment scenarios, assuming a relatively complex training objective. All of the other model classes scale with the complexity of the training objective, whereas the complexity of the deceptively aligned model is essentially fixed. Therefore the more complex the base objective (e.g. human values) the more deceptive alignment wins in the complexity race. Overall, the analysis results in the conclusion that the number of internally aligned AIs is less than the number of corrigibly aligned AIs which is less than the number of deceptively aligned AIs:

(internally aligned AIs) < #(corrigibly aligned AIs) < #(deceptively aligned AIs)
Random sampling from a distribution of learned optimizers means there are more ways to get a deceptively aligned AI than the other two.

The speed inductive bias thankfully falls in favor of corrigibly and internally aligned models. The deceptively aligned model has to perform extra steps of ‘thinking’. For example, it has to realize that caring about the mesa-objective in the long term means that it should optimize the training objective temporarily to get a higher reward on your internal objective eventually. The internal and corrigibly aligned models however don’t have to do this extra thinking and can just directly optimize what they care for which is the base objective. So in terms of time taken for each model class to output the correct answer:

t(internally aligned) ~= t(corrigibly aligned) < t(deceptively aligned)