import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")

names = df['CARGO'].unique()

fig, axes = plt.subplots(ncols=3, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

data = [[], [], []]
for p in names:
    data[0].append([df[df["CARGO"] == p].shape[0], p])
    data[1].append([int(df[df["CARGO"] == p]['PRICE'].sum()), p])
    data[2].append([int(df[df["CARGO"] == p]['WEIGHT'].sum()), p])

del df

for i in range(3):
    axes[i].bar([0, 1, 2], height=[data[i][k][0] for k in range(3)])
    axes[i].set_xticks([0, 1, 2])
    axes[i].set_xticklabels((k[1] for k in data[i]))

axes[0].set_title("Flights amount")
axes[1].set_title("Total price")
axes[2].set_title("Total weight")

plt.savefig("output.png")
# plt.show()
