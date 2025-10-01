
import pandas as pd
import numpy as np

# ============================================================================
# PANDAS ROWS AND COLUMNS CONCEPT STUDY
# ============================================================================

print("=== PANDAS ROWS AND COLUMNS CONCEPT ===\n")

# ============================================================================
# 1. CREATING A DATAFRAME - UNDERSTANDING STRUCTURE
# ============================================================================

# Create sample data for demonstration
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Salary': [50000, 60000, 70000, 55000, 65000]
}

# Create DataFrame - think of it as a table with rows and columns
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print(f"\nDataFrame shape: {df.shape}")  # (rows, columns)
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\n" + "="*50 + "\n")

# ============================================================================
# 2. UNDERSTANDING ROWS (HORIZONTAL DATA)
# ============================================================================

print("=== WORKING WITH ROWS ===\n")

# Each row represents a complete record/observation
# Rows are indexed starting from 0 (unless specified otherwise)

# Accessing single row by index using .iloc (integer location)
print("First row (index 0) using .iloc:")
first_row = df.iloc[0]  # Returns a Series
print(first_row)
print(f"Type: {type(first_row)}\n")

# Accessing single row by label using .loc (label location)
print("First row (index 0) using .loc:")
first_row_loc = df.loc[0]  # Returns a Series
print(first_row_loc)
print("\n")

# Accessing multiple rows
print("First three rows using .iloc:")
first_three_rows = df.iloc[0:3]  # Returns a DataFrame
print(first_three_rows)
print(f"Type: {type(first_three_rows)}\n")

# Accessing rows by condition (boolean indexing)
print("Rows where Age > 30:")
older_people = df[df['Age'] > 30]  # Boolean indexing
print(older_people)
print("\n")

# Getting row information
print("Row index labels:")
print(df.index.tolist())
print(f"Total number of rows: {len(df)}")
print("\n" + "="*50 + "\n")

# ============================================================================
# 3. UNDERSTANDING COLUMNS (VERTICAL DATA)
# ============================================================================

print("=== WORKING WITH COLUMNS ===\n")

# Each column represents a feature/attribute
# Columns have names (labels) and contain data of usually the same type

# Accessing single column - returns a Series
print("Accessing 'Name' column:")
names = df['Name']  # Method 1: bracket notation
print(names)
print(f"Type: {type(names)}\n")

# Alternative way to access column (only works if column name is valid Python identifier)
ages = df.Age  # Method 2: dot notation
print("Accessing 'Age' column using dot notation:")
print(ages)
print("\n")

# Accessing multiple columns - returns a DataFrame
print("Accessing multiple columns ['Name', 'Age']:")
name_age = df[['Name', 'Age']]  # Note: double brackets for multiple columns
print(name_age)
print(f"Type: {type(name_age)}\n")

# Getting column information
print("Column names:")
print(df.columns.tolist())
print(f"Number of columns: {len(df.columns)}")
print("\n")

# Column data types
print("Column data types:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# ============================================================================
# 4. ADDING AND REMOVING ROWS AND COLUMNS
# ============================================================================

print("=== ADDING AND REMOVING ROWS AND COLUMNS ===\n")

# Adding a new column
print("Adding a new column 'Department':")
df['Department'] = ['IT', 'Finance', 'HR', 'Marketing', 'IT']
print(df)
print("\n")

# Adding a calculated column
print("Adding calculated column 'Annual_Bonus' (10% of salary):")
df['Annual_Bonus'] = df['Salary'] * 0.10
print(df)
print("\n")

# Adding a new row using .loc
print("Adding a new row:")
df.loc[5] = ['Frank', 29, 'Berlin', 58000, 'Sales', 5800.0]
print(df)
print("\n")

# Removing a column
print("Removing 'Annual_Bonus' column:")
df_without_bonus = df.drop('Annual_Bonus', axis=1)  # axis=1 means column
print(df_without_bonus)
print("\n")

# Removing a row
print("Removing row at index 5:")
df_without_last = df.drop(5, axis=0)  # axis=0 means row
print(df_without_last)
print("\n" + "="*50 + "\n")

# ============================================================================
# 5. SELECTING SPECIFIC CELLS (ROW + COLUMN INTERSECTION)
# ============================================================================

print("=== SELECTING SPECIFIC CELLS ===\n")

# Selecting a specific cell using .loc[row, column]
print("Value at row 0, column 'Name':")
cell_value = df.loc[0, 'Name']
print(cell_value)
print("\n")

# Selecting a specific cell using .iloc[row_index, column_index]
print("Value at row 1, column 2 (using integer positions):")
cell_value_iloc = df.iloc[1, 2]
print(cell_value_iloc)
print("\n")

# Selecting multiple cells
print("Values at rows 0-2, columns 'Name' and 'Age':")
multiple_cells = df.loc[0:2, ['Name', 'Age']]
print(multiple_cells)
print("\n" + "="*50 + "\n")

# ============================================================================
# 6. ITERATING THROUGH ROWS AND COLUMNS
# ============================================================================

print("=== ITERATING THROUGH ROWS AND COLUMNS ===\n")

# Iterating through rows
print("Iterating through rows using .iterrows():")
for index, row in df.head(3).iterrows():  # Using head(3) to limit output
    print(f"Row {index}: {row['Name']} is {row['Age']} years old")
print("\n")

# Iterating through columns
print("Iterating through columns:")
for column_name in df.columns:
    print(f"Column: {column_name}")
    print(f"First value: {df[column_name].iloc[0]}")
    print("---")
print("\n" + "="*50 + "\n")

# ============================================================================
# 7. ROW AND COLUMN OPERATIONS
# ============================================================================

print("=== ROW AND COLUMN OPERATIONS ===\n")

# Column statistics
print("Column statistics for 'Age':")
print(f"Mean age: {df['Age'].mean()}")
print(f"Max age: {df['Age'].max()}")
print(f"Min age: {df['Age'].min()}")
print("\n")

# Row operations - calculating across columns
print("Adding a row sum example (Age + Salary for demonstration):")
df['Age_Salary_Sum'] = df['Age'] + df['Salary']
print(df[['Name', 'Age', 'Salary', 'Age_Salary_Sum']].head(3))
print("\n")

# Filtering rows based on column conditions
print("Filtering: People from IT department:")
it_people = df[df['Department'] == 'IT']
print(it_people[['Name', 'Department', 'Salary']])
print("\n")

# Sorting by column
print("Sorting by Age (ascending):")
sorted_by_age = df.sort_values('Age')
print(sorted_by_age[['Name', 'Age']].head())
print("\n" + "="*50 + "\n")

# ============================================================================
# 8. KEY CONCEPTS SUMMARY
# ============================================================================

print("=== KEY CONCEPTS SUMMARY ===\n")

print("""
ROWS (Horizontal):
- Represent individual records/observations
- Indexed by numbers (0, 1, 2, ...) or custom labels
- Access with .iloc[row_number] or .loc[row_label]
- Each row contains values across all columns

COLUMNS (Vertical):
- Represent features/attributes/variables
- Named with string labels
- Access with df['column_name'] or df.column_name
- Each column contains values of usually the same data type

DATAFRAME STRUCTURE:
- 2D structure with rows and columns
- Think of it as a spreadsheet or database table
- Shape is (number_of_rows, number_of_columns)
- Can be sliced, filtered, and manipulated

SELECTION METHODS:
- df[column] → Select column (returns Series)
- df[[col1, col2]] → Select multiple columns (returns DataFrame)
- df.iloc[row] → Select row by position (returns Series)
- df.loc[row, col] → Select specific cell by label
- df.iloc[row, col] → Select specific cell by position
""")

print("Final DataFrame shape:", df.shape)
print("Final DataFrame columns:", df.columns.tolist())