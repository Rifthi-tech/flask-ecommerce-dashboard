import pandas as pd

def load_data():
    df = pd.read_csv("dataset/ecommerce.csv")

    # Clean column names (important for safety)
    df.columns = df.columns.str.strip()

    # Ensure numeric columns
    df["Aggregate rating"] = pd.to_numeric(df["Aggregate rating"], errors="coerce")
    df["Average Cost for two"] = pd.to_numeric(df["Average Cost for two"], errors="coerce")
    df["Votes"] = pd.to_numeric(df["Votes"], errors="coerce")

    return df