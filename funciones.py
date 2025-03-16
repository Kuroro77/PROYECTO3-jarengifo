class Funciones():

    @staticmethod
    def es_sano(calorias:int, vegetariano:bool)->bool:

        if calorias < 100 or vegetariano == True:
            return True
        else:
            return False

    @staticmethod
    def calorias_x_producto(calorias:list)->float:
        calorias_totales = 0

        for caloria in calorias:
            calorias_totales += caloria

        calorias_totales = calorias_totales * 0.95

        return round(calorias_totales, 2)

    @staticmethod
    def costo_produccion(ingredientes1:dict, ingredientes2:dict, ingredientes3:dict)->int:

        costo_total = 0

        ingredientes = [ingredientes1, ingredientes2, ingredientes3]
        for ingrediente in ingredientes:
            costo_total += ingrediente.precio

        return costo_total

    @staticmethod
    def rentabilidad_x_producto(precio:int, ingredientes1:dict, ingredientes2:dict, ingredientes3:dict)->int:

        costo_total = Funciones.costo_produccion(ingredientes1, ingredientes2, ingredientes3)
        rentabilidad = precio - costo_total
        return rentabilidad

    @staticmethod
    def producto_mas_rentable(productos1:dict, productos2:dict, productos3:dict, productos4:dict)->str:

        valor_rentabilidad = 0
        nombre_producto = ''

        productos = [productos1, productos2, productos3, productos4]
        for producto in productos:
            if valor_rentabilidad < producto.rentabilidad:
                valor_rentabilidad = producto.rentabilidad
                nombre_producto = producto.nombre

        return nombre_producto


