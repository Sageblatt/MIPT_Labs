import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel("students_info.xlsx")
df1 = df1[df1['login'].notna()]
gr_f = df1['group_faculty'].unique()
gr_o = df1['group_out'].unique()

df2 = pd.read_html("results_ejudge.html")[0].rename(columns={'User': 'login'})

df = pd.merge(df2, df1, on='login')
del df1, df2

# print(df)

f_stat, o_stat = [], []
for i in gr_f:
    f_stat.append([i, df.loc[df['group_faculty'] == i, 'Solved'].sum() / df[df['group_faculty'] == i].shape[0]])

for i in gr_o:
    o_stat.append([i, df.loc[df['group_out'] == i, 'Solved'].sum() / df[df['group_out'] == i].shape[0]])

o_stat.sort()
data = [f_stat, o_stat]
# print(data)

fig, axes = plt.subplots(ncols=2, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

for i in range(2):
    axes[i].bar([i for i in range(7)], height=[data[i][k][1] for k in range(7)])
    axes[i].set_xticks([i for i in range(7)])
    axes[i].set_xticklabels((k[0] for k in data[i]))

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
