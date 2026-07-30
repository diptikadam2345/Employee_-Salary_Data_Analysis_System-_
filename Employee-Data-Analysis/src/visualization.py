import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/cleaned_employees.csv")

# Salary Distribution

plt.figure(figsize=(10,6))
plt.bar(df["Name"], df["Salary"], color="skyblue", edgecolor="black")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.title("Employee Salary Distribution")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("output/salary_distribution.png")
plt.show()
print("Salary chart saved successfully")


# Department Analysis (Pie Chart)

department_counts = df["Department"].value_counts()
plt.figure(figsize=(8,8))
plt.pie(
    department_counts,
    labels=department_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)
plt.title("Employee Distribution by Department")
plt.savefig("output/department_distribution.png")
plt.show()
print("Department chart saved successfully.")


# Employee by City (Bar Chart)

city_counts = df["City"].value_counts()
plt.figure(figsize=(10,6))
plt.bar(city_counts.index, city_counts.values, color="skyblue", edgecolor="black")
plt.title("Employee Distribution by City")
plt.xlabel("City")
plt.ylabel("Number of Employees")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/city_distribution.png")
plt.show()
print("City chart saved successfully.")


# Age Distribution (Histogram)

plt.figure(figsize=(10,6))
plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
plt.title("Age Distribution of Employees")
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("output/age_distribution.png")
plt.show()
print("Age chart saved successfully.")


# Experience Distribution (Histogram)

plt.figure(figsize=(10,6))
plt.hist(df["Experience"], bins=10, color="skyblue", edgecolor="black") 
plt.title("Experience Distribution of Employees")
plt.xlabel("Years of Experience")
plt.ylabel("Number of Employees")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("output/experience_distribution.png")
plt.show()
print("Experience chart saved successfully.")


# Performance Trend (Line Chart)

plt.figure(figsize=(10,6))
plt.plot(df["Name"], df["PerformanceScore"], marker="o", linestyle="-", color="skyblue",alpha=0.5)
plt.title("Performance Score Trend of Employees")
plt.xlabel("Employee Name")
plt.ylabel("Performance Score")
plt.xticks(rotation=90)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("output/performance_trend.png")
plt.show()
print("Performance trend chart saved successfully.")    
