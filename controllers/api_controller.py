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

@api_blueprint.route("/productos/calorias/<int:id>", methods=["GET"])
def calorias(id):
    producto = Productos.detalle(id)
    tipo = producto.tipo
    calorias_x_ingredientes = [producto.ingrediente_uno.calorias, producto.ingrediente_dos.calorias, producto.ingrediente_tres.calorias]

    if tipo =='COPA':
        calorias = producto.calcular_calorias_copa(calorias_x_ingredientes)
    elif tipo =='MALTEADA':
        calorias = producto.calcular_calorias_malteada(calorias_x_ingredientes)

    return jsonify({
        "mensaje": f'Calorias producto',
        "data": calorias,
        "code": 200
    })

@api_blueprint.route("/productos/rentabilidad/<int:id>", methods=["GET"])
def rentabilidad(id):
    producto = Productos.detalle(id)
    rentabilidad = producto.calcular_rentabilidad(producto.precio_publico, producto.ingrediente_uno, producto.ingrediente_dos, producto.ingrediente_tres)

    return jsonify({
        "mensaje": f'Rentabilidad producto',
        "data": rentabilidad,
        "code": 200
    })

@api_blueprint.route("/productos/costos/<int:id>", methods=["GET"])
def costos(id):
    producto = Productos.detalle(id)
    tipo = producto.tipo

    if tipo == 'COPA':
        costo = producto.calcular_costo_copa(producto.ingrediente_uno, producto.ingrediente_dos, producto.ingrediente_tres)
    elif tipo == 'MALTEADA':
        costo = producto.calcular_costo_malteada()

    return jsonify({
        "mensaje": f'Costo producto',
        "data": costo,
        "code": 200
    })
