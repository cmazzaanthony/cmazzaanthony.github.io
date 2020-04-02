---
title: 'The Unbreakable Bayes Theorem'
date: 2020-04-02
permalink: /posts/2020/03/blog-post-4/
tags:
  - probability
  - bayes' theorem
---

It is said by many that Bayes' Theorem is one of the most important theorems in all of mathematics and philosophy. Let's say right now we have some evidence which leads to a **hypothesis**. Five minutes pass and we then acquire new evidence which needs to be accounted for in our previous hypothesis. How do we update our hypothesis? In this post, we will outline all you need to know about the famous theorem!

Like previous posts, we will set the stage by relating this theorem to some pop culture. In what I think is M. Night Shyamalan's best film, [Unbreakable](https://en.wikipedia.org/wiki/Unbreakable_(film)), David Dunn is a man who begins to discover that he possesses superhuman abilities. Unbreakable is the first installment in a trilogy of films referred to as the *Eastrail 177 Trilogy*. In further films, David meets other so called "enhanced" humans, such as the character Kevin Wendell Crumb, a person who suffers from multiple personality disorder, but also possesses superhuman abilities like David. I really loved the films Unbreakable and Split; I highly recommend them. Where was I? Ahh yes, Bayes' Theorem.

<p align="center">
  <img width="460" height="300" src="https://media0.giphy.com/media/2tSjIKp84Pp6pgq7oY/giphy.gif">
</p>

Let's start with the definition of Bayes' Theorem and connect it back to the aforementioned pop culture reference. Let $H$ denote our hypothesis and $E$ denote our evidence. Bayes' Theorem is defined by

$$\mathbb{P} (H | E) = \frac{\mathbb{P} (H)  \mathbb{P} (E | H)}{\mathbb{P} (E) }$$

So essentially what Bayes theorem is trying to explain is the $\mathbb{P} (H \| E)$ conditional probability (see previous post for more details). It's saying what is the probability that my hypothesis is true given the evidence we have. In order to answer this questions, we need three things: the probability the hypothesis is true $\mathbb{P} (H)$, the probability of the evidence given that the hypothesis is true $\mathbb{P} (E \| H)$, and the probability of the evidence $\mathbb{P} (E)$.

We are going to do our first proof that shows why Bayes' Theorem is true. This proof will illustrate why it is important to believe in mathematical statements and how powerful they can be! Let's begin by stating two definitions $\mathbb{P} (B \| A)$ and $\mathbb{P} (A \| B)$:

$$\mathbb{P} (B | A) = \frac{\mathbb{P} (A \cap B)}{\mathbb{P} (A)}$$

$$\mathbb{P} (A | B) = \frac{\mathbb{P} (A \cap B)}{\mathbb{P} (B)}$$

Now, lets rearrange and set them to be equal. Well, how do we do that? We will use the fact that $\mathbb{P} (A \cap B)$ is present in both formulas.

$$\mathbb{P} (B | A) \mathbb{P} (A) = \mathbb{P} (A | B) \mathbb{P} (B)$$

Do you see it? Let's do one more rearrangement

$$\mathbb{P} (B | A) = \frac{\mathbb{P} (A | B) \mathbb{P} (B)}{\mathbb{P} (A)}$$

It's just like magic! We just derived Bayes' Theorem by using the conditional probability formula!

So, this may seem pretty meaningless by itself, but I feel that Bayes' Theorem really shows its magic when used in an example.

Circling back to Unbreakable, lets start by putting ourselves in the shoes of David Dunn. Throughout the film, David starts to notice his superhuman abilities such as the time where he is the sole survivor of a train crash or the time he bench presses 400 pounds. Let's pretend we are half way through the film where the only evidence David has is that he survived a train crash and can bench big weight! He decides that the probability of these abilities given that he is a superhuman is very high let's say $0.99$ or 99%, we will denote this $\mathbb{P} (E \| H)$. In other words, if you are superhuman than you will most likely be very strong and have an uncanny level of invulnerability. Because of this, David begins to freak out because he doesn't want the life of a superhero. He just wants to take care of his family and lead a normal life. However, David educates himself with Bayes' Theorem and realizes he needs more information before he begins to freak out. He needs to know what is the probability of actually being superhuman. Well, that's pretty low, but since we are in a fictitious superhero universe, let's say he decides on a 1 in a million chance, 0.000001 to be exact. We will denote this $\mathbb{P} (H)$. Finally, we need the last key ingredient. How common is it to have survived a train crash and be able to bench press 400 pounds. Well, this number should be a bit higher. There are regular humans in the world who can bench a lot and survive a train crash. We denote this value by $\mathbb{P} (E)$ or the probability of the evidence occurring. Lets give this a value of 1 / 10000. Now we have everything we need! Let's apply Bayes' Theorem:

$$\mathbb{P} (H | E) = \frac{\mathbb{P} (H)  \mathbb{P} (E | H)}{\mathbb{P} (E) }$$

$$\mathbb{P} (H | E) = \frac{ 0.000001 * 0.99}{0.0001}$$

$$\mathbb{P} (H | E) = 0.0099$$

David takes a much needed sigh of relief. Essentially, his chances are very low that he is indeed a superhero, only 1%. However, as the film progresses more unusual things begin to occur that affect the probability of the evidence. David begins to realize that by touching people he can read their minds, especially thoughts that relate to violence. Now this ability should be considered almost none-existent in the human race. David has to update his beliefs! He changes $\mathbb{P} (E)$ from 1 in ten thousand to 1 in 950000 and decides to recalculate. 

$$\mathbb{P} (H | E) = \frac{\mathbb{P} (H)  \mathbb{P} (E | H)}{\mathbb{P} (E) }$$

$$\mathbb{P} (H | E) = \frac{ 0.000001 * 0.99}{0.00000105263}$$

$$\mathbb{P} (H | E) = 0.941$$

Uh oh, now the probability has gone way up! There is a 94.1\% chance that David Dunn is superhuman given the evidence of bench pressing 400 pounds, surviving a train crash, and being able to read minds. Spoilers ahead! By the end of the film David becomes quite certain that he is special and **is** a super hero!

## References

[Khan Academy]. (2020, March 30). Bayes Theorem. [Video File]. Retrieved from https://www.khanacademy.org/partner-content/wi-phi/wiphi-critical-thinking/wiphi-fundamentals/v/bayes-theorem?modal=1
