# CSV Data Validator and Summary Tool

## 📌 Project Overview

The **CSV Data Validator and Summary Tool** is a Python-based project designed to read CSV files, identify missing values, detect duplicate records, validate data formats, and generate useful statistical summaries.

This tool helps users clean and understand datasets before performing further data analysis. It reduces manual data-checking efforts and improves overall data quality.

## 🎯 Objectives

- Validate CSV files and check data consistency.
- Identify missing or empty values.
- Detect duplicate records.
- Generate statistical summaries of numerical columns.
- Display dataset information in a structured format.
- Help prepare clean datasets for data analysis.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy
- **File Format:** CSV
- **Development Environment:** VS Code / PyCharm

## ⚙️ Key Features

1. **CSV File Reading:** Loads CSV datasets using Python.
2. **Missing Value Detection:** Identifies null and empty values in columns.
3. **Duplicate Detection:** Finds duplicate records in the dataset.
4. **Data Validation:** Checks column data types and data consistency.
5. **Statistical Summary:** Generates count, mean, standard deviation, minimum, and maximum values for numerical columns.
6. **Dataset Overview:** Displays the number of rows, columns, and column names.
7. **Data Quality Report:** Provides a summary of detected data issues.

## 📂 Project Structure

```text
CSV-Data-Validator-and-Summary-Tool/
│
├── main.py
├── sample_data.csv
├── requirements.txt
├── README.md
└── output/
    └── validation_report.txt
```

## 🚀 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd CSV-Data-Validator-and-Summary-Tool
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python main.py
```

## 📊 Sample Output

```text
========== CSV DATA VALIDATOR ==========

Dataset Information:
Total Rows: 100
Total Columns: 5

Missing Values:
Name: 2
Age: 3
Salary: 1

Duplicate Records: 4

Statistical Summary:
             Age       Salary
Count      97.00        99.00
Mean       25.50     45000.00
Minimum    18.00     20000.00
Maximum    40.00     90000.00

========== VALIDATION COMPLETED ==========
```

*Note: Sample output is illustrative; actual results depend on the input CSV file.*

## 💡 Learning Outcomes

- Practical experience with Python programming.
- Understanding CSV file handling.
- Hands-on experience with Pandas and NumPy.
- Data cleaning and preprocessing techniques.
- Identifying data quality issues.
- Generating statistical reports from datasets.

## 🔮 Future Enhancements

- Add an interactive graphical user interface.
- Support Excel files (XLSX).
- Automatically clean missing and duplicate records.
- Generate downloadable PDF and Excel reports.
- Add interactive data visualizations.

## 👨‍💻 Author

**Koushik Kumar Katla**

B.Tech – Computer Science and Engineering (AI & ML)

**Project Domain:** Python | Data Analytics | Data Validation

---

⭐ If you find this project useful, feel free to star the repository!
