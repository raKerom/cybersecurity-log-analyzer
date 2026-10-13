
import pandas as pd

# 1. Load the existing dataset
df = pd.read_csv("security_logs.csv")

print("Original dataset shape:", df.shape)

# 2. Inspect the dataset
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn data types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

print("\nLabel counts:")
print(df["label"].value_counts())




# Assign a synthetic affected asset to each log
assets = [
    "web-server-01",
    "database-01",
    "workstation-01",
    "auth-server-01",
]

df["affected_asset"] = [
    assets[i % len(assets)]
    for i in range(len(df))
]

# 3. Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(
    df["timestamp"], errors="coerce"
)

# 4. Convert failed_attempts to numeric
df["failed_attempts"] = pd.to_numeric(
    df["failed_attempts"], errors="coerce"
)

# 5. Remove exact duplicate rows
df = df.drop_duplicates()

# 6. Remove rows missing essential information
df = df.dropna(
    subset=[
        "timestamp",
        "source_ip",
        "event_type",
        "failed_attempts",
        "label",
    ]
)

# 7. Keep only valid labels
df = df[df["label"].isin(["Normal", "Suspicious"])]

# 8. Save the cleaned dataset
df.to_csv("processed_logs.csv", index=False)

print("\nPreprocessing completed!")
print("Cleaned dataset shape:", df.shape)
print("\nFinal label counts:")
print(df["label"].value_counts())
print("\nSaved as processed_logs.csv")
