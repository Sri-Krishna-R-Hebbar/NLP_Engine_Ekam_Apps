from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, text

bp = Blueprint("debug", __name__, url_prefix="/api/debug")

@bp.route("/test", methods=["POST"])
def test_connection():
    data = request.get_json()
    conn_str = data.get("connection_string")
    try:
        engine = create_engine(conn_str)
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            rows = [dict(row._mapping) for row in result.fetchall()]
        return jsonify({"status": "ok", "rows": rows})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400


