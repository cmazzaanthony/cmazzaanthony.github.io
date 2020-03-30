---
title: 'Infinity Stones and Sample Spaces'
date: 2020-04-01
permalink: /posts/2020/03/blog-post-1/
tags:
  - probability
  - sample space
---

Mastering probability is as close as one gets to having a super power. It's one of those increasingly useful skills that you can apply to your everyday life. You can use it to determine the outcome of certain events, win big at the casino, and even use it to stop the mighty Thanos from wiping out half the universe! Kidding.  Essentially, what I am saying is probability is how you quantify/describe a random event. It's a language and a foresight that allows you to make informed decisions and to, quite possibly, know what happens before it happens.

## Prerequisites & Notation

* $\Omega$: sample space (considered a [set](https://en.wikipedia.org/wiki/Set_(mathematics))
* $\omega$: sample outcome
* $A$: event ([subset](https://en.wikipedia.org/wiki/Set_(mathematics) of $\Omega$)
* $\|A\|$: the number of elements in set $A$
* $a \in S$: the value $a$ is "a member of" or simply "in" set $S$.

Let's start with an example!

I love comic books so all the examples in this blog series will be centered around comics, cinematic universes, and all pop culture goodness that comes with being a self-professed geek! I assume a lot of readers are familiar with such, so let's jump right into it. Assume, for instance, Iron Man is facing off with the mad titan Thanos, who already possesses all six infinity stones. During their fiery battle, the goal for Stark is to prevent Thanos from snapping his fingers, and to ensure this, all Iron Man needs is ONE out of SIX stones!

Now, since Thanos is the toughest bad guy around, we will consider this liaison as a "random event". Iron Man is all on his own without Thor, Captain Marvel, and the other avengers, thereby we assume that Iron Man can only acquire one of the six infinity stones and flee before Thanos obliterates him. We must also state that acquiring only one of the six infinity stones from Thanos are **equally likely outcomes**. We must also note that this battle is **easily repeatable** and that in each battle the outcomes do **not** change.

Lots to take in? Welcome to Math, and don't worry. It gets easier.

We will refer to this battle as an "experiment". In this experiment, there are **six** possible outcomes: acquiring the soul stone, time stone, space stone, mind, reality and power stones. After one battle with Thanos, I ask, what is the probability of acquiring, let's say, the mind stone?

And, after two more battles with the tyrannical Thanos, what is the probability of acquiring the time and space stones too? By the end of the blog, you will be able to answer both these questions. First, a little notation.

## Sample Spaces and Events

As many know, Mathematics is an extremely rigorous endeavour. So, in order to speak intelligently about this intense battle between Iron Man and Thanos, we begin gradually, by defining a few things.

We will begin with the **sample space**. A sample space represented by $\Omega$ is the set of all possible outcomes in an experiment. Elements in the set $\Omega$ are denoted by $\omega$ and are called **sample outcomes**. Any subset of $\Omega$ is called an **event** and is denoted by $A$.

Back to the Thanos example, if we battle Thanos exactly once then our sample space is defined by $\Omega = {soul, time, space, mind, reality, power}$. A sample outcome would be acquiring the power stone defined by $\omega = power$. An event can be one or more sample outcomes (subset) of an experiment. Let's get a bit tougher, what is the sample space if we battle Thanos, let's say...twice?

How do we define the event where we pick the **same** infinity stone in **both** battles? Well, in this case there are 36 sample outcomes ($\|\Omega\| = 36$) and in our sample space: $\{ (soul, time), (soul, space) , ...\}$. If this is confusing, don't worry. I don't find it by any means obvious why there are 36 possible sample outcomes. In order to better understand this, we will dabble in \textit{combinatorics}. The number of sample outcomes can be calculated using the formula $n^r$ where $n$ represents the number of items to choose from and $r$ represents the number we wish to choose. So in our example there are 6 infinity stones to choose from and we want to choose 2 of them, thus $6^2 = 36$ ([reference](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)).

We won't list all the possibilities, but instead we will do something even better to define this **sample space**. We will use mathematical notation!

If we fight Thanos twice the sample space is the set:

$$\Omega = \Big\{ \omega = (\omega_1, \omega_2) : \omega_1, \omega_2 \in \{ soul, time, space, mind, reality, power \} \Big\}$$

The symbol $\in$ simply means that an element is in the set. If $\omega_1 = soul$ and the set $S = \{ soul, time, space, mind, reality, power\}$. Then we can say that the soul stone is "a member of" the set $S$ or in set notation: $\omega_1 \in S$. The event of picking the same infinity stone in both battles can be described as:

$$A = \{(soul, soul), (time, time), (space, space), (mind, mind), (reality, reality), (power, power) \}$$

with $|A| = 6$. What we would be the sample space if Iron Man fought Thanos an infinite amount of times? Well, it would be the following:

$$\Omega = \Big\{ \omega = (\omega_1, \omega_2, \dots) : \omega_i \in \{ soul, time, space, mind, reality, power \} \Big\}$$

As Captain America would say, "I can do this all day".

So what is a probability? Well, it can be defined as:

$$\text{Probability of an event occurring} = \frac{\text{Number of ways an event can occur}}{\text{Total number of sample outcomes}}$$

So let's tie this concept back to our example. If Iron Man fights Thanos **twice**, what is the probability that Iron Man takes the **same** infinity stone? Well, the total number of sample outcomes was $\|\Omega\| = 36$ and the number of ways it can happen was $|A| = 6$ so we simply divide $6/36 = 1/6$. Thus, there is a 1 in 6 chance that Iron Man picks the same infinity stone in both battles. We will elaborate on this concept in the next post.

To summarize, in this blog post we essentially learned what a random experiment is in probability theory. To formalize, a random experiment consists of three parts:

1. A sample space $\Omega$, which is the set of all sample outcomes.
2. A set of events, where each event $A$ is a subset of $\Omega$ containing zero or more sample outcomes.
3. Each event must have a probability assigned to it.

Now, what does this mean for you? Well, now that the fundamental buildings are in place, and have taken the first steps towards understanding statistics, you see that math is often found in the least expected, yet most exciting places!

It is, as Nick Fury said, at the end of Iron Man, "Mr. Stark, you've become part of a bigger universe. You just don't know it yet."

## References

Wasserman, L., 2013. All of statistics: a concise course in statistical inference. Springer Science \& Business Media.

(2020, October 1). Probability. https://www.mathsisfun.com/data/probability.html


