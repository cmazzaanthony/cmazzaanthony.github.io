from itertools import product
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import randint, bernoulli

stones = ['Space', 'Reality', 'Mind', 'Time', 'Power', 'Soul']
stones_scores = dict(zip(stones, range(1, 7)))
X_omega = {
    (stone1, stone2): stones_scores[stone1] + stones_scores[stone2]
    for stone1, stone2 in product(stones, repeat=2)
}
total_sample_outcomes = len(X_omega)
frequencies = dict.fromkeys(X_omega.values(), 0)
for sample_outcome, overall_score in X_omega.items():
    frequencies[overall_score] += 1

probabilities = pd.DataFrame(
    data=[
        [value, frequency / total_sample_outcomes]
        for value, frequency in frequencies.items()
    ],
    columns=['Total Score of Choosing Two Infinity Stones', 'Probability']
)

ax = sns.barplot(
    x='Total Score of Choosing Two Infinity Stones',
    y='Probability',
    data=probabilities,
)
plt.savefig("pmf")

# discrete uniform distribution
x = np.arange(1, 7)
y = randint.pmf(x, 1, 7)
ax = sns.barplot(
    x='x',
    y='f(x)',
    data=pd.DataFrame(data=list(zip(x, y)), columns=['x', 'f(x)']),
)
plt.savefig("uniform_pmf")

# bernoulli distribution
p = 0.5
bernoulli()


