import sqlite3

import pymysql
import pytest

ENV_CONFIG = {
    "test": {"db": "test.db", "url": "http://localhost:8000",
             "mysql": {"host": "127.0.0.1", "port": 3306, "user": "root", 
                       "password": "root", "database": "test"}},
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

@pytest.fixture(scope="session")
def mysql_conn(config):
    conn = pymysql.connect(**config["mysql"])
    yield conn
    conn.close()