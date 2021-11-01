import math
import pandas as pd
import matplotlib.pyplot as plt


preps_mean = []
groups_mean = []
colour_map = {str(i): ("C" + str(i)) for i in range(11)}

df = pd.read_csv("students.csv", names=['prep', 'group', 'mark'], sep=";")
preps = df[['prep', 'mark']]
groups = df[['group', 'mark']]
del df

# preps chart
preps_names = preps['prep'].unique()
columns = 3
strings = math.ceil(len(preps_names) / columns)
fig, axes = plt.subplots(ncols=columns, nrows=strings, gridspec_kw={"wspace": 0.2, "hspace": 0.3})

for i, p in enumerate(preps_names):
    a1, a2 = i // columns, i % columns
    if i == len(preps_names) - 1:
        a2 = 1
    d = dict(preps[preps['prep'] == p].value_counts())
    total = len(preps.loc[preps['prep'] == p, 'mark'])
    marks_sum = preps[preps['prep'] == p]['mark'].sum()
    preps_mean.append([p, marks_sum/total])
    labels = [str(s[1]) for s in d.keys()]
    values = [s for s in d.values()]
    axes[a1, a2].pie(values, labels=labels, colors=[colour_map[key] for key in labels],
                     autopct=lambda y: f'{int(y/100*total)}', textprops={'size': 'smaller'})
    axes[a1, a2].set_title(p)

fig.delaxes(axes[2, 0])
fig.delaxes(axes[2, 2])

pM = max(preps_mean, key=lambda y: y[1])
pm = min(preps_mean, key=lambda y: y[1])
fig.suptitle(f'The most strict teacher is {pm[0]}, the least strict one is {pM[0]}')

plt.savefig("preps.png", bbox_inches='tight')

del fig, axes, columns, strings

# groups chart
groups_names = groups['group'].unique()
columns = 3
strings = math.ceil(len(groups_names) / columns)
fig, axes = plt.subplots(ncols=columns, nrows=strings, gridspec_kw={"wspace": 0.2, "hspace": 0.3})


for i, p in enumerate(sorted(groups_names)):
    a1, a2 = i // columns, i % columns
    d = dict(groups[groups['group'] == p].value_counts())
    total = len(groups.loc[groups['group'] == p, 'mark'])
    marks_sum = groups[groups['group'] == p]['mark'].sum()
    groups_mean.append([p, marks_sum/total])
    labels = [str(s[1]) for s in d.keys()]
    values = [s for s in d.values()]
    axes[a1, a2].pie(values, labels=labels, colors=[colour_map[key] for key in labels],
                     autopct=lambda y: f'{int(y/100*total)}', textprops={'size': 'smaller'})
    axes[a1, a2].set_title(p)

pM = max(groups_mean, key=lambda y: y[1])
pm = min(groups_mean, key=lambda y: y[1])
fig.suptitle(f'The most intelligent groups are 752 and 755 , the least intelligent one is {pm[0]}')

plt.savefig("groups.png", bbox_inches='tight')
plt.close()
# plt.show()
