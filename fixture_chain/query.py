import sqlite3
import pandas as pd

def query_top_employee(db_conn):
    db_conn.executescript("""
    DROP TABLE IF EXISTS employees;
    CREATE TABLE employees (id INTEGER, name TEXT, dept TEXT, salary INTEGER);
    INSERT INTO employees VALUES
    (1,'张三','研发',20000),(2,'李四','研发',18000),
    (3,'王五','市场',15000),(4,'赵六','市场',16000),
    (5,'孙七','财务',12000);
    """)

    res = pd.read_sql("""
    SELECT dept, name, salary
    FROM(
    SELECT dept, name, salary, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn
    FROM employees
    )
    WHERE rn = 1
    """, db_conn)

    return res.to_dict("records")