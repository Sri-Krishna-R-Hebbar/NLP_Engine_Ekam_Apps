from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes and origins

# Import and register your blueprints
from api.routes.ingestion import bp as ingestion_bp
from api.routes.query import bp as query_bp
from api.routes.schema import bp as schema_bp
from api.routes.debug import bp as debug_bp

app.register_blueprint(ingestion_bp)
app.register_blueprint(query_bp)
app.register_blueprint(schema_bp)
app.register_blueprint(debug_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
