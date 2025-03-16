from config.db import db

class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo = db.Column(db.String(16), nullable=False)