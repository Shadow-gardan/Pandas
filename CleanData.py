import pandas as pd

df = pd.read_csv("CSV file name")
print("Data Frame\n",df)
res1 = df.isnull()
print("Find the NULL value",res1.to.tring())
res2 = df.notnull()
print("To change NULL to true or false",res2.to.tring())
res3 = df.dropna()
print("Remove rows with NULL value",res3.to.tring())
res4 = df.fillna(111)
print("Replace the NULL value with the specific value",res4.to.tring())