from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec
import numpy as np
import glob
import os

li_avg = []
li_hist = []
li_count_08 = []
li_count_rest = []

columns = ['urlLen', 'authorityLen', 'pathLen', 'queryLen']
csv_files = glob.glob("2019-35/year-month/*.tsv")
csv_files.sort()

for file in csv_files:
 data = pd.read_csv(file, sep='\t', header=None, names=columns)
 avg = data.mean()
 lm  = datetime.strptime(os.path.splitext(os.path.basename(file))[0], '%Y-%m')
 avg['epoch'] = lm
 if lm.month == 8:
  count_08 = {}
  count_08['epoch'] = lm
  count_08['count'] = data.shape[0]
  li_count_08.append(count_08)
 else:
  count_rest = {}
  count_rest['epoch'] = lm
  count_rest['count'] = data.shape[0]
  li_count_rest.append(count_rest)
 avg['count'] = data.shape[0]
 li_avg.append(avg)
 if lm.year == 2018:
  li_hist.append(data)

df_avg = pd.DataFrame(li_avg)
df_count_08 = pd.DataFrame(li_count_08)
df_count_rest = pd.DataFrame(li_count_rest)
df_count_rest = df_count_rest.resample('M', on='epoch').sum().reset_index()
df_hist = pd.concat(li_hist, axis=0)
df_hist.astype('int')

df_avg.to_csv('result/Average.csv', index=False)
df_count_08.to_csv('result/Count-Aug.csv', index=False)
df_count_rest.to_csv('result/Count-rest.csv', index=False)

half_year_locator = mdates.MonthLocator(interval=6)
year_month_formatter = mdates.DateFormatter("%Y-%m")

############################ Count #########################################
fig = plt.figure(figsize=(10,8))
gs = gridspec.GridSpec(2,2)
year_locator = mdates.YearLocator(1)
year_formatter = mdates.DateFormatter("%Y")

ax1=fig.add_subplot(gs[0,0])
ax1.xaxis.set_major_locator(year_locator)
ax1.xaxis.set_major_formatter(year_formatter)
ax1.plot(df_count_08.epoch, df_count_08['count'])
ax1.tick_params(axis='x', rotation=90, labelsize = 'xx-small')
ax1.set(xlabel="Year", ylabel="URL count")
ax1.set_title("Number of URL each Aug")

ax2=fig.add_subplot(gs[0,1])
ax2.xaxis.set_major_locator(year_locator)
ax2.xaxis.set_major_formatter(year_formatter)
ax2.plot(df_count_rest['epoch'], df_count_rest['count'])
ax2.tick_params(axis='x', rotation=90, labelsize = 'xx-small')
ax2.set(xlabel="Year", ylabel="URL count")
ax2.set_title("Number of URL each month excluding Aug")

ax3=fig.add_subplot(gs[1,:])
ax3.xaxis.set_major_locator(half_year_locator)
ax3.xaxis.set_major_formatter(year_month_formatter)
ax3.plot(df_avg.epoch, df_avg['count'])
ax3.tick_params(axis='x', rotation=90, labelsize = 'xx-small')
ax3.set(xlabel="Year-month", ylabel="URL count")
ax3.set_title("Number of URL in each month")

plt.tight_layout()
plt.savefig('result/count.jpeg', dpi=500)

##################### Histogram 2018 #####################################

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

axis[0,0].hist(urlLen.loc[lambda x : x < quant_urlLen], alpha=0.8, edgecolor = "black")
axis[0,0].set_title("URL Length 2018")
#axis[0,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[0,1].hist(authorityLen.loc[lambda x : x < quant_authorityLen], alpha=0.8, edgecolor = "black")
axis[0,1].set_title("Authority Length 2018")
#axis[0,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[1,0].hist(pathLen.loc[lambda x : x < quant_pathLen], alpha=0.8, edgecolor = "black")
axis[1,0].set_title("Path Length 2018")
#axis[1,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[1,1].hist(queryLen.loc[lambda x : x < quant_queryLen], alpha=0.8, edgecolor = "black")
axis[1,1].set_title("Query Length 2018")
#axis[1,1].tick_params(axis='x', labelsize = 'xx-small')

plt.tight_layout()
plt.savefig('result/hist.jpeg', dpi=500)

###########################
figure, axis = plt.subplots(2, 2, figsize=(16,8))

axis[0,0].hist(urlLen.loc[lambda x : x > quant_urlLen], alpha=0.8, edgecolor = "black")
axis[0,0].set_title("URL Length 2018")
#axis[0,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[0,1].hist(authorityLen.loc[lambda x : x > quant_authorityLen], alpha=0.8, edgecolor = "black")
axis[0,1].set_title("Authority Length 2018")
#axis[0,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[1,0].hist(pathLen.loc[lambda x : x > quant_pathLen], alpha=0.8, edgecolor = "black")
axis[1,0].set_title("Path Length 2018")
#axis[1,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')


axis[1,1].hist(queryLen.loc[lambda x : x > quant_queryLen], alpha=0.8, edgecolor = "black")
axis[1,1].set_title("Query Length 2018")
#axis[1,1].tick_params(axis='x', labelsize = 'xx-small')
plt.tight_layout()
plt.savefig('result/outliers.jpeg', dpi=500)

############## Averages ##################################
figure, axis = plt.subplots(2, 2, figsize=(16,8))

axis[0,0].xaxis.set_major_locator(half_year_locator)
axis[0,0].xaxis.set_major_formatter(year_month_formatter)
axis[0,0].plot(df_avg.epoch, df_avg.urlLen)
axis[0,0].set_title("URL avg Length")
axis[0,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')

axis[0,1].xaxis.set_major_locator(half_year_locator)
axis[0,1].xaxis.set_major_formatter(year_month_formatter)
axis[0,1].plot(df_avg.epoch, df_avg.authorityLen, label="Authority")
axis[0,1].set_title("Authority avg Length")
axis[0,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')

axis[1,0].xaxis.set_major_locator(half_year_locator)
axis[1,0].xaxis.set_major_formatter(year_month_formatter)
axis[1,0].plot(df_avg.epoch, df_avg.pathLen, label="Path")
axis[1,0].set_title("Path avg Length")
axis[1,0].tick_params(axis='x', rotation=90, labelsize = 'xx-small')

axis[1,1].xaxis.set_major_locator(half_year_locator)
axis[1,1].xaxis.set_major_formatter(year_month_formatter)
axis[1,1].plot(df_avg.epoch, df_avg.queryLen, label="query")
axis[1,1].set_title("Query avg Length")
axis[1,1].tick_params(axis='x', rotation=90, labelsize = 'xx-small')

plt.tight_layout()
plt.savefig('result/avg.jpeg', dpi=500)

df_avg = df_avg.drop(['count', 'urlLen'], axis=1)
df_avg['epoch'] = df_avg['epoch'].dt.strftime('%Y-%m')
df_avg.plot(x='epoch', kind='bar', stacked=True, figsize=(16, 8), title='Length Averages of URL Components each month', xlabel='year-month', ylabel='URL Length')
plt.xticks(rotation=90, fontsize = 'xx-small')
plt.locator_params(axis='x', nbins=50)
plt.tight_layout()
plt.savefig('result/stacked.jpeg', dpi=500)

