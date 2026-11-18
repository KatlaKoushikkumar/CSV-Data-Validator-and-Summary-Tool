"""
CSV Data Validator and Summary Tool
-----------------------------------
A beginner-friendly Python project that checks a CSV file for:
- Missing required values
- Invalid email addresses
- Invalid ages
- Duplicate email addresses

Usage:
    python csv_validator.py sample_records.csv

The script creates validation_report.csv in the same folder.
Use synthetic/demo data only; do not put real Aadhaar or other sensitive data in this project.
"""

import csv
import re
import sys
from pathlib import Path

REQUIRED_COLUMNS = ["full_name", "email", "age", "city"]
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_file(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: File not found: {path}")
        return

    with path.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames:
            print("Error: CSV file is empty or has no header.")
            return

        missing_columns = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing_columns:
            print("Error: Missing required columns:", ", ".join(missing_columns))
            print("Required columns:", ", ".join(REQUIRED_COLUMNS))
            return

        rows = list(reader)

    seen_emails = set()
    report_rows = []
    valid_count = 0

    for row_number, row in enumerate(rows, start=2):
        issues = []

        name = (row.get("full_name") or "").strip()
        email = (row.get("email") or "").strip().lower()
        age_text = (row.get("age") or "").strip()
        city = (row.get("city") or "").strip()

        if not name:
            issues.append("Missing full_name")
        if not email:
            issues.append("Missing email")
        elif not EMAIL_PATTERN.match(email):
            issues.append("Invalid email format")

        if not age_text:
            issues.append("Missing age")
        else:
            try:
                age = int(age_text)
                if age < 1 or age > 120:
                    issues.append("Age must be between 1 and 120")
            except ValueError:
                issues.append("Age must be a whole number")

        if not city:
            issues.append("Missing city")

        if email:
            if email in seen_emails:
                issues.append("Duplicate email")
            else:
                seen_emails.add(email)

        status = "Valid" if not issues else "Invalid"
        if status == "Valid":
            valid_count += 1

        report_rows.append({
            "row_number": row_number,
            "full_name": name,
            "email": email,
            "status": status,
            "issues": "; ".join(issues) if issues else "None"
        })

    report_path = path.with_name("validation_report.csv")
    with report_path.open("w", newline="", encoding="utf-8") as file:
        fieldnames = ["row_number", "full_name", "email", "status", "issues"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)

    total = len(rows)
    invalid_count = total - valid_count

    print("\nCSV Validation Summary")
    print("----------------------")
    print(f"Total records : {total}")
    print(f"Valid records : {valid_count}")
    print(f"Invalid records: {invalid_count}")
    print(f"Report saved  : {report_path.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_validator.py <input_csv_file>")
    else:
        validate_file(sys.argv[1])
