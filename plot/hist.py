import pandas as pd
import matplotlib.pyplot as plt
import glob
import os


li_hist = []


columns = ['urlLen', 'authorityLen', 'pathLen', 'queryLen']
csv_files = glob.glob("./2019-35/year-month/2018*.tsv")
csv_files.sort()

for file in csv_files:
 data = pd.read_csv(file, sep='\t', header=None, names=columns)
 li_hist.append(data)


df_hist = pd.concat(li_hist, axis=0)
df_hist.astype('int')

print(df_hist.describe())

limit=0.995
quant_urlLen = df_hist['urlLen'].quantile(limit)
quant_authorityLen = df_hist['authorityLen'].quantile(limit)
quant_pathLen = df_hist['pathLen'].quantile(limit)
quant_queryLen = df_hist['queryLen'].quantile(limit)


urlLen = df_hist.urlLen
authorityLen = df_hist.authorityLen
pathLen = df_hist.pathLen
queryLen = df_hist.queryLen

figure, axis = plt.subplots(2, 2, figsize=(16,8))

print('Data')
(n2, bins2, patches) =  axis[0,0].hist(urlLen.loc[lambda x : x < quant_urlLen], alpha=0.8, edgecolor = "black")
axis[0,0].set_title("URL Length 2018")
#axis[0,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[0,1].hist(authorityLen.loc[lambda x : x < quant_authorityLen], alpha=0.8, edgecolor = "black")
axis[0,1].set_title("Authority Length 2018")
#axis[0,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[1,0].hist(pathLen.loc[lambda x : x < quant_pathLen], alpha=0.8, edgecolor = "black")
axis[1,0].set_title("Path Length 2018")
#axis[1,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[1,1].hist(queryLen.loc[lambda x : x < quant_queryLen], alpha=0.8, edgecolor = "black")
axis[1,1].set_title("Query Length 2018")
#axis[1,1].tick_params(axis='x', labelsize = 'xx-small')
print(n2, bins2, patches)



###########################
figure, axis = plt.subplots(2, 2, figsize=(16,8))


print('Data')
(n2, bins2, patches) =  axis[0,0].hist(urlLen.loc[lambda x : x > quant_urlLen], alpha=0.8, edgecolor = "black")
axis[0,0].set_title("URL Length 2018")
#axis[0,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[0,1].hist(authorityLen.loc[lambda x : x > quant_authorityLen], alpha=0.8, edgecolor = "black")
axis[0,1].set_title("Authority Length 2018")
#axis[0,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[1,0].hist(pathLen.loc[lambda x : x > quant_pathLen], alpha=0.8, edgecolor = "black")
axis[1,0].set_title("Path Length 2018")
#axis[1,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')
print(n2, bins2, patches)

print('Data')
(n2, bins2, patches) =  axis[1,1].hist(queryLen.loc[lambda x : x > quant_queryLen], alpha=0.8, edgecolor = "black")
axis[1,1].set_title("Query Length 2018")
#axis[1,1].tick_params(axis='x', labelsize = 'xx-small')
print(n2, bins2, patches)





