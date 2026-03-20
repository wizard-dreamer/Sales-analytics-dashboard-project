try:
    import pandas as pd
except ModuleNotFoundError:
    raise SystemExit("Missing dependency: pandas is required. Install with `pip install pandas`.")

import sqlite3

# === Step 1: Load dataset ===
csv_path = "data/sales_data.csv"
df = pd.read_csv(csv_path, parse_dates=["Order_Date"])
print("Initial rows:", len(df))
print(df.head())

# === Step 2: Data cleaning and validation ===
# Remove fully empty rows
initial_count = len(df)
df = df.dropna(how='all')
print(f"Dropped {initial_count - len(df)} fully empty rows")

# Standardize column names in case CSV format changes
expected_cols = ["Order_ID", "Order_Date", "Product_Name", "Category", "Country", "Sales", "Profit", "Quantity"]
if not set(expected_cols).issubset(df.columns):
    missing = set(expected_cols) - set(df.columns)
    raise ValueError(f"Missing required columns: {missing}")

# Convert numeric fields and fix invalid values
for col in ["Sales", "Profit", "Quantity"]:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with null in key fields
df = df.dropna(subset=["Order_ID", "Order_Date", "Product_Name", "Category", "Country", "Sales", "Profit", "Quantity"])
print("After dropping rows with key nulls:", len(df))

# Remove clear duplicates
dupe_count = df.duplicated().sum()
if dupe_count > 0:
    df = df.drop_duplicates()
    print(f"Dropped {dupe_count} duplicate rows")

# Optional value sanity filter
df = df[(df["Quantity"] > 0) & (df["Sales"] >= 0) & (df["Profit"].abs() < 1000000)]
print("After sanity filtering:", len(df))

# === Step 3: Create SQLite DB and save table ===
db_path = "sales.db"
conn = sqlite3.connect(db_path)
df.to_sql("sales", conn, if_exists="replace", index=False)
print(f"Created '{db_path}' with {len(df)} records in 'sales' table")

# Create a helper summary table for quick queries
summary = (df.groupby(["Category", "Country"]).agg(
    total_sales=("Sales", "sum"),
    total_profit=("Profit", "sum"),
    total_quantity=("Quantity", "sum")
).reset_index())
summary.to_sql("sales_summary", conn, if_exists="replace", index=False)
print("Created 'sales_summary' table for category-country insights")

conn.close()

