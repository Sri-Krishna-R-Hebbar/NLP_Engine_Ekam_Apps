from sqlalchemy import create_engine, MetaData

class SchemaDiscovery:
    def __init__(self):
        self.last_schema = {}

    def analyze_database(self, connection_string: str) -> dict:
        engine = create_engine(connection_string)
        metadata = MetaData()
        try:
            metadata.reflect(bind=engine)
        except Exception as e:
            return {"error": str(e)}

        schema = {
            "tables": [],
            "relationships": []  # placeholder for future
        }
        for table_name, table in metadata.tables.items():
            schema["tables"].append({
                "name": table_name,
                "columns": [col.name for col in table.columns]
            })
        self.last_schema = schema
        return schema
