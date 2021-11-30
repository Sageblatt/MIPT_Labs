import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("flights.csv")

fig, axes = plt.subplots(ncols=3, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

names = ['Flights amount', "Total price", "Total weight"]

df.groupby('CARGO').count()['Unnamed: 0'].plot(kind='bar', ax=axes[0], title=names[0], xlabel='')
df.groupby('CARGO').sum()['PRICE'].plot(kind='bar', ax=axes[1], title=names[1], xlabel='')
df.groupby('CARGO').sum()['WEIGHT'].plot(kind='bar', ax=axes[2], title=names[2], xlabel='')

plt.savefig("output.png")
# plt.show()
