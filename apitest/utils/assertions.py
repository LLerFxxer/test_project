def assert_code(resp, expected_code):
    assert resp.status_code == expected_code

def assert_key(body, key):
    assert key in body

def assert_schema(body, expected):
    for k, v in expected.items():
        assert k in body, f"响应缺少字段 {k}"
        assert isinstance(body[k], type(v))