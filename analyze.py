import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("engagement_data.csv")  # Make sure file name matches your CSV

# Clean data
df.dropna(inplace=True)

# Match columns by partial name (case-insensitive)
def find_column(possible_names):
    for col in df.columns:
        for name in possible_names:
            if name.lower() in col.lower():
                return col
    return None

course_col = find_column(["course", "module"])
completion_col = find_column(["completion", "complete", "pass"])

# Calculate average completion
avg_completion = df[completion_col].mean()
print(f"Average Completion Rate: {avg_completion:.2f}%")

# Find most popular course
popular_course = df[course_col].value_counts().idxmax()
print(f"Most Popular Course: {popular_course}")

# Visualization
df.groupby(course_col)[completion_col].mean().plot(kind='bar')
plt.title("Completion Rate by Course")
plt.xlabel("Course Name")
plt.ylabel("Completion Rate (%)")
plt.tight_layout()
plt.show()
