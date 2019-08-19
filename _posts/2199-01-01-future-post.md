---
title: 'An Introduction to Convex Optimization'
date: 2020-01-01
permalink: /posts/2012/08/blog-post-4/
tags:
  - convexity
  - optimization
---

This article is the first part of a series of articles that will examine and outline 
different optimization algorithms from basic to more advanced. 

To quote one of my favorite researchers, "Everything is an optimization problem". When I 
first took mathematical optimization in my master's degree at McGill, I struggled. 
It involved a lot of linear algebra, real analysis, and a good amount of proofs. My background
is mainly computer science and I have worked in industry as a programmer so the course was 
a difficult ride. The main goal of this series of blog posts is more pragmatic with maybe a 
proof here or there. I will provide the algorithm, the implementation, and few examples of 
how to use these algorithms in research and industry.

So what is an optimization problem? Fundamentally it is taking an idea and translating this 
concept into the form P : min .. This idea could be traversing traffic on your way to work in
the morning. It could be fitting a linear model to some data. It could be trying to manage 
your retirement savings or creating a budget. The applications are endless! 
The approach is to your idea and translates into a function that can be minimized.
 
## Convex Sets and Functions

Let's begin with the basics. A set $C \subset \mathbb{R}^n$ is called convex if

$$\lambda x + (1 - \lambda) y \in C \quad (x, y \in C, \lambda \in (0,1))$$

Simply put, a set is convex if a line can be drawn between any two points that will remain in the set.
