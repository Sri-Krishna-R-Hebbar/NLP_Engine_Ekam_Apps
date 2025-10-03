from flask import Blueprint, request, jsonify
from api.services.schema_discovery import SchemaDiscovery
from api.services.document_processor import DocumentProcessor
from api.services.document_store import save_document_text  # ✅ import the store
import os

bp = Blueprint("ingestion", __name__, url_prefix="/api/ingest")

schema_service = SchemaDiscovery()
doc_service = DocumentProcessor()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/database", methods=["POST"])
def ingest_database():
    data = request.get_json()
    conn_str = data.get("connection_string")
    try:
        schema = schema_service.analyze_database(conn_str)
        return jsonify({"status": "success", "schema": schema})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@bp.route("/documents", methods=["POST"])
def upload_documents():
    if "files" not in request.files:
        return jsonify({"status": "error", "message": "No files uploaded"}), 400

    files = request.files.getlist("files")
    file_paths = []
    all_text = ""  # ✅ collect all extracted text

    for f in files:
        safe_filename = f.filename.replace(" ", "_")
        path = os.path.join(UPLOAD_FOLDER, safe_filename)
        f.save(path)
        file_paths.append(path)

    try:
        # Process documents (your processor should return extracted text)
        texts = doc_service.process_documents(file_paths)

        # If process_documents returns a list of texts, join them
        if isinstance(texts, list):
            all_text = "\n".join(texts)
        else:
            all_text = str(texts)

        # ✅ Save into our persistent document store
        save_document_text(all_text)

        return jsonify({
            "status": "success",
            "detail": f"{len(files)} documents processed and saved",
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
