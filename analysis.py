import pandas as pd

# Load the dataset
data = pd.read_csv("student_performance.csv")

# Display basic information
print("Student Performance Analysis")
print("=" * 35)

print("\nDataset:")
print(data)

print("\nAverage Performance:")
print("-" * 35)

print("Average Study Hours:",
      round(data["Study_Hours"].mean(), 2))

print("Average Attendance:",
      round(data["Attendance"].mean(), 2), "%")

print("Average Previous Score:",
      round(data["Previous_Score"].mean(), 2))

print("Average Final Score:",
      round(data["Final_Score"].mean(), 2))

# Find highest performing student
highest = data.loc[data["Final_Score"].idxmax()]

print("\nHighest Performing Student:")
print("-" * 35)
print(highest)

# Find lowest performing student
lowest = data.loc[data["Final_Score"].idxmin()]

print("\nLowest Performing Student:")
print("-" * 35)
print(lowest)

# Correlation analysis
print("\nCorrelation with Final Score:")
print("-" * 35)

print(data[
    ["Study_Hours", "Attendance", "Previous_Score", "Final_Score"]
].corr()["Final_Score"])