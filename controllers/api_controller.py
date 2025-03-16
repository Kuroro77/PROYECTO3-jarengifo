from flask import Blueprint, jsonify
from models.productos import Productos, ProductosSchema
from models.heladeria import Heladeria
from models.ingredientes import Ingredientes, IngredientesSchema

api_blueprint = Blueprint("api", __name__, url_prefix = "/api")
producto_schema = ProductosSchema()
productos_schema = ProductosSchema(many=True)

ingrediente_schema = IngredientesSchema()
ingredientes_schema = IngredientesSchema(many=True)

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

@api_blueprint.route("/productos/ventas/<int:id>", methods=["GET"])
def ventas(id):
    try:
       Heladeria.ventas(id)
       return jsonify({
           "mensaje": f'Producto vendido',
           "code": 200
       })
    except ValueError as e:
        return jsonify({
            "mensaje": f'Error en venta: {e}',
            "code": 404
        })

@api_blueprint.route("/ingredientes")
def ingredientes():
    ingredientes = Ingredientes()
    lista_ingredientes = ingredientes.listar()

    return jsonify({
        "mensaje": f'Lista ingredientes',
        "data": ingredientes_schema.dump(lista_ingredientes),
        "code": 200
    })

@api_blueprint.route("/ingredientes/<int:id>", methods=["GET"])
def detalle_ingrediente(id):
    ingredientes = Ingredientes()
    detalle_ingrediente = ingredientes.detalle(id)

    return jsonify({
        "mensaje": f'Detalle ingrediente',
        "data": ingrediente_schema.dump(detalle_ingrediente),
        "code": 200
    })

@api_blueprint.route("/ingredientes/<string:nombre>", methods=["GET"])
def detalle_x_nombre_ingrediente(nombre):
    ingredientes = Ingredientes()
    detalle_ingrediente = ingredientes.detalle_x_nombre(nombre)

    return jsonify({
        "mensaje": f'Detalle ingrediente',
        "data": ingrediente_schema.dump(detalle_ingrediente),
        "code": 200
    })

@api_blueprint.route("/ingredientes/sano/<int:id>", methods=["GET"])
def sano(id):
    ingrediente = Ingredientes.detalle(id)
    es_sano = ingrediente.es_sano(ingrediente.calorias, ingrediente.es_vegetariano)

    return jsonify({
        "mensaje": f'Ingrediente sano ?',
        "data": es_sano,
        "code": 200
    })

@api_blueprint.route("/ingredientes/abastecer/<int:id>", methods=["GET"])
def abastecer(id):
    ingrediente = Ingredientes.detalle(id)
    tipo = ingrediente.tipo

    if tipo == 'BASE':
        ingrediente.abastecer(ingrediente.id, ingrediente.inventario, 5)
    elif tipo == 'COMPLEMENTO':
        ingrediente.abastecer(ingrediente.id, ingrediente.inventario, 10)

    return jsonify({
        "mensaje": f'Ingrediente abastecido',
        "code": 200
    })

@api_blueprint.route("/ingredientes/renovar/<int:id>", methods=["GET"])
def renovar(id):
    ingrediente = Ingredientes.detalle(id)
    ingrediente.renovar(id)

    return jsonify({
        "mensaje": f'Inventario renovado',
        "code": 200
    })