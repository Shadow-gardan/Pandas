import pandas as pd
import matplotlib.pyplot as plt   # Import matplotlib for plotting

# Create sample data with some missing values (None = NaN in pandas)
data = {
    "Hindi" : [77, 66, 88, 55, None],
    "English" : [87, None, 98, 23, 46],
    "Math" : [97, 45, 54, None, 85]
}

# Create DataFrame with custom index (student names)
df = pd.DataFrame(data, index=["Sam", "Dam", "Ess", "Fax", "Opp"])

# Plot all numeric columns together (default line plot)
df.plot()

# Plot histogram for Hindi marks
df["Hindi"].plot(kind="hist")

# Plot pie chart for English marks
df.plot.pie(y="English")

# Plot scatter plot between Hindi and Math (fixed typo: "Mayh" → "Math")
df.plot(kind="scatter", x="Hindi", y="Math")

# Show all plots
plt.show()
