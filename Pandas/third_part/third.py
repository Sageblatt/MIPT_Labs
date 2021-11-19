import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_excel("students_info.xlsx")
df1 = df1[df1['login'].notna()]

names = [df1['group_faculty'].unique(), np.sort(df1['group_out'].unique())]

df2 = pd.read_html("results_ejudge.html")[0].rename(columns={'User': 'login'})

df = pd.merge(df2, df1, on='login')
del df1, df2

f_stat = df.groupby('group_faculty').mean()['Solved'].to_list()
o_stat = df.groupby('group_out').mean()['Solved'].to_list()

data = [f_stat, o_stat]

fig, axes = plt.subplots(ncols=2, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

for i in range(2):
    axes[i].bar([i for i in range(7)], height=[data[i][k] for k in range(7)])
    axes[i].set_xticks([i for i in range(7)])
    axes[i].set_xticklabels((k for k in names[i]))

axes[0].set_title("Фак. группы")
axes[1].set_title("Инф. группы")
fig.suptitle("Распределение среднего числа задач по группам")

plt.savefig("output.png")
# plt.show()

geniuses = df[(df['G'] > 10) | (df['H'] > 10)]
g_fs = geniuses['group_faculty'].unique()
g_os = geniuses['group_out'].unique()

print("Фак. группы: ", sorted(g_fs))
print("Инф. группы: ", g_os)

# df.to_excel("1.xlsx") # для ручной проверки результаттов с помощью экселя
