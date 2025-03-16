from flask import Blueprint, jsonify
from models.productos import Productos, ProductosSchema

api_blueprint = Blueprint("api", __name__, url_prefix = "/api")
producto_schema = ProductosSchema()
productos_schema = ProductosSchema(many=True)

@api_blueprint.route("/productos")
def productos():
    productos = Productos()
    lista_productos = productos.listar()

    return jsonify({
        "mensaje": f'Lista productos',
        "data": productos_schema.dump(lista_productos),
        "code": 200
    })
