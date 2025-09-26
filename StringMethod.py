import pandas as pd

sere = ["Rax","Eax","Hax","Tax","max","resw","uytr"]

sd = pd.Series(sere)
print("Series \n", sd)

print("\nPrint the data in lower-case \n", sd.str.lower())
print("\nPrint the data in Upper-case \n", sd.str.upper())
print("\nPrint the data in Camel-case \n", sd.str.title())
print("\nLength Of data \n", sd.str.len())
print("\nCount Of data \n", sd.count())
print("\nTo find the specific data \n", sd.str.contains("Tax"))