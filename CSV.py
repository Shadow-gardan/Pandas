import pandas as pd
df = pd.read.csv("Path of csv file", index_col = "Student")
print(df)
print("Head of csv file\n",df.head(3))
print("tail of csv file\n",df.tail(3))

res = df["Marks"]
print(res)
print(de.loc["ZAX"])
print(de.iloc[2])