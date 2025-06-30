from abc import ABC, abstractmethod
from producto import Producto

class Tienda(ABC):
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self._productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    @abstractmethod
    def ingresar_producto(self):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self):
        pass

    # Método auxiliar común para encontrar productos
    def _buscar_producto(self, nombre_producto):
        for p in self._productos:
            if p.obtener_nombre().lower() == nombre_producto.lower():
                return p
        return None



#RESTAURANTE
class Restaurante(Tienda):
    def ingresar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        producto = Producto(nombre, precio, 0)

        existente = self._buscar_producto(nombre)
        if existente:
            print("Producto ya existe. No se modifica stock (siempre es 0 en Restaurante).")
        else:
            self._productos.append(producto)

    def listar_productos(self):
        salida = f"Productos del Restaurante {self.nombre}:\n"
        for p in self._productos:
            salida += f"- {p.obtener_nombre()} - ${p.obtener_precio()}\n"
        return salida

    def realizar_venta(self):
        nombre = input("Producto a vender: ")
        cantidad = int(input("Cantidad (sin efecto real): "))
        producto = self._buscar_producto(nombre)
        if producto:
            print(f"Venta registrada de {cantidad} unidades de {nombre}")
        else:
            print("Producto no encontrado.")


#SUPERMERCADO
class Supermercado(Tienda):
    def ingresar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Stock inicial: "))
        nuevo = Producto(nombre, precio, stock)

        existente = self._buscar_producto(nombre)
        if existente:
            existente.modificar_stock(stock)
        else:
            self._productos.append(nuevo)

    def listar_productos(self):
        salida = f"Productos del Supermercado {self.nombre}:\n"
        for p in self._productos:
            stock = p.obtener_stock()
            alerta = " - Pocos productos disponibles" if stock < 10 else ""
            salida += f"- {p.obtener_nombre()} - ${p.obtener_precio()} - Stock: {stock}{alerta}\n"
        return salida

    def realizar_venta(self):
        nombre = input("Producto a vender: ")
        cantidad = int(input("Cantidad: "))
        producto = self._buscar_producto(nombre)

        if producto and producto.obtener_stock() > 0:
            vendido = min(cantidad, producto.obtener_stock())
            producto - vendido
            print(f"Venta realizada de {vendido} unidades de {nombre}")
        else:
            print("Producto no disponible o sin stock.")


#FARMACIA
class Farmacia(Tienda):
    def ingresar_producto(self):
        nombre = input("Nombre del producto: ")
        precio = int(input("Precio del producto: "))
        stock = int(input("Stock inicial: "))
        nuevo = Producto(nombre, precio, stock)

        existente = self._buscar_producto(nombre)
        if existente:
            existente.modificar_stock(stock)
        else:
            self._productos.append(nuevo)

    def listar_productos(self):
        salida = f"Productos de la Farmacia {self.nombre}:\n"
        for p in self._productos:
            precio = p.obtener_precio()
            promo = " - Envío gratis al solicitar este producto" if precio > 15000 else ""
            salida += f"- {p.obtener_nombre()} - ${precio}{promo}\n"
        return salida

    def realizar_venta(self):
        nombre = input("Producto a vender: ")
        cantidad = int(input("Cantidad (máx 3): "))
        if cantidad > 3:
            print("No se pueden vender más de 3 unidades por venta.")
            return

        producto = self._buscar_producto(nombre)
        if producto and producto.obtener_stock() > 0:
            vendido = min(cantidad, producto.obtener_stock())
            producto - vendido
            print(f"Venta realizada de {vendido} unidades de {nombre}")
        else:
            print("Producto no disponible o sin stock.")