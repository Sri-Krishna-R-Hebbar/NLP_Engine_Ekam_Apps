from flask import Blueprint, request, jsonify
from api.services.db import run_sql_query
from api.services.document_processor import DocumentProcessor
import re

bp = Blueprint("query", __name__, url_prefix="/api/query")

doc_service = DocumentProcessor()

@bp.route("/", methods=["POST"])
def run_query():
    data = request.get_json()
    query = data.get("query", "").strip()
    connection_string = data.get("connection_string", "").strip()

    if not query:
        return jsonify({"status": "error", "message": "No query provided"}), 400

    # Simple check: if query starts with SELECT/INSERT/UPDATE etc. treat as SQL
    sql_pattern = re.compile(r"^(SELECT|INSERT|UPDATE|DELETE|CREATE|DROP|ALTER)\b", re.IGNORECASE)

    if sql_pattern.match(query):
        # Run SQL query
        try:
            results = run_sql_query(connection_string, query)
            return jsonify({"status": "success", "data": {"results": results, "documents": []}})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    else:
        # Run NLP QA query on uploaded documents
        try:
            doc_answer = doc_service.query_documents(query)
            return jsonify({"status": "success", "data": {"results": [{"answer": doc_answer}], "documents": []}})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
