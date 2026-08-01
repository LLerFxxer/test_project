def test_env_chain(env, config, db_conn):
    assert env in ("test", "prod")
    assert config == {"db": "test.db", "url": "http://localhost:8000"} or config["db"] == "prod.db"
    assert db_conn is not None
