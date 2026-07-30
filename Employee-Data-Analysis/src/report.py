import pandas as pd

# Load Cleaned Dataset
df = pd.read_csv("output/cleaned_employees.csv")

# Create Report

report = {
    "Total Employees": [df.shape[0]],
    "Highest Salary": [df["Salary"].max()],
    "Lowest Salary": [df["Salary"].min()],
    "Average Salary": [df["Salary"].mean()],
    "Total Salary": [df["Salary"].sum()],
    "Median Salary": [df["Salary"].median()],
    "Average Experience": [df["Experience"].mean()],
    "Maximum Experience": [df["Experience"].max()],
    "Minimum Experience": [df["Experience"].min()],
    "Highest Performance Score": [df["PerformanceScore"].max()],
    "Lowest Performance Score": [df["PerformanceScore"].min()],
    "Average Performance Score": [df["PerformanceScore"].mean()]
}

# Convert Dictionary to DataFrame
report_df = pd.DataFrame(report)

# Save Report
report_df.to_csv("output/report.csv", index=False)

print("Report generated successfully.")
print(report_df)