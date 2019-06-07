---
title: "Learning Gaussian Graphical Models with Ordered Weighted L1 Regularization."
collection: publications
permalink: /publication/2019-06-07-GOWL-number-2.md
excerpt: 'We address the task of identifying densely connected subsets of multivariate 
Gaussian random variables within a graphical model framework. We propose two novel estimators 
based on the Ordered Weighted ℓ1 (OWL) norm: 1) The Graphical OWL (GOWL) is a penalized 
likelihood method that applies the OWL norm to the lower triangle components of the 
precision matrix. 2) The column-by-column Graphical OWL (ccGOWL) estimates the precision 
matrix by performing OWL regularized linear regressions. Both methods can simultaneously 
identify highly correlated groups of variables and control the sparsity in the resulting 
precision matrix. We formulate GOWL such that it solves a composite optimization problem 
and establish that the estimator has a unique global solution. In addition, we prove 
sufficient grouping conditions for each column of the ccGOWL precision matrix estimate. 
We propose proximal descent algorithms to find the optimum for both estimators. For synthetic 
data where group structure is present, the ccGOWL estimator requires significantly reduced 
computation and achieves similar or greater accuracy than state-of-the-art estimators. Timing 
comparisons are presented and demonstrates the superior computational efficiency of the ccGOWL. 
We illustrate the grouping performance of the ccGOWL method on a cancer gene expression data 
set and an equities data set'
date: 2019-06-07
venue: 'Submitted to NeurIPS 2019'
paperurl: 'http://cmazzaanthony.github.io/files/1906.02719.pdf'
citation: 'Mazza-Anthony, C., Mazoure, B., Coates, M., 2019. 
Learning Gaussian Graphical Models with Ordered Weighted L1 Regularization. 
arXiv preprint arXiv:1906.02719, 2019.'
---