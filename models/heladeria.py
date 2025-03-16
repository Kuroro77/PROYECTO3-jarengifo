from models.productos import Productos
from models.ingredientes import Ingredientes
from config.db import db

class Heladeria():
        @staticmethod
        def ventas(id):
            producto = Productos.query.filter_by(id=id).first()

            if not producto:
                raise ValueError('Producto no encontrado')

            ingredientes = [producto.ingrediente_uno, producto.ingrediente_dos, producto.ingrediente_tres]

            for ingrediente in ingredientes:
                if ingrediente.tipo == "BASE":
                    inventario = ingrediente.inventario
                    if inventario < 0.2:
                        raise ValueError(ingrediente.nombre)
                if ingrediente.tipo == "COMPLEMENTO":
                    inventario = ingrediente.inventario
                    if inventario < 1:
                        raise ValueError(ingrediente.nombre)

            for ingrediente in ingredientes:
                if ingrediente.tipo == "BASE":
                    nuevo_inventario = ingrediente.inventario - 0.2
                    Ingredientes.query.filter_by(id=ingrediente.id).update({"inventario": nuevo_inventario})
                    db.session.commit()
                if ingrediente.tipo == "COMPLEMENTO":
                    nuevo_inventario = ingrediente.inventario - 1
                    Ingredientes.query.filter_by(id=ingrediente.id).update({"inventario": nuevo_inventario})
                    db.session.commit()

            return True