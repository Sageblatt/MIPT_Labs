import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")

names = np.sort(df['CARGO'].unique())

fig, axes = plt.subplots(ncols=3, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

data = [[], [], []]

data[0] = df.groupby('CARGO').count()['Unnamed: 0'].to_list()
data[1] = df.groupby('CARGO').sum()['PRICE'].to_list()
data[2] = df.groupby('CARGO').sum()['WEIGHT'].to_list()

del df

for i in range(3):
    axes[i].bar([0, 1, 2], height=[data[i][k] for k in range(3)])
    axes[i].set_xticks([0, 1, 2])
    axes[i].set_xticklabels((p for p in names))

axes[0].set_title("Flights amount")
axes[1].set_title("Total price")
axes[2].set_title("Total weight")

plt.savefig("output.png")
# plt.show()
