# PDF post
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import quad

mean = 6  # mean time passed before Rick burps
std = 1.2  # std of time passed before Rick burps
# samples = np.random.exponential(6, size=1000)

# uniform distribution
a = 1
b = 10
samples = np.random.uniform(a, b, size=100000)
ax = sns.distplot(
    samples,
    kde=False,
    bins=5,
    color='darkblue',
    hist_kws={'edgecolor': 'black'},
)
plt.savefig('uniform_pdf.png')


# geometric distribution
mean = 1.0
std = 2.0
x = np.random.randint(0, 5, 100)
y = norm(mean, std).pdf(x)
ax = sns.barplot(
    x='x',
    y='f(x)',
    data=pd.DataFrame(data=list(zip(x, y)), columns=['x', 'f(x)']),
    palette="Blues_d",
)
plt.savefig("normal_pdf")

# ax = sns.distplot(
#     samples,
#     hist=True,
#     # kde=True,
#     bins=10,
#     # color='darkblue',
#     hist_kws={'edgecolor': 'black'},
#     # kde_kws={'linewidth': 4},
# )
# ax.set_xlabel("Amount of time between Rick's burps in the next episode")
ax.set_xlabel("x")
ax.set_ylabel("Density")
plt.show()
# plt.savefig('pdf.png')


# Compute Probabilities of a PDF (Area under the Curve)
# pdf_func = norm(mean, std).pdf
# probability, _ = quad(pdf_func, 0, 12)  # computes integral of function
#
# expectation, _ = quad(lambda x: x * pdf_func(x), a=-np.inf, b=np.inf)[0]

# https://stackoverflow.com/questions/55788868/how-to-return-mean-value-or-expectation-value-of-a-distribution-estimated-via
