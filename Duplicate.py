import pandas as pd

data = {
    "student" : ["Zax","Dax","Tax","Rax","Max"],
    "Subject" : ["Hindi","SST","Math","English","Science"],
    "Marks" : [89,78,56,98,78]
}

df = pd.DataFrame(data)
print(df, "\n")

# Show duplicated rows
print("Duplicate data:\n", df.duplicated())

# Remove duplicates
print("Delete the Duplicate data:\n", df.drop_duplicates())
