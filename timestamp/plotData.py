import os
import matplotlib.pyplot as plt
import pandas as pd


directory="/work/dc007/dc007/qunoot/2019-35/tim*/0"

plt.figure(figsize=(8,6), dpi=100, frameon=True, clear=False)
plt.axis([-20000, 20000, -0.3, 0.3])

for filename in os.listdir(directory):
 data = pd.read_csv(filename, sep='\t', header=None)
 # data = pd.DataFrame(data) # This step is redundant
 plt.plot(data[5], data[1])

plt.axvline(x=0, color="black", linestyle='-')
plt.axhline(y=0, color="black", linestyle='-')

plt.title("URL Length over Last-modified date")
plt.xlabel("Date (epoch)")
plt.ylabel("URL Length")
# Rest of the code
plt.show() 


