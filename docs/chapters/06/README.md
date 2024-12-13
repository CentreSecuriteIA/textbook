# Specification

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
            Jeanne Salle, Oscar Heitmann, Ram Rachum, Nicolas Guillard, Camille Berger
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
                <div class="meta-value">2023-12-01</div>
            </div>
        </div>
        
        <!-- Reading Time -->
        <div class="meta-item">
            <span class="meta-icon">
                <i class="fas fa-book-open"></i>
            </span>
            <div class="meta-content">
                <div class="meta-label">Reading Time</div>
                <div class="meta-value">59 minutes</div>
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
                    <a href="https://www.lesswrong.com/s/3ni2P2GZzBvNebWYZ/p/mMBoPnFrFqQJKzDsZ" class="meta-link">Alignment Forum</a> · <a href="https://docs.google.com/document/d/1kEdmyVTUG3MO7lwuw4utHEm7CcavvgAiUZcWHaOZuPY/edit?usp=sharing" class="meta-link">Google Docs</a>
                </div>
            </div>
        </div>
    </div>
</div>

</div>

[Feedback](https://forms.gle/ZsA4hEWUx1ZrtQLL9){ .md-button }
[Facilitate](https://docs.google.com/document/d/1JfmzGii5QG6hW8AM5WxzDBVyGc14aLV_Lc_1PkK2ZLc/edit?usp=sharing){ .md-button }

# Introduction

**Reinforcement Learning**: The chapter starts with a reminder of some reinforcement learning concepts. This includes a quick dive into the concept of rewards and reward functions. This section lays the groundwork for explaining why reward design is extremely important.

**Optimization**: This section briefly introduces the concept of Goodhart's Law. It provides some motivation behind understanding why rewards are difficult to specify in a way such that they do not collapse in the face of immense optimization pressure.

**Reward misspecification**: With a solid grasp of the notion of rewards and optimization the readers are introduced to one of the core challenges of alignment - reward misspecification. This is also known as the Outer Alignment problem. The section begins by discussing the necessity of good reward design in addition to algorithm design. This is followed by concrete examples of reward specification failures such as reward hacking and reward tampering.

**Learning by Imitation**: This section focuses on some proposed solutions to reward misspecification that rely on learning reward functions through imitating human behavior. It examines proposals such as imitation learning (IL), behavioral cloning (BC), and inverse reinforcement learning (IRL). Each section also contains an examination of possible issues and limitations of these approaches as they pertain to resolving reward hacking.

**Learning by Feedback**: The final section investigates proposals aiming to rectify reward misspecification by providing feedback to the machine learning models. The section also provides a comprehensive insight into how current large language models (LLMs) are trained. The discussion covers reward modeling, reinforcement learning from human feedback (RLHF), reinforcement learning from artificial intelligence feedback (RLAIF), and the limitations of these approaches.