import pandas as pd
import matplotlib.pyplot as plt

names = ["Фак. группы", "Инф. группы"]
df1 = pd.read_excel("students_info.xlsx")
df2 = pd.read_html("results_ejudge.html")[0].rename(columns={'User': 'login'})

df = pd.merge(df2, df1, on='login')
del df1, df2

fig, axes = plt.subplots(ncols=2, nrows=1, gridspec_kw={"wspace": 0.8}, figsize=[11, 8])

df.groupby('group_faculty').mean()['Solved'].plot(kind='bar', ax=axes[0], title=names[0], xlabel='')
df.groupby('group_out').mean()['Solved'].plot(kind='bar', ax=axes[1], title=names[1], xlabel='')

fig.suptitle("Распределение среднего числа задач по группам")

plt.savefig("output.png")
# plt.show()

geniuses = df[(df['G'] > 10) | (df['H'] > 10)]
g_fs = geniuses['group_faculty'].unique()
g_os = geniuses['group_out'].unique()

print("Фак. группы: ", sorted(g_fs))
print("Инф. группы: ", g_os)

# df.to_excel("1.xlsx") # для ручной проверки результатов с помощью экселя
