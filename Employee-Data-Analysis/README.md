# Employee Data Analysis Project

## Project Description

This project is developed using Python, Pandas, NumPy, and Matplotlib.

The main objective of this project is to analyze employee data, clean the dataset, perform different analyses, generate visualizations, and export the final report.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL

---

## Project Folder Structure

Employee-Data-Analysis/

│

├── data/

│ └── employees.csv

│

├── output/

│ ├── cleaned_employees.csv

│ ├── report.csv

│ ├── salary_distribution.png

│ ├── department_distribution.png

│ ├── city_distribution.png

│ ├── age_distribution.png

│ ├── experience_distribution.png

│ └── performance_trend.png

│

├── src/

│ ├── load_data.py

| |__ main.py

│ ├── clean_data.py

│ ├── analysis.py

│ ├── visualization.py

│ └── report.py

│

├── README.md

└── requirements.txt

---

## Dataset Columns

- Employee_ID
- Name
- Age
- Gender
- Department
- Salary
- Experience
- City
- Joining_Date
- PerformanceScore

---

## Project Features

### Data Loading

- Load Employee Dataset
- Display First 5 Records
- Display Last 5 Records
- Display Shape
- Display Columns

### Dataset Information

- Dataset Information
- Data Types
- Statistical Summary
- Missing Values

### Data Cleaning

- Remove Duplicate Records
- Handle Missing Values
- Rename Columns
- Convert Date Format
- Export Cleaned Dataset

### Data Analysis

#### Salary Analysis

- Highest Salary
- Lowest Salary
- Average Salary
- Total Salary
- Median Salary

#### Department Analysis

- Employee Count
- Average Salary
- Highest Salary
- Lowest Salary

#### City Analysis

- Total Employees
- Average Salary
- Highest Paid City

#### Experience Analysis

- Average Experience
- Maximum Experience
- Minimum Experience

#### Performance Analysis

- Highest Performance Score
- Lowest Performance Score
- Average Performance Score

### Filtering

- Salary greater than 50000
- Age greater than 30
- Department = IT
- City = Pune

### Sorting

- Salary (Ascending & Descending)
- Age (Ascending & Descending)
- Experience (Ascending & Descending)

### Data Visualization

- Salary Distribution (Bar Chart)
- Department Analysis (Pie Chart)
- Employee by City (Bar Chart)
- Age Distribution (Histogram)
- Experience Distribution (Histogram)
- Performance Trend (Line Chart)

### Report Generation

- Generate report.csv
- Export cleaned dataset
- Save all charts

---

## Output Files

- cleaned_employees.csv
- report.csv
- salary_distribution.png
- department_distribution.png
- city_distribution.png
- age_distribution.png
- experience_distribution.png
- performance_trend.png

---

## How to Run

Install the required libraries

```
pip install -r requirements.txt
```

Run the files

```
python src/load_data.py
python src/clean_data.py
python src/analysis.py
python src/visualization.py
python src/report.py
```

---

## Author

Dipti Kadam
"# Employee_-Salary_Data_Analysis_System-_" 
