from sqlalchemy import create_engine, text
from api.services.document_processor import DocumentProcessor
from api.services.nlp_query import NLPQueryEngine
import sqlparse

class QueryEngine:
    def __init__(self, connection_string: str):
        self.conn_str = connection_string
        self.engine = create_engine(connection_string)
        self.doc_service = DocumentProcessor()
        self.nlp_engine = NLPQueryEngine(self.doc_service)

    def is_sql_query(self, query: str):
        try:
            parsed = sqlparse.parse(query)
            return bool(parsed) and parsed[0].get_type() != "UNKNOWN"
        except Exception:
            return False

    def process_query(self, user_query: str):
        try:
            if self.is_sql_query(user_query):
                with self.engine.connect() as conn:
                    result = conn.execute(text(user_query))
                    rows = [dict(r) for r in result.mappings()]
                docs = self.doc_service.search(user_query)
                return {"results": rows, "documents": docs, "status": "success"}
            else:
                # Natural language query
                answer = self.nlp_engine.answer(user_query)
                print("[QueryEngine] NLP Answer:", answer)
                return {"results": [{"answer": answer}], "documents": [], "status": "success"}
        except Exception as e:
            return {"error": str(e), "status": "error"}
