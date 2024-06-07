# Foundation Models

⌛ Estimated Reading Time: 10 minutes. (1840 words)


???+ note "Foundation Models - Video Introduction"

    <iframe style=" width: 100%; aspect-ratio: 16 / 9;" frameborder="0" allowfullscreen src="https://www.youtube.com/embed/kK3NmQT241w"></iframe>

    !!! warning "This video is optional and not necessary to understand the text."

Foundation models emerged in the mid-to-late 2010s, symbolizing a move away from the labor-intensive, one-model-per-task approach. These models are trained on vast, diverse datasets to learn broad patterns and skills, ready to be adapted to a multitude of tasks. Imagine them as the Swiss Army knives of the AI that can tackle everything from language translation to generating artwork. This marked a shift in strategy, to leveraging large, unlabeled datasets creating generalist models that can later be fine-tuned for specific needs.

**Economics of Foundation Models.** The shift towards foundation models was fueled by several factors: the explosion of data, advances in computational power, and refinements in machine learning techniques. These models are also extremely resource-intensive. Their development, training, and deployment often requires significant investment. This capital requirement comes from three main areas:

- **Data Acquisition**. The large-scale datasets they're trained on, often sourced from the internet. Collecting, cleaning, and updating these datasets can be expensive, especially for specialized or proprietary data.

- **Computational Resources**. The sheer size of foundation models and the datasets used in their training demands significant computational resources, not just in terms of hardware but also the electricity needed for operation.

- **Research and Development**. Beyond the immediate costs of data and computation, there's the ongoing investment in research required to develop new techniques, and fine-tune the existing models. This requires both financial resources and specialized expertise.

The next section provides a deeper dive into the machinery that powers these models.

## Techniques

**Pre-training.** This is the initial training phase on a large dataset comprising millions, if not billions, of examples. Here the models learn general patterns, structures, and knowledge.

**Self-Supervised Learning (SSL).** This is how we actually implement the pre-training. Unlike traditional supervised learning (SL) that relies heavily on labeled data, Self-Supervised Learning (SSL) leverages unlabeled data, enabling models to learn from the inherent structure of the data itself. The development of this technique was a crucial step because it allowed developers to not be restricted by human provided labels. Now, we can leverage nearly unlimited (unlabeled) data available on the web.

As an example of how this technique would work - suppose you have an image of a dog in a park. Instead of a human labeling the image, and then training the model to learn what the human would say, the task for the model is to predict a portion of the image given the rest of it. For instance, the model might be given the top half of the image, and its task would be to predict what the bottom half looks like.

This is repeated on a large number of such images, learning to recognize patterns and structures in this data. Through these examples, the model might learn for instance that images with trees and grass at the top often have more grass, or perhaps a path, at the bottom. It learns about objects and their context — trees and grass often appear in parks, dogs are often found in these environments, paths are usually horizontal, and so on. These learned representations can then be used for a wide variety of tasks that the model was not explicitly trained for, such as identifying dogs in images, or recognizing parks - all without any human-provided labels!

**Zero & Few-Shot Learning.** These are techniques in machine learning where models learn to perform tasks with very few examples. Zero-shot is when they perform well without any specific examples. This is yet another example of a technique which is useful when collecting extensive labeled data is impractical or too costly. Think about introducing a human to the concept of a cat for the first time with just a few images. Despite only seeing three examples, they learn to identify cats in a variety of contexts, not limited to the initial examples. Similarly, few-shot learning enables AI models to generalize from a minimal set of instances, identifying new examples in broader categories they've scarcely encountered.

**Transfer Learning. **Transfer learning is the next step that follows the pre-training. It's where the model takes the general patterns, structures, and knowledge it has learned from the pre-training phase and applies them to new, related tasks. This technique hinges on the fact that knowledge acquired in one context can actually be "transferred" to enhance learning in another. It allows for the utilization of pre-existing knowledge, thereby sidestepping the need to start from scratch for every new task.

**Fine-Tuning.** The fine-tuning phase is where the model is specifically adapted to perform particular tasks. Fine-tuning enables the creation of versatile models capable of undertaking a wide range of tasks, from following instructions to doing programming or scientific analysis. This can be further enhanced later through methods like "Reinforcement Learning from Human Feedback" (RLHF), which refines models to be more effective and user-friendly by reinforcing desirable outputs. We will talk about this technique in detail in later chapters.

![https://www.artificialintelligence.news/pathal/uploads/2021/09/2021-foundationmodel-1024x692.png](Images/uxE-.png)

***Figure****:** Bommasani Rishi et. al. (2022) "**[On the Opportunities and Risks of Foundation Models](https://arxiv.org/pdf/2108.07258.pdf)**"*

**Elicitation Techniques**. Prompting is how we interact with the models. It's akin to giving the model a nudge in the right direction, ensuring that the vast knowledge it has acquired is applied in a way that's relevant and useful. So the structure of the prompt can have a large effect on the overall performance you are able to elicit out of the system. We only briefly introduce the concept here. There are a variety of elicitation techniques like chain-of-thought (CoT) that will be discussed in later chapters.

Prompting serves as a critical interface between human users and the sophisticated capabilities of foundation models. It's akin to giving the model a nudge in the right direction, ensuring that the vast knowledge it has acquired is applied in a way that's relevant and useful. The development of prompting techniques also reflects a broader shift in AI towards more interactive, user-friendly models like ChatGPT. We only briefly introduce the concept here, a broad variety of elicitation and prompting techniques will be discussed in later chapters.

The learning journey of a student—beginning with acquiring broad knowledge, honing specific skills, engaging in self-directed exploration, and seeking expert guidance—mirrors the trajectory of foundation model development. From the foundational broad learning in pre-training through specialization via fine-tuning to the targeted application through prompting, this progression encapsulates the evolving interaction between AI models and the complex, multifaceted tasks they are now capable of addressing.

## Properties

![Enter image alt description](Images/Wif_Image_14.png)

***Figure****: Bommasani Rishi et. al. (2022) "**[On the Opportunities and Risks of Foundation Models](https://arxiv.org/pdf/2108.07258.pdf)**"*

**Efficient use of resources**. Foundation models have the capacity to elevate their performance by leveraging additional data, more powerful computing resources, or advancements in model architecture. It's not merely a technique, but a pivotal attribute that dictates how well a model can adapt and expand its capabilities. As foundation models scale, they don't just grow; they become more nuanced, capable, and efficient in processing information, mirroring the enrichment of understanding and knowledge transfer. This makes scalability a crucial determinant in the operational efficacy of these models. We will discuss this capability further in the subsequent section on leveraging computation.

**Generalization**. This is the cornerstone of foundation models' effectiveness, enabling these AI systems to perform accurately on data they haven't previously encountered. This trait ensures the models remain versatile and reliable across various applications, making them indispensable tools in the AI toolkit. However, even though foundation models are displaying increasingly better generalization of capabilities, more research is needed to ensure the generalization of goals as well. The issue of capability generalization without goal generalization is something we will tackle in depth in subsequent chapters.

**Multi-modality**. This is a newer property that is still emerging as of 2024, but is expected to become extremely relevant as the years progress. This opinion was reflected by Sam Altman, CEO of OpenAI in a conversation with Bill Gates, where he mentioned "*Multimodality will definitely be important. Speech in, speech out, images, eventually video. Clearly, people really want that. Customizability and personalization will also be very important.*" ([source](https://www.linkedin.com/pulse/altman-multimodality-important-david-cronshaw-5fz0c))

We slightly touched on these capabilities in the section on state-of-the-art AI. This characterizes the capability of foundation models to process, interpret, and generate insights from various types of data, or "modalities," such as text, images, audio, and video. The power of multimodality in foundation models lies in its potential to create richer, more nuanced representations of information. By leveraging multiple forms of data, these models can establish deeper connections and uncover insights that might be missed when data types are considered in isolation. This can be considered similar to humans, where our comprehension of the environment is enhanced by integrating visual, auditory, and textual information, thereby offering a more holistic understanding of our surroundings.

## Limitations & Risks

**Balancing Cost and Accessibility. **The development and training of foundation models require a significant investment, posing a delicate balance between cost and accessibility. While adapting an existing model for a specific task might be more cost-effective than developing a new one from scratch, potentially democratizing access to cutting-edge AI capabilities, the substantial initial costs risk centralizing power among a few well-resourced entities. Ensuring equitable access and ethical use of these technologies is vital to harness their societal benefits fully.

**Homogenization**. The process of homogenization refers to the situation where an increasing number of AI systems are merely fine-tuned versions of the same foundation models. Therefore, if a foundation model has certain biases or failure modes, these could potentially be propagated to all models that are fine-tuned from this foundation. This is a significant risk because if the same problem exists in the foundation model, it could manifest across many different models and applications, leading to widespread and potentially correlated failures. For example, if a foundation model has been trained on data that has gender or racial biases, these biases could propagate to all models fine-tuned from it, leading to biased decisions across various applications, whether it be text generation, sentiment analysis, or even predictive policing.

**Emergence**. Increasing the centralization of general-purpose capabilities within a single model might result in unexpected and unexplainable behavior arising as a function of scale. This describes the phenomenon where foundation models exhibit complex behaviors or outputs not explicitly programmed, arising unpredictably from some underlying learned patterns. Emergent qualities rather than their explicit construction provide immense benefits, but this also makes foundation models hard to understand, predict, and control. This lack of predictability and control is a significant concern when these models are used in high-stakes domains. If they fail in ways that are outside our current understanding and expectations, these failures could be particularly problematic when combined with homogenization described above. The same foundation model integrated into multiple critical functions could lead to correlated failures that span multiple critical functions or failsafes. This phenomenon of emergence is also talked about in more detail in subsequent sections.

## Questions & Exercises

??? question "What are foundation models?"

	
	Foundation models are large-scale, pretrained models that serve as a base for fine-tuning on various downstream tasks. These models are trained on vast, diverse datasets to learn broad patterns and skills, enabling them to generalize well across different applications.
	
	*Example*: Imagine a foundation model like GPT-3, which has been trained on diverse internet text. It can then be fine-tuned to write poetry, generate code, or summarize articles, demonstrating its versatility.
	

??? question "How do foundation models differ from traditional machine learning models?"

	
	Foundation models differ from traditional machine learning models in that they are pretrained on massive datasets and then fine-tuned for specific tasks. Traditional models are typically trained from scratch for each individual task. This pretraining allows foundation models to leverage a wide range of knowledge, making them more efficient and versatile when adapting to new tasks.
	
	*Example*: Instead of building a new model to detect spam emails from scratch, you could fine-tune a foundation model like GPT, which has already learned a lot about language from a huge corpus of text.
	

??? question "What significant shift in AI strategy did the emergence of foundation models represent?"

	
	The emergence of foundation models marked a shift from the labor-intensive, one-model-per-task approach to developing generalist models trained on vast, unlabeled datasets. These models can be adapted to multiple tasks, leveraging large, diverse datasets to create versatile AI systems capable of handling various applications.
	
	*Example*: Instead of creating separate models for speech recognition, translation, and text generation, a single model like GPT-4 can be fine-tuned for all these tasks, saving time and resources.
	

??? question "What are the three main areas where significant investment is required for the development of foundation models?"

	
	The three main areas requiring significant investment for foundation models are:
	
	- Data Acquisition: Collecting, cleaning, and updating large-scale datasets.
	
	- Computational Resources: Providing the necessary hardware and electricity for training and deploying models.
	
	- Research and Development: Ongoing investment in developing new techniques and fine-tuning existing models, requiring financial resources and specialized expertise.
	
	*Example*: Training a model like GPT-3 required vast amounts of internet text (data acquisition), powerful GPUs and TPUs (computational resources), and a team of researchers to develop and refine the model (research and development).
	

??? question "Describe Self-Supervised Learning (SSL) and its significance in the training of foundation models."

    Self-Supervised Learning (SSL) is a technique that leverages unlabeled data to train models by predicting parts of the data from other parts. It allows models to learn from the inherent structure of the data, which is crucial as it eliminates the need for extensive human-provided labels. SSL enables the utilization of vast amounts of unlabeled data available on the web, significantly advancing the capability and scalability of AI models.

    *Example*: In SSL, a model might be trained to predict the missing words in a sentence (like filling in the blank). Given the sentence "The cat sat on the ____," the model learns to predict "mat," leveraging the context provided by the rest of the sentence.


??? question "What are zero-shot and few-shot learning, and why are they important in machine learning?"

	Zero-shot learning refers to models performing tasks without any specific examples, while few-shot learning involves models generalizing from a minimal set of examples. These techniques are important because they enable models to function effectively even when extensive labeled data is impractical or too costly to obtain. They enhance the versatility and adaptability of AI systems.
	
    *Example*: A zero-shot learning scenario could involve asking a language model to translate a sentence into a language it has never seen before. Few-shot learning could involve showing the model a few examples of translations before asking it to translate new sentences.

??? question "Explain the concept of transfer learning and its role in the development of foundation models."

	
	Transfer learning involves applying the general patterns, structures, and knowledge learned during the pre-training phase to new, related tasks. This technique allows models to utilize pre-existing knowledge, avoiding the need to start from scratch for every new task. It enhances efficiency and effectiveness in developing AI systems for diverse applications.
	
	*Example*: A model trained on general image recognition tasks could be fine-tuned to recognize specific types of medical images, such as identifying tumors in radiographs.
	

??? question "How does fine-tuning differ from pre-training in the context of foundation models?"

	
	Fine-tuning is the process of specifically adapting a pre-trained model to perform particular tasks. Unlike pre-training, which involves learning broad patterns from large datasets, fine-tuning hones the model's capabilities for specific applications. This step enables the creation of versatile models capable of undertaking a wide range of tasks with high accuracy.
	
	*Example*: OpenAI fine-tuned GPT-3 on specific datasets to enhance its ability to generate human-like text for customer support chatbots, making it more responsive and accurate in that context.
	

??? question "Why is scalability important in the performance of foundation models?"

	
	Scalability is crucial for foundation models as it dictates their ability to adapt and expand their capabilities by leveraging additional data, more powerful computing resources, or advancements in model architecture. As foundation models scale, they become more nuanced, capable, and efficient, enhancing their operational efficacy and broadening their applicability.
	
	*Example*: Scaling up models like GPT-3 from 1.5 billion parameters to 175 billion parameters resulted in significantly improved performance across a range of tasks, from language translation to question answering.
	

??? question "What is multi-modality, and why is it expected to become increasingly important in foundation models?"

	
	Multi-modality refers to the ability of foundation models to process, interpret, and generate insights from various types of data, such as text, images, audio, and video. This capability is expected to become increasingly important because it allows models to create richer, more nuanced representations of information, offering a more holistic understanding of complex environments and tasks.
	
	*Example*: A multi-modal model like DALL-E can generate images from textual descriptions, combining language and visual data to create unique and contextually appropriate images.
	

??? question "What are the risks associated with the homogenization of foundation models?"

	
	The homogenization of foundation models refers to the widespread use of fine-tuned versions of the same foundation models. This poses risks such as the propagation of biases or failure modes present in the original model across multiple applications. If a foundation model has certain biases, they can be replicated in all derivative models, leading to widespread and potentially correlated failures.
	
	*Example*: If a foundation model trained on internet text contains gender biases, these biases might manifest in various applications, such as biased hiring recommendations or biased language generation.
	

??? question "Describe the phenomenon of emergence in the context of foundation models and its potential implications."

	
	Emergence refers to the unexpected and unexplainable behaviors or outputs that arise from foundation models as they scale. These emergent qualities can provide immense benefits but also make the models hard to understand, predict, and control. This lack of predictability and control is particularly concerning in high-stakes domains, where unexpected failures can have significant consequences.
	
	*Example*: A model trained to generate text might start producing highly coherent but subtly harmful content, which was not explicitly programmed or anticipated by the developers.
	

??? question "How can the use of foundation models impact data privacy?"

	
	The use of foundation models can lead to privacy concerns because these models can inadvertently memorize and reproduce sensitive information from their training data. This is particularly problematic when the training data includes personal or confidential information, raising significant privacy and security issues.
	
	*Example*: A language model like GPT-3 might accidentally generate text containing personal information it encountered during training, such as snippets of private conversations or confidential documents.
	

??? question "How can centralized development of foundation models be both a benefit and a drawback for AI safety?"

	
	Centralized development of foundation models can be a benefit for AI safety because it allows for more controlled and coordinated efforts to ensure model safety and alignment. However, it can also be a drawback because any flaws or biases in the centrally developed models can propagate widely, affecting many downstream applications. Additionally, it might lead to power concentration in the hands of a few companies which poses a different dimension of risk.
	
	*Example*: A centrally developed model by a major AI company could be rigorously tested for safety and biases, but if an overlooked bias exists, it could impact a wide range of applications built on that model.
	

??? question "What are some potential unintended emergent capabilities in foundation models, and why are they concerning?"

	
	Unintended emergent capabilities in foundation models refer to unexpected behaviors or skills that arise when the model is fine-tuned or deployed in new contexts. These are concerning because they can lead to unpredictable and potentially harmful outcomes, making it challenging to ensure the model's safety and reliability.
	
	*Example*: A foundation model trained for general language tasks might unexpectedly develop the ability to generate convincing but false medical advice, posing risks if used in health-related applications.
	

