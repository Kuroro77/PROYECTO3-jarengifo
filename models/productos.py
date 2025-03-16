from config.db import db, ma
from models.ingredientes import Ingredientes

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(256), nullable=False)
    precio_publico = db.Column(db.Integer, nullable=False)
    id_ingrediente_uno = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=False)
    id_ingrediente_dos = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=False)
    id_ingrediente_tres = db.Column(db.Integer, db.ForeignKey("ingredientes.id"), nullable=False)
    rentabilidad = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(16), nullable=False)

    ingrediente_uno = db.relationship("Ingredientes", foreign_keys=[id_ingrediente_uno])
    ingrediente_dos = db.relationship("Ingredientes", foreign_keys=[id_ingrediente_dos])
    ingrediente_tres = db.relationship("Ingredientes", foreign_keys=[id_ingrediente_tres])

    def listar(self):
        productos = Productos.query.all()
        return productos

    @staticmethod
    def detalle(id):
        producto = Productos.query.filter_by(id=id).first()
        return producto

class ProductosSchema(ma.Schema):
    class Meta:
        model = Productos
        fields = ("id", "nombre", "precio_publico", "rentabilidad", "tipo")
