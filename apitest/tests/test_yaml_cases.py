import pathlib

import allure
import pytest
import responses
import yaml

from apitest.utils.assertions import assert_code, assert_schema

CASES = yaml.safe_load((pathlib.Path(__file__).parent.parent / "data" / "cases.yml").read_text(encoding="utf-8"))

@allure.feature("接口框架")
@allure.title("{case[name]}")
@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
@responses.activate
def test_yaml_case(case, client):
    responses.add(case["method"], case["url"], json=case["expected"], status=case["expected"]["code"])
    resp = client.request(case["method"], case["url"])
    assert_code(resp, case["expected"]["code"])
    assert_schema(resp.json(), case["expected"])