import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import glob
import os

li = []
num = 1000

columns = ['urlLen', 'authorityLen', 'pathLen', 'queryLen']
csv_files = glob.glob("2019-35/year-month/*.tsv")
csv_files.sort()

for file in csv_files:
 data = pd.read_csv(file, sep='\t', header=None, names=columns)
 data = data.sample(n = num, replace = False)
 li.append(data)

df = pd.concat(li, axis=0)
#df.astype('int')

print(df)


############## Correion ##################################
print('Query', df['urlLen'].corr(df['queryLen']))

# plot the data
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100})
sns.lmplot(x='queryLen', y='urlLen', data=df, line_kws={'color': 'red'})

plt.title("URL Length vs Query Length");
 
# Labelling axes
plt.xlabel('Query Length')
plt.ylabel('URL Length')

plt.tight_layout()
plt.savefig('result/queyr_corr.jpeg', dpi=500)
############################################
print('Authority', df['urlLen'].corr(df['authorityLen']))

sns.lmplot(x='authorityLen', y='urlLen', data=df, line_kws={'color': 'red'})

plt.title("URL Length vs Authority Length");

# Labelling axes
plt.xlabel('Authority Length')
plt.ylabel('URL Length')

plt.tight_layout()
plt.savefig('result/auth_corr.jpeg', dpi=500)
##################################################
print('Path', df['urlLen'].corr(df['pathLen']))

sns.lmplot(x='pathLen', y='urlLen', data=df, line_kws={'color': 'red'})

plt.title("URL Length vs Path Length");
 
# Labelling axes
plt.xlabel('Path Length')
plt.ylabel('URL Length')

plt.tight_layout()
plt.savefig('result/path_corr.jpeg', dpi=500)


