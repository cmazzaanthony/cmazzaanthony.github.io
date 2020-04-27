import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


probabilities = pd.DataFrame(
    data=[
        [0, 0.2],
        [1, 0.1],
        [2, 0.5],
        [3, 0.2],
    ],
    columns=['The number of times Morty says \'Ah Jeez\'', 'Probability']
)

ax = sns.barplot(
    x='The number of times Morty says \'Ah Jeez\'',
    y='Probability',
    data=probabilities,
)
plt.savefig('pmf_moments')

expected_value = (probabilities['The number of times Morty says \'Ah Jeez\''] * probabilities['Probability']).sum()



