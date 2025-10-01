import pandas as pd

data = {
    "student" : ["Zax","Dax","Tax","Rax","Max"],
    "Subject" : ["Hindi","SST","Math","English","Science"],
    "Marks" : [89,78,56,98,78]
}

df = pd.DataFrame(data)
print(df)
print("\nPrint the two Column\n",df[["Subject","Marks"]])
print("\nPrint the Column in range\n",df.columns[1:3])

# Insert Roll column
df.insert(loc=2, column="Roll", value=[1,2,3,4,5])

print("\nDataFrame after inserting Roll column:\n", df)

# Using assign to add a Roll column (alternative way)
resdf = df.assign(Roll=[1,2,3,4,5])

print("\nDataFrame created with assign:\n", resdf)

df = pd.DataFrame(data)
print(df)

# Drop column
print("\ndelete the column:\n", df.drop("Marks", axis=1))

# Drop row by index (e.g., row 0)
print("\ndelete row at index 0:\n", df.drop(0, axis="index"))

# Drop row where Marks == 89
print("\ndelete row where Marks = 89:\n", df[df["Marks"] != 89])

print("To display the row one by one using the iterrow method\n")
for row in df.iterrows():
    print(row,"\n")
    
print("To DIsplay the row one by one using the itertuples method\n")
for row in df.itertuples():
    print(row)


print("Itreate with each column")

for col_name, col_data in df.items():
    print(f"Column name: {col_name}")
    print(col_data)
    print()