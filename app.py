from flask import Flask
from flask_cors import CORS

from routes.analisis_routes import analisis_bp
from routes.extraccion_routes import extraccion_bp
from routes.dashboard_routes import dashboard_bp
from routes.test_routes import test_bp
from routes.report_routes import report_bp
from routes.user_routes import user_bp
from routes.config_routes import config_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    analisis_bp
)

app.register_blueprint(
    extraccion_bp
)

app.register_blueprint(
    dashboard_bp
)

app.register_blueprint(
    test_bp
)

app.register_blueprint(
    report_bp
)
app.register_blueprint(
    user_bp
)
app.register_blueprint(
    config_bp
)

if __name__ == "__main__":
    app.run(debug=True)

