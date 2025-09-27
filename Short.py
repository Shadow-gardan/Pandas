import pandas as pd

data = {
    "student" : ["Zax","Dax","Tax","Rax","Max"],
    "Subject" : ["Hindi","SST","Math","English","Science"],
    "Marks" : [89,78,56,98,78]
}

df = pd.DataFrame(data, index = ["A","B","C","D","E"])

print("Short the table in ascending\n",df.sort_values(by = ["Marks"]),"\n")
print("Short the table descending\n",df.sort_values(by = ["Marks"],ascending = False))