import pandas as pd
cs = pd.Series(data = ["a","s","d","f","g",],dtype = "category")
print("Category Series\n",cs)

cf = pd.Series(data={"cat": "Animal", "Dog": "Animal", "Han": "Bird"}, dtype="category")
print("\nCategorical Dictionary Series\n", cf)
print("\nCategorical Dictionary Series data type\n", cf.dtype)

cs = cs.cat.add_categories("t")
print("add category in old category\n",cs)

cs = cs.cat.remove_categories("s")
print("remove category in old category\n",cs)