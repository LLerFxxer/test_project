def test_env_chain(env, config, db_conn):
    assert env in ("test", "prod")
    assert config["db"] == f"{env}.db"
    assert db_conn is not None
