import pandas as pd
import os
# updated via GitHub
def compare_data(api_df: pd.DataFrame, db_df: pd.DataFrame, key_col: str, compare_cols: list) -> dict:
    api_keys = set(api_df[key_col])
    db_keys = set(db_df[key_col])
    only_in_api = list(api_keys - db_keys)
    only_in_db = list(db_keys - api_keys)

    merged = pd.merge(api_df, db_df, how="inner", on=key_col, suffixes=("_api", "_db"))
    value_mismatch = [
        {key_col: row[key_col], "column": col, "api_value": row[f"{col}_api"], "db_value": row[f"{col}_db"]}
        for _, row in merged.iterrows()
        for col in compare_cols
        if row[f"{col}_api"] != row[f"{col}_db"]
    ]

    return {
        "only_in_api": only_in_api,
        "only_in_db": only_in_db,
        "value_mismatch": value_mismatch
    }

def check_login(username, password):
    return username == "admin" and password == os.getenv("DB_PASSWORD")

def setup_logging(level):
    print(f"Logging set to {level}")
