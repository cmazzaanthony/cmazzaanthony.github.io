# PDF post
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

mean = 6  # mean time passed before Rick burps
std = 1.2  # std of time passed before Rick burps
samples = np.random.normal(6, 1.2, size=1000)

ax = sns.distplot(
    samples,
    hist=True,
    kde=True,
    bins=20,
    color='darkblue',
    hist_kws={'edgecolor': 'black'},
    kde_kws={'linewidth': 4},
)
ax.set_xlabel("Amount of time between Rick's burps in the next episode")
ax.set_ylabel("Density")
plt.show()
# plt.savefig('pdf.png')


# Compute Probabilities of a PDF (Area under the Curve)
pdf_func = norm(mean, std).pdf
probability, error = quad(pdf_func, 0, 12)  # computes integral of function
