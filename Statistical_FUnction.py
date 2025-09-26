import pandas as pd

# Creating a dictionary with 3 keys (student, Subject, Marks)
# Each key has a list of values, including some missing values (None)
data = {
    "Hindi" : [77,66,88,55,None],
    "English" : [87,None,98,23,46],
    "Math" : [97,45,54,None,85]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Data frame\n", df)

# Sum of each column (ignores NaN/None by default)
print("\nSum of data frame\n", df.sum())

# Count of non-missing values in each column
print("\nCount the data frame\n", df.count())

# Maximum value in each column
print("\nMax of data frame\n", df.max())

# Minimum value in each column
print("\nMinimum of data frame\n", df.min())

# Mean (average) of each column (ignores NaN/None)
print("\nMean of the values\n", df.mean())

# Median (middle value) of each column
print("\nMedian of the values\n", df.median())

# Standard deviation (spread of data) of each column
print("\nStandard Deviation of the values\n", df.std())

# Statistical summary of each column:
# count, mean, std, min, 25%, 50%, 75%, max
print("\nDescribe the values\n", df.describe())
