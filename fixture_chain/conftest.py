import pytest
import sqlite3

ENV_CONFIG = {
    "test": {"db": "test.db", "url": "http://localhost:8000"},
    "prod": {"db": "prod.db", "url": "https://api.example.com"},
}

def pytest_addoption(parser):
    parser.addoption("--env", default="test")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def config(env):
    if env == "test":
        return ENV_CONFIG["test"]
    else:
        return ENV_CONFIG["prod"]

@pytest.fixture(scope="session")
def db_conn(config):
    conn = sqlite3.connect(config["db"])
    yield conn
    conn.close()