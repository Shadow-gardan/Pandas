import numpy as np
import pandas as pd


data = {
    "Student" : ["max","Rax","zax"],
    "rank" : [1,2,3],
    "Marks" : [99,97,97]
}

df = pd.DataFrame(data)
print("\n\n",df)

print(df)
print("\nDisplay the column using for loop")
for col in df:
    print(col)

print("\nTo find the data type")    
print(df.dtypes)

print("\n To find the number of Dimensions",df.ndim)

print("\n to find the Size of Data Frame",df.size)

print("\n to find the Shape of Data Frame",df.shape)

print("\n To find the index of Data Frame",df.index)

print("\n To find the column names of Data Frame",df.columns)

print("To print the specefic data"df.tail(3))

data1 ={
    "roll" : [1,2,3,4,5],
    "addres" : ["asd","khg","qwe","wrr","gfd"]
}

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data1)

data2 = df1.join(df2)

print("To join the 2 data",data2)

data2 ={
    "roll" : [6,7,8,9,10,],
    "addres" : ["asd","khg","qwe","wrr","gfd"]
}

df3 = pd.DataFrame(data1)
df4 = pd.DataFrame(data2)

data3 = pd.concat([df1,df2])

print("Concatenating data frame",data3)

