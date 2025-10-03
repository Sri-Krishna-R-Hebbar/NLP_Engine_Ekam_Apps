from flask import Blueprint, jsonify
from api.services.schema_discovery import SchemaDiscovery

bp = Blueprint("schema", __name__, url_prefix="/api/schema")
schema_service = SchemaDiscovery()

@bp.route("/", methods=["GET"])
def get_schema():
    if not schema_service.last_schema:
        return jsonify({"status": "error", "message": "No schema discovered yet"}), 404
    return jsonify({"status": "success", "schema": schema_service.last_schema})
