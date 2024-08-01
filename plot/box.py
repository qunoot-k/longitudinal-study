import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_hist = pd.read_csv("./2019-35/year-month/2009-01.tsv", sep='\t', header=None, usecols=[0, 2], names=['URL Length', 'Path Length'])
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16,8))
sns.boxplot(x=df_hist['URL Length'], ax=ax1)
sns.boxplot(x=df_hist['Path Length'], ax=ax2)
#ax1.hist(df_hist['URL Length'], bins=15)
#ax2.hist(df_hist['Path Length'], bins=15)
plt.tight_layout()
plt.savefig('result/2009_09_box.jpeg', dpi=500)

df_hist = pd.read_csv("./2019-35/year-month/2013-08.tsv", sep='\t', header=None, usecols=[0, 3], names=['URL Length', 'Query Length'])
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(16,8))
sns.boxplot(x=df_hist['URL Length'], ax=ax1)
sns.boxplot(x=df_hist['Query Length'], ax=ax2)
#ax1.hist(df_hist['URL Length'], bins=15)
#ax2.hist(df_hist['Query Length'], bins=15)
plt.tight_layout()
plt.savefig('result/2013_08_box.jpeg', dpi=500)

