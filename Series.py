import numpy as np
import pandas as pd

sere =["qw","er","rt","yu","io"]

sd = pd.Series(sere)
print("Series \n",sd)
print("access Series 2 \n",sd[2])

rs = pd.Series(sere, index=[1,2,3,4,5])
print("Series with custom index \n", rs)

se = ["wq","er","ty","ui","op",np.nan]
dt2 = pd.Series(se, index = [1,2,3,4,5,6],name = "pratice")
print("Sereies\n",dt2,"\n")
print("Data type of serie",dt2.dtype)
print("Series Dimension",dt2.ndim)
print("Size of the series",dt2.size)
print("Series name",dt2.name)
print("Hasnans of Series",dt2.hasnans)
print("Index of series",dt2.index)
print("Two row of series\n",dt2.head(3))
print("Use the Tail method\n",dt2.tail(3))
print("Series information\n",dt2.info())
se1 = [1,2,3,4,5]
se2 = [6,7,8,9,10]
s1 = pd.Series(se1)
s2 = pd.Series(se2)

def damo(x1,x2):
    if(x1 > x2):
        return x1
    else :
        return x2

com = s1.combine(s2 ,damo)

print("Combine two sereies\n",com)
