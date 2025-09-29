import pandas as pd
df = pd.read_excel("Path fo the file")
print(df)
print("Head of csv file\n",df.head(3))
print("tail of csv file\n",df.tail(3))