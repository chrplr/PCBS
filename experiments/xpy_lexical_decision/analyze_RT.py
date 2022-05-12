""" analyze reaction-rimes of lexdec experiment """

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import scipy

results = pd.read_csv('data/lexdec_v3_02_202112131227.xpd', comment='#')
results.head()

# average RTs
results.groupby(results.cat).describe()

# distributions
sns.boxplot(x="cat", y="RT", hue="respkey", data=results)
plt.show()

# T-test
scipy.stats.ttest_ind(results.RT.loc[results.cat == 'W'],
                      results.RT.loc[results.cat == 'P'],
                      equal_var=False)
