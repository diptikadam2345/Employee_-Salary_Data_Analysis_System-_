import pandas as pd

df = pd.read_csv("data\employees.csv")

print("Employee Data:")
print(df)

# Remove Duplicate Rows

print("\nDuplicated rows before removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicated rows after removing:")
print(df.duplicated().sum())


# Handle Missing Values

# Fill numerical missing values with mean

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

df["Performance_Score"] = df["Performance_Score"].fillna(df["Performance_Score"].mean())

# Fill text missing values with "Unknown"

df["Department"] = df["Department"].fillna("Unknown")

df["City"] = df["City"].fillna("Unknown")

# Fill missing Joining_Date

df["Joining_Date"] = df["Joining_Date"].fillna("2000-01-01")

# Rename Column

df = df.rename(columns={"Performance_Score": "PerformanceScore"})

# Convert Date Format

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nClean Dataset:")
print(df)

print("\nMissing Values after Cleaning:")
print(df.isnull().sum())

# Save Clean Dataset

df.to_csv("output/cleaned_employees.csv", index=False)
print("\nCleaned dataset saved successfully.")

