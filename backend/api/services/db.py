from sqlalchemy import create_engine, text

def run_sql_query(connection_string: str, query: str):
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = [dict(r) for r in result.mappings()]
    return rows
