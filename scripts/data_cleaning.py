import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR.parent / "online_retail_II.xlsx"
OUTPUT_FILE = BASE_DIR / "data" / "clean_retail_transactions.csv"

# Load both periods
sheet_2009_2010 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2009-2010"
)

sheet_2010_2011 = pd.read_excel(
    RAW_FILE,
    sheet_name="Year 2010-2011"
)

# Combine datasets
transactions = pd.concat(
    [sheet_2009_2010, sheet_2010_2011],
    ignore_index=True
)

original_rows = len(transactions)

# Remove records without customer identification
transactions = transactions.dropna(subset=["Customer ID"])

# Remove cancelled invoices
transactions = transactions[
    ~transactions["Invoice"].astype(str).str.startswith("C")
]

# Keep valid purchases only
transactions = transactions[
    (transactions["Quantity"] > 0) &
    (transactions["Price"] > 0)
]

# Remove duplicate records
transactions = transactions.drop_duplicates()

# Calculate transaction value
transactions["Transaction_Value"] = (
    transactions["Quantity"] * transactions["Price"]
)

# Save cleaned dataset
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
transactions.to_csv(OUTPUT_FILE, index=False)

print("Data cleaning completed.")
print(f"Original rows: {original_rows:,}")
print(f"Clean rows: {len(transactions):,}")
print(f"Rows removed: {original_rows - len(transactions):,}")
print(f"Customers: {transactions['Customer ID'].nunique():,}")
print(f"Invoices: {transactions['Invoice'].nunique():,}")
print(f"Total transaction value: £{transactions['Transaction_Value'].sum():,.2f}")
print(f"Saved to: {OUTPUT_FILE}")
