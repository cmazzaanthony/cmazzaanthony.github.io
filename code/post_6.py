# PDF post
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


burps_per_episode = [20, 19, 14, 13, 12, 11, 11, 11, 10, 8, 8, 7, 6, 5, 4, 3, 3, 2, 2, 1, 1]
mean_burps_per_episode = np.array(burps_per_episode).mean().round(1)
variance_burps_per_episode = np.array(burps_per_episode).var().round(1)

print(mean_burps_per_episode)
print(variance_burps_per_episode)

# 1. Pick a distribution, easiest is Gaussian, use mean and variance

# sns.distplot(burps_per_episode, hist=True, kde=True,
#              bins=int(180/5), color = 'darkblue',
#              hist_kws={'edgecolor':'black'},
#              kde_kws={'linewidth': 4})
#
# plt.show()
