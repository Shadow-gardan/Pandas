import pandas as pd

data =["Tiger","\tElephant\n","\tCat\t","\nDog\n","\nFox\t"]

dt = pd.Series(data)
print("Series \n",dt)
print("White space and specific character from both side \n",dt.str.strip("!\n\t"))
print("White space and specific character from left side only\n",dt.str.lstrip("!\n\t"))
print("White space and specific character from right side only\n",dt.str.rstrip("!\n\t"))