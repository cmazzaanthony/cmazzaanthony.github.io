---
title: 'Probability and The Triwizard Tournament'
date: 2020-03-31
permalink: /posts/2020/03/blog-post-2/
tags:
  - probability
  - independent events
---

Now let's get down to the brass tax and discuss what "probability" is?

Essentially every event $A$ gets assigned a real number $\mathbb{P}(A)$. $\mathbb{P}$ is often referred to as a **probability measure**.

There are some caveats here, a forewarning if you will.

$\mathbb{P}$ is considered a function, but not just **any** function. It needs to be a function that follows three rules, but more on that later.

First, it is important to note that a probability measure is just **one** type of "measure". There are many different measures and the study of them is referred to as "Measure Theory". Think of it like a ruler is just one way of measuring length, but there are others too such as inches and by hand thus = Measure Theory. 

But this post is not about **measure theory** (for those of you who want to know more, I will post some resources in the references section).

## Prerequisites & Notation

* $\Omega$: sample space; considered a [set](https://en.wikipedia.org/wiki/Set_(mathematics)).
* $\omega$: sample outcome
* $A$: event; a [subset](https://en.wikipedia.org/wiki/Set_(mathematics)) of $\Omega$.
* $\|A\|$: the number of elements in set $A$
* $a \in S$: the value $a$ is "a member of" or simply "in" set $S$.

So what makes a **probability measure** so special AND what makes it different from any other measure?

Well, before you answer this, let's start with a motivating example!

Recall, that Doctor Strange has been shown to use the time stone to look at all possible future events. He does this on the planet Titan before Thanos arrives to retrieve the time stone. I think it's reasonable to assume that Doctor Strange can also use the time stone to replay an experiment an infinite amount of times (we discussed this concept in the previous post).

Time for a more ambitious crossover!

In the first task of the Triwizard Tournament, all four Champions were required to dip their hand into a bag containing four miniature dragons: The Swedish Short-Snout, Common Welsh Green, The Chinese Fireball, and The Hungarian Horntail! Bonus points, for those of you who know which Champion chose which dragon.

We will refer to this first task selection as an **experiment**. To simplify, let's assume Harry Potter always chooses first (modelling this experiment would be more difficult otherwise).

## Probability Measure

Let's apply the skills we learned in the previous post to model the sample space. If Doctor Strange repeats this experiment once, then

$$\Omega &= \{ SSS, CWG, CF, HH \}$$

The event that Harry chooses the Swedish Short-Snout is 

$$A = \{ SSS \}$$

In this experiment, the sample space is **finite** meaning it has a limit in terms of how many elements are contained in the sample space. In this case there are four elements in the sample space and one element in our event: $\|\Omega\| = 4$ and $\|A\| = 1$. If $\Omega$ and each sample outcome is equally likely, then:

$$\mathbb{P}(A) = \frac{|A|}{|\Omega|}$$

Keep in mind that this is only true for a particular choice of probability measure. However, this is the most common choice of probability measure, but we could have chosen something different. Thus, the probability of Harry choosing a Swedish Short-Snout from the bag is 

$$\mathbb{P}(A) = \frac{1}{4}$$

Simple enough. Given what we just learned, now, I ask, what is highest a value a probability measure can take? What is the lowest value it can take? In other words, what are the bounds of the function $\mathbb{P}$? Recall, that in our example above $\Omega$ = {SSS, CWG, CF, HH} then $\mathbb{P}(\Omega) = 1$ (means the "the probability of Event $\Omega$"). The probability of Harry Potter choosing Swedish Short-Snout or the Common Welsh Green or the Chinese Fireball or the Hungarian Horntail is 1.0 because he has to choose one of those four dragons! In other words, previous events will have an impact on future events.

**Definition**: A function $\mathrm{P}$ is a probability measure if it satisfies the following:

* **Rule 1**: $\mathbb{P} (A) \ge 0$ for every $A$.
* **Rule 2**: $\mathbb{P} (\Omega) = 1$
* **Rule 3**: If $A_1, A_2 \dots$ are disjoint then

$$\mathbb{P} \Big( cup_{i=1}^{\infty} A_i \Big) &= \sum_{i=1}^{\infty} \mathbb{P} (A_i)$$

(Note: Two events are considered disjoint (mutually exclusive) if they cannot both occur at the same time.)

## Independent and Dependent Events

Random events happen in life all the time such as, which of the five people in the drive-thru will have the same order as you do, what are the chances that a store will have your size of sneaker, and what is the outcome of you asking a girl out for coffee? Most of the time, the sample space is small: two outcomes for a 'yes' or 'no'. However, it's important to navigate these outcomes.

See, it's like I tell my family, instead of worrying about events, trust in the numbers and all will be well.

However, in order to navigate we must discuss two very important concepts: 1) **independent**  and 2) **dependent** events.

A dependent event is one that relies on events that have come before. The best example of this is poker! The cards that come before very much influence the cards that will come after (the flop, the turn, and the river). These are said to be dependent events since future events depend on events that have previously occurred. Conversely, an independent event does not care about previous events.

Easy. Don't overthink!

For example, in a casino at the roulette table who will sometimes see a screen that indicates the number of times the ball landed on red vs. black. Usually a player will assume that since the ball has landed on a red 100 times and on black 90 times that in the upcoming toss the ball is more likely to land on black. However, **each** time the ball is rolled, this is considered an **independent event**, this is not the case and is often referred to as the Gamblers fallacy.

We will discuss dependent events in more detail later on. For now, rejoice in the fact that you know the difference between what is, and what can be.

**(Mathematical Definition)** Two events $A$ and $B$ are independent if

$$\mathbb{P}(AB) = \mathbb{P}(A) \cap \mathbb{P}(B)$$

A set of events $\{A_i : i \in I \}$ is independent if 

$$\mathbb{P} \Big( \bigcap_{i \in J} A_i \Big) = \prod_{i \in J} \mathbb{P} (A_i)$$


## References

Wasserman, L., 2013. All of statistics: a concise course in statistical inference. Springer Science \& Business Media. \\
\\
(2020, October 1). Probability of Independent Events. https://www.mathsisfun.com/data/probability-events-independent.html
