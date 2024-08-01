from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.gridspec as gridspec
import numpy as np
import glob
import os

li_avg = []

csv_files = glob.glob("2019-35/year-month/*.tsv")
csv_files.sort()

for file in csv_files:
 data = pd.read_csv(file, sep='\t', header=None, usecols=[3], names=['queryLen'])
 data = data[data['queryLen'] != 0]
 avg = data.mean()
 lm  = datetime.strptime(os.path.splitext(os.path.basename(file))[0], '%Y-%m')
 avg['epoch'] = lm
 avg['count'] = data.shape[0]
 if avg['count'] == 0:
  avg['queryLen'] = 0
 print(lm)
 print(data.describe())
 li_avg.append(avg)

df_avg = pd.DataFrame(li_avg)


df_avg.to_csv('result/Average_query.csv', index=False)


############## Averages ##################################

half_year_locator = mdates.MonthLocator(interval=6)
year_month_formatter = mdates.DateFormatter("%Y-%m")

ax = plt.axes()
ax.xaxis.set_major_locator(half_year_locator)
ax.xaxis.set_major_formatter(year_month_formatter)
plt.plot(df_avg.epoch, df_avg.queryLen)
plt.xlabel('Year-Month')
plt.ylabel('Query Length')
plt.title("Average Query Length over Time")
plt.xticks(rotation=90, fontsize = 'xx-small')
plt.tight_layout()
plt.savefig('result/avg_query.jpeg', dpi=500)

plt.show()

