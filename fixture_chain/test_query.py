from query import query_translations


def test_query_translations(mysql_conn):
    res = query_translations(mysql_conn)
    assert len(res) == 3
    assert {"id": 1, "text": "你好", "lang": "zh", "chars": 2} in res
    assert {"id": 2, "text": "hello", "lang": "en", "chars": 5} in res
    assert {"id": 3, "text": "bonjour", "lang": "fr", "chars": 7} in res