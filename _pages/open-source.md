---
layout: archive
title: "Open-Source"
permalink: /open-source/
author_profile: true
---

{% include base_path %}

## [Coptim: Optimization Framework](https://cmazzaanthony.github.io/coptim/)

The repository is available [here](https://github.com/cmazzaanthony/coptim).

### Description
Optimization framework that includes implementations of popular methods
for solving convex smooth/non-smooth objective functions.

```python
from src.optimizers.gradient_method import GradientMethod

objective = Rosenbrock()
starting_point = np.array([-1.2, 1])
beta = 0.5
sigma = 0.0001
epsilon = 0.0001

optimizer = GradientMethod()

x = optimizer.optimize(starting_point,
                       objective,
                       beta,
                       sigma,
                       epsilon)

print(f'Optimal Point: {x}')
print(f'Iterations: {optimizer.iterations}')
```

```
Optimal Point: [0.99992058 0.9998407 ]
Iterations: 8058
```

----

## [ccgowl: Gaussian Graphical Model library](https://cmazzaanthony.github.io/ccgowl/)

The repository is available [here](https://github.com/cmazzaanthony/ccgowl).

### Description
We address the task of estimating sparse structured precision matrices for multivariate Gaussian random variables within a graphical model
framework. We propose two novel estimators based on the Ordered Weighted $\ell_1$ (OWL) norm: 1) The Graphical OWL (GOWL) is a penalized likelihood method that applies the OWL norm to the lower triangle components of the precision matrix. 2) The column-by-column Graphical OWL (ccGOWL) estimates the precision matrix by performing OWL regularized linear regressions. Both methods can simultaneously identify groups of related edges in the graphical model and control the sparsity in the estimated precision matrix. We propose proximal descent algorithms to find the optimum for both estimators. For synthetic data where group structure is present, the ccGOWL estimator requires significantly reduced computation and achieves similar or greater accuracy than state-of-the-art estimators. Timing comparisons are presented and demonstrate the superior computational efficiency of the ccGOWL. We demonstrate the efficacy of the ccGOWL estimator on two domains---gene network analysis and econometrics.

<br/><img src='/images/fig_groups-01.png' width="100%" height="500">
