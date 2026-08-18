import pandas as pd


def query_translations(mysql_conn):
    res = pd.read_sql("""
    SELECT id, text, lang, chars
    FROM translations
    ORDER BY id
    """, mysql_conn)
    return res.to_dict("records")