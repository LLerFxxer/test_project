import pandas as pd
import io
import allure

sales_csv = io.StringIO("""sale_id,product,qty,amount
1,A,10,150.00
2,B,20,200.00
3,C,30,0.00
""")

products_csv = io.StringIO("""product,name,price
A,Apple,100
B,Banana,200
D,Durian,300
""")

def test_integration():
    api_csv = pd.read_csv(sales_csv)
    db_csv = pd.read_csv(products_csv)
    merged = pd.merge(api_csv, db_csv, how="left", on="product", indicator=True, suffixes=("_api", "_db"))
    only_in_left = merged[merged["_merge"] == "left_only"]["product"].tolist()
    with allure.step("断言：merge 后行数 = 3，且 left_only 的行数为 1"):
        assert len(merged) == 3 and len(only_in_left) == 1
    with allure.step("找出 amount=0 的异常记录"):
        value_mismatch = []
        for _,row in merged.iterrows():
            if row["amount"] == 0:
                value_mismatch.append(row["product"])
        allure.attach(str(value_mismatch), "异常记录", allure.attachment_type.CSV)

    print(merged[(merged["amount"] == 0) & (merged["_merge"] == "left_only")].sort_values("product")[["sale_id", "product"]])
