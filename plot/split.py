import pandas as pd
import sys

columns = ['url', 'urlLen', 'authorityLen', 'pathLen', 'queryLen', 'epoch']
keep_cols = ['urlLen', 'authorityLen', 'pathLen', 'queryLen']
file=sys.argv[1]
print("{}.tsv start".format(file))
data = pd.read_csv('2019-35/merge_10_seg/{}.tsv'.format(file), sep='\t', header=None, names=columns)
data = data[(data["epoch"] > 946684800) & (data["epoch"] < 1567295999)]
data['epoch'] = pd.to_datetime(data['epoch'], unit='s')
for i, x in data.groupby(data['epoch'].dt.to_period('M')):
 x.to_csv("2019-35/year-month/{}.tsv".format(i), sep="\t", index=False, header=False, mode='a', columns=keep_cols)
     #x.to_csv("2019-35/year-month/{}.tsv".format(i), sep="\t", index=False, header=False, mode='a')
print("{}.tsv end".format(file))
