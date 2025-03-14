from flask import Flask
from config.config import Config
from config.db import db
from config.routes import register_routes
from config.auth import login_manager

app = Flask(__name__, template_folder="views")
app.config.from_object(Config)
db.init_app(app)
login_manager.init_app(app)
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)