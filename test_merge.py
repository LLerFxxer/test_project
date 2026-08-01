import pandas as pd

df_sales = pd.DataFrame({
    "sale_id": [1, 2, 3],
    "product": ["A", "B", "C"],
    "qty": [10, 20, 30]
})
df_products = pd.DataFrame({
    "product": ["A", "B", "D"],
    "price": [100, 200, 300]
})

def test_merge():
    merged = pd.merge(df_sales, df_products, how="left", on="product", indicator=True, suffixes=("_sl", "_pd"))
    assert len(merged) == 3
    only_left = merged[merged["_merge"] == "left_only"]
    assert len(only_left) == 1
