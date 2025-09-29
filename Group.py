import pandas as pd
import numpy as np

data = {
    "Player": ["Zax", "Dax", "Tax", "Rax", "Max"],
    "Point": [90, 98, 99, 97, 96],
    "Rank": [1, 2, 3, 4, 5],
    "Marks": [89, 78, 56, 98, 78]
}

df = pd.DataFrame(data)
print("Data Frame:\n", df)

# Group by Player
rs = df.groupby('Player')
print("\nSplit the object:\n", rs.first())

for name, group in rs:
    print(f"\n{name}")
    print(group)

print("\nView the groups:\n", rs.groups)

# Group by Rank and compute mean of Points
gr = df.groupby('Rank')
print("\nMean of Points by Rank:\n", gr['Point'].mean())

print("Size attribute \n",rs.agg(np.size))