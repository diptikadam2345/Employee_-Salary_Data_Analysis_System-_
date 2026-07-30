import pandas as pd

df = pd.read_csv("data\employees.csv")

# Load Dataset

print("Employee Data:")
print(df)

print("\nTop 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

print("\nShape of the DataFrame:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

# Dataset Information

print("\nDataset Information:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nData Types of Columns:")
print(df.dtypes)

print("\nChecking for Missing Values:")
print(df.isnull().sum())

