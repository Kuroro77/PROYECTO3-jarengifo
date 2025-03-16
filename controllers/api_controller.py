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

@api_blueprint.route("/productos/<int:id>", methods=["GET"])
def detalle(id):
    producto = Productos()
    detalle_producto = producto.detalle(id)

    return jsonify({
        "mensaje": f'Detalle producto',
        "data": producto_schema.dump(detalle_producto),
        "code": 200
    })

@api_blueprint.route("/productos/<string:nombre>", methods=["GET"])
def detalle_x_nombre(nombre):
    producto = Productos()
    detalle_producto = producto.detalle_x_nombre(nombre)

    return jsonify({
        "mensaje": f'Detalle producto',
        "data": producto_schema.dump(detalle_producto),
        "code": 200
    })
