import pandas as pd

# out = open('output.txt', 'w', encoding='utf-8')
df = pd.read_csv("transactions.csv")

df_ok = df[df['STATUS'] == 'OK']
del df

biggest = df_ok['SUM'].nlargest(3).to_dict()
print("TOP THREE PAYMENTS:")
# out.write("TOP THREE PAYMENTS:\n")
[print(df_ok.loc[i, :].to_string(), "\n") for i in biggest]
# [out.write(df_ok.loc[i, :].to_string() + '\n\n') for i in biggest]

print("--------------------------------\n")
# out.write("--------------------------------\n")

umb = df_ok[df_ok["CONTRACTOR"] == "Umbrella, Inc"]

del df_ok
print("UMBRELLA, INC INCOME:", umb["SUM"].sum())
# out.write("UMBRELLA, INC INCOME: " + str(umb["SUM"].sum()))
# out.close()
