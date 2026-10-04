import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "clean_retail_transactions.csv"
OUTPUT_FILE = BASE_DIR / "data" / "rfm.csv"

transactions = pd.read_csv(INPUT_FILE, parse_dates=["InvoiceDate"])

snapshot_date = transactions["InvoiceDate"].max() + pd.Timedelta(days=1)

rfm = transactions.groupby("Customer ID").agg(
    Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("Invoice", "nunique"),
    Monetary=("Transaction_Value", "sum")
).reset_index()

rfm.to_csv(OUTPUT_FILE, index=False)

print("RFM analysis completed.")
print(f"Snapshot date: {snapshot_date}")
print(f"Customers analyzed: {len(rfm):,}")
print(f"Average Recency: {rfm['Recency'].mean():.2f} days")
print(f"Average Frequency: {rfm['Frequency'].mean():.2f} orders")
print(f"Average Monetary Value: £{rfm['Monetary'].mean():,.2f}")
print(f"Saved to: {OUTPUT_FILE}")
