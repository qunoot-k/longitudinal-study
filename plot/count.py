import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec
import numpy as np
import glob
import os

li_count = []

data_2019 = glob.glob("2019-35/merge*/*.tsv")
csv_files = glob.glob("2019-35/year**/*.tsv")
csv_files.sort()

li_2019 = []
for file in data_2019:
 data = pd.read_csv(file, sep='\t', header=None, usecols=[5], names=['epoch'])
 data = data[(data["epoch"] >= 1564617600) & (data["epoch"] < 1567296000)]
 data['epoch'] = pd.to_datetime(data['epoch'], unit='s')
 li_2019.append(data)

df = pd.concat(li_2019, axis=0)
df = df['epoch'].dt.date.value_counts().sort_index().reset_index()
df.columns = ['epoch','count']
li_2019 = []

data = pd.read_csv("result/Average.csv",  usecols=['epoch', 'count'])
data['epoch'] = pd.to_datetime(data['epoch'])
data_other = data[data["epoch"].dt.year != 2019]

df.to_csv('result/August_count.csv', index=False)

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
ax1.plot(data_other.epoch, data_other['count'])
ax1.tick_params(axis='x', rotation=90, labelsize = 'xx-small')
ax1.set(xlabel="Year", ylabel="URL count")
ax1.set_title("Count of URL each month before August 2019")

ax2=fig.add_subplot(gs[0,1])
ax2.xaxis.set_major_locator(mdates.DayLocator(interval=2))
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
ax2.plot(df['epoch'], df['count'])
ax2.set(xlabel="Day Aug 2019", ylabel="URL count")
ax2.set_title("Count of URL in Aug 2019")

ax3=fig.add_subplot(gs[1,:])
ax3.xaxis.set_major_locator(half_year_locator)
ax3.xaxis.set_major_formatter(year_month_formatter)
ax3.plot(data.epoch, data['count'])
ax3.tick_params(axis='x', rotation=90, labelsize = 'small')
ax3.set(xlabel="Year-month", ylabel="URL count")
ax3.set_title("Count of URL each month")

plt.tight_layout()
plt.savefig('result/count.jpeg', dpi=500)






