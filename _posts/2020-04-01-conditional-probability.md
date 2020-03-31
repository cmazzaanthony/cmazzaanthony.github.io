---
title: 'Dragons and Conditional Probability'
date: 2020-04-01
permalink: /posts/2020/03/blog-post-3/
tags:
  - probability
  - dependent events
---

Think of conditional probability as a way to analyze **dependent** events. Dependent events are events affected by previous events. We denote the conditional probability as $\mathbb{P} (A \| B)$ which means the probability of event A occurring given event B has already happened.

Recall, the Triwizard Tournament example from the previous post where our sample space was $\Omega$ = {SSS, CWG, CF, HH}. In order to illustrate the effects of dependent events lets change the sample space to the following: $\Omega$ = { SSS, SSS, CWG, CWG, CWG, CF, HH} where

* SSS = Swedish Short-Snout
* CWG = Common Welsh Green
* CF = Chinese Fireball
* HH = Hungarian Horntail

The chances of choosing a Swedish Short-Snout are 2 in 7. If Fleur Delacour chose Swedish Short-Snout, what are the chances of then choosing a Swedish Short-Snout? Well, the chances have changed since we removed a dragon from the bag because there's now one less!

The idea here is that if we replaced the dragons each time a wizard chose one, then the probability would not change and the events are considered independent. However, in this example the dragons are **not** being replaced, thus the events are considered dependent.

**(Mathematical Definition)** If $\mathbb{P}(A) > 0$ then the **conditional probability** of $B$ given $A$ is

$$\mathbb{P}(B|A) = \frac{\mathbb{P} (AB)}{\mathbb{P} (A)}$$

Let's discuss this notation a bit more.

In our example let's say event $A$ is "choose a Swedish Short-Snout first" with a probability of 2/7 and event $B$ is "choose a Swedish Short-Snout second".

Now here is the tricky part, for event $B$ we have four choices:
    
(a) If we chose a Swedish Short-Snout first the probability is now 1/6.

(b) If we chose a Common Welsh Green the probability is now 3/6.

(c) If we chose a Chinese Fireball the probability is now 1/6.

(d) If we chose a Hungarian Horntail the probability is now 1/6.

We have to stipulate which one happened must have happened first. To do that we use the mathematical symbol "$\|$" to denote "given". Thus, $\mathbb{P}(A\|B)$ means "Event A given event B" and is also referred to as the conditional probability of A given B. Let's do an example using our fancy new notation! What are the chances of choosing a Common Welsh Green dragon first (Event A), and then choosing a Common Welsh Green second (Event B). So we can start with the conditional probability formula and rearrange a bit:

$$\mathbb{P}(B|A) = \frac{\mathbb{P} (AB)}{\mathbb{P} (A)}$$
$$\mathbb{P} (AB) = \mathbb{P}(B|A) \mathbb{P} (A)$$

We know the chances of choosing a Common Welsh Green is 3/7 ($\mathbb{P} (A)$), but after we remove that dragon from the bag, the second dragon chosen from the bag is less likely to be a Common Welsh Green: $\mathbb{P} (B\|A) = 2/6$.

So we plug in the numbers:

$$\mathbb{P} (AB) = 2/6 * 3/7$$
$$\mathbb{P} (AB) = 0.14$$

This may seem simple, but sometimes it can be tricky. For instance, it is usually not the case that $\mathbb{P}(A\|B) = \mathbb{P}(B\|A)$. In fact, they can be extremely different! Let's think about this when answering the question: What is the probability of choosing a Swedish Short-Snout given that we chose a Chinese Fireball first ($\mathbb{P}(A\|B)$)?

Secondly, is this probability the same as choosing a Chinese Fireball given a Swedish Short-Snout was chosen first ($\mathbb{P}(B\|A)$)?

Well, the answer to the first question is 2/6, since there are two Swedish Short-Snout's in the bag once we removed the Chinese Fireball. Now, if we chose the Swedish Short-Snout first and then chose the Chinese Fireball, the probability of this event would be 3/6. See! Not the same! $\mathbb{P}(A\|B) \ne \mathbb{P}(B\|A)$!

In the next Triwizard Tournament, you will know exactly what your probabilities of choosing each dragon will be! Hopefully, this new skill will help make it passed task one.

## References

Wasserman, L., 2013. All of statistics: a concise course in statistical inference. Springer Science \& Business Media.

(2020, October 1). Conditional Probability. https://www.mathsisfun.com/data/probability-events-conditional.html
