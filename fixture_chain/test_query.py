from query import query_top_employee

def test_query(db_conn):
    res = query_top_employee(db_conn)
    assert len(res) == 3
    assert {"dept": "研发", "name": "张三", "salary": 20000} in res
    assert {"dept": "市场", "name": "赵六", "salary": 16000} in res
    assert {"dept": "财务", "name": "孙七", "salary": 12000} in res