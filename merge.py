import pandas as pd
# updated via GitHub
def compare_data(api_df: pd.DataFrame, db_df: pd.DataFrame, key_col: str, compare_cols: list) -> dict:
    merged = pd.merge(api_df, db_df, how="outer", on=key_col, indicator=True, suffixes=("_api", "_db"))
    only_in_api = merged[merged["_merge"] == "left_only"][key_col].to_list()
    only_in_db = merged[merged["_merge"] == "right_only"][key_col].to_list()
    both = merged[merged["_merge"] == "both"]
    value_mismatch = [
        {key_col: row[key_col], "column": col, "api_value": row[f"{col}_api"], "db_value": row[f"{col}_db"]}
        for _,row in both.iterrows()
        for col in compare_cols
        if row[f"{col}_api"] != row[f"{col}_db"]
    ]

    return{
        "only_in_api":only_in_api,
        "only_in_db":only_in_db,
        "value_mismatch":value_mismatch
    }

def check_login(username, pd):
    return username == "admin" and pd == "123456"

def setup_logging(level):
    print(f"Logging set to {level}")

def find_duplicates(df, key):
    return df[df.duplicated(subset=[key], keep=False)].sort_values(key)