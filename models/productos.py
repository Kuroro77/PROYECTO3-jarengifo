from config.db import db, ma
from models.ingredientes import Ingredientes
from funciones import Funciones

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

    @staticmethod
    def detalle_x_nombre(nombre):
        producto = Productos.query.filter_by(nombre=nombre).first()
        return producto

    @staticmethod
    def calcular_calorias_copa(calorias: list) -> float:
        calorias_total = Funciones.calorias_x_producto(calorias)
        return calorias_total

    @staticmethod
    def calcular_calorias_malteada(calorias: list) -> float:
        calorias_crema = 200
        calorias_totales = 0

        for caloria in calorias:
            calorias_totales += caloria

        calorias_total = calorias_totales + calorias_crema
        return calorias_total

class ProductosSchema(ma.Schema):
    class Meta:
        model = Productos
        fields = ("id", "nombre", "precio_publico", "rentabilidad", "tipo")
