from itertools import product
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

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
