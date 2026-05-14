#!/usr/bin/env python3
import pandas as pd

# Read the Excel file
excel_path = '/Users/marc/Desktop/beschrijvingen.xlsx'
xls = pd.ExcelFile(excel_path)

print(f"Sheet names: {xls.sheet_names}")

for sheet in xls.sheet_names:
    df = pd.read_excel(excel_path, sheet_name=sheet)
    print(f"\n=== Sheet: {sheet} ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Column names: {df.columns.tolist()}")
    print(f"\nFirst 3 rows:")
    print(df.head(3).to_string())
