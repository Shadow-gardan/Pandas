import pandas as pd

# Current date and time
print("Current date or time:\n", pd.Timestamp.now())

# Create a specific timestamp
ts = pd.Timestamp(year=2045, month=10, day=10, hour=12)
print("\nDisplay the input time:", ts)

# Day of week (0=Monday, 6=Sunday)
print("\nDay of week (number):\n",ts.dayofweek)
print("\nDay of week (name):\n",ts.day_name())
print("\nDay of Year:\n", ts.dayofyear)
print("\nDay in month:\n", ts.daysinmonth)
print("\nIs leap year or not :\n", ts.is_leap_year)
print("\nIs This the month end :\n", ts.is_month_end)
print("\nIs This the month start :\n", ts.is_month_start)
print("\nIs This the year end :\n", ts.is_year_end)
print("\nIs This the year start :\n", ts.is_year_start)