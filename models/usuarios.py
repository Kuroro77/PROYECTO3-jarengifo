from config.db import db
from flask_login import UserMixin

class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(16), nullable=False)

    def auth(username, password):
        user = Usuarios.query.filter_by(username=username, password=password).first()
        return user