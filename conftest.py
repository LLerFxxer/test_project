import pandas as pd
import pytest

# 两个 CSV（模拟数据）
df_sales = pd.DataFrame({
    "sale_id": [1, 2, 3],
    "product": ["A", "B", "C"],
    "qty": [10, 20, 30]
})
df_products = pd.DataFrame({
    "product": ["A", "B", "D"],
    "price": [100, 200, 300]
})

@pytest.fixture(scope="function")
def merge_res():
    return pd.merge(df_sales, df_products, how="left", on="product", indicator=True, suffixes=("_sl", "_pd"))

def test_merge(merge_res):
    assert len(merge_res) == 3
    only_left = merge_res[merge_res["_merge"] == "left_only"]
    assert len(only_left) == 1
