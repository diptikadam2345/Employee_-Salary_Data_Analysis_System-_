import pandas as pd

df = pd.read_csv("output\cleaned_employees.csv")

print("Cleaned Employee Dataset:")
print(df)

# Salary Analysis

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nTotal Salary:")
print(df["Salary"].sum())

print("\nMedian Salary:")
print(df["Salary"].median())

# Department Analysis
print("\nDepartment Analysis:")

# Employee Count
print("\nEmployee count in each department:")
print(df["Department"].value_counts())

# Average Salary
print("\nAverage salary in each department:")
print(df.groupby("Department")["Salary"].mean())

# Highest Salary
print("\nHighest salary in each department:")
print(df.groupby("Department")["Salary"].max())

# Lowest Salary
print("\nLowest salary in each department:")
print(df.groupby("Department")["Salary"].min())

# City Analysis
print("\nCity Analysis:")

#Total Employees
print("\nTotal employees in each city:")
print(df["City"].value_counts())

#Average Salary
print("\nAverage salary in each city:")
print(df.groupby("City")["Salary"].mean())

# Highest Paid City
print("\nHighest paid city:")
city_salary = df.groupby("City")["Salary"].mean()
highest_paid_city = city_salary.idxmax()
print(highest_paid_city)


# Experience Analysis
print("\nExperience Analysis:")

# Average Experience
print("\nAverage experience:")
print(df["Experience"].mean())

# Maximum Experience
print("\nMaximum experience:")
print(df["Experience"].max())

# Minimum Experience
print("\nMinimum experience:")
print(df["Experience"].min())

# Performance Analysis
print("\nPerformance Analysis:")

# Highest Performance Score
print("\nHighest performance score:")
print(df["PerformanceScore"].max())

# Lowest Performance Score
print("\nLowest performance score:")
print(df["PerformanceScore"].min())

# Average Performance Score
print("\nAverage performance score:")
print(df["PerformanceScore"].mean())

# Filtering

print("Employees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("Employees with Age>30")
print(df[df["Age"] > 30])

print("Employees from IT department:")
print(df[df["Department"] == "IT"])

print("Employees from pune")
print(df[df["City"] == "Pune"])


# Sorting

# Salary Sorting
print("Salary sorted in ascending order:")
print(df.sort_values("Salary"))

print("Salary sorted in descending order:")
print(df.sort_values("Salary", ascending=False))

# Age Sorting
print("Age sorted in ascending order:")
print(df.sort_values("Age"))

print("Age sorted in descending order:")
print(df.sort_values("Age", ascending=False))

# Experience Sorting
print("Experience sorted in ascending order:")
print(df.sort_values("Experience"))

print("Experience sorted in descending order:")
print(df.sort_values("Experience", ascending=False))





