from config.db import db, ma

class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Integer, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(256), nullable=False)
    inventario = db.Column(db.Integer, nullable=False)
    es_vegetariano = db.Column(db.Boolean, nullable=False)
    tipo = db.Column(db.String(16), nullable=False)

    def listar(self):
        ingredientes = Ingredientes.query.all()
        return ingredientes

    @staticmethod
    def detalle(id):
        ingrediente = Ingredientes.query.filter_by(id=id).first()
        return ingrediente

    @staticmethod
    def detalle_x_nombre(nombre):
        producto = Ingredientes.query.filter_by(nombre=nombre).first()
        return producto

class IngredientesSchema(ma.Schema):
    class Meta:
        model = Ingredientes
        fields = ("id", "nombre", "precio", "calorias", "inventario", "es_vegetariano", "tipo")