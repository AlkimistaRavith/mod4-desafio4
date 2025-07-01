class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock >= 0 else 0

    # Getter para nombre y precio (sin setter porque no se modifican.)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    # Getter y setter para stock (para las modificaciones en venta e ingresos.)
    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock):
        if nuevo_stock >= 0:
            self.__stock = nuevo_stock
        else:
            self.__stock = 0

    # Método para modificar el stock (sumar o restar)
    def modificar_stock(self, cantidad):
        self.stock = self.__stock + cantidad

    # Sobrecarga de igualdad: compara por nombre de producto.
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre.lower() == other.nombre.lower()
        return False

    # Sobrecarga de suma: suma stock de un producto con sobrecarga de igualdad, sin modificar el precio.
    def __add__(self, other):
        if self == other:
            nuevo_stock = self.stock + other.stock
            return Producto(self.nombre, self.precio, nuevo_stock)
        return self

    # Sobrecarga de resta: para restar stock en ventas
    def __sub__(self, cantidad):
        if isinstance(cantidad, int):
            self.stock = self.stock - cantidad
        return self

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"


#PRUEBA
if __name__ == "__main__":
        
    p1 = Producto("Pan", 500, 10)
    print(p1.nombre)       # Pan
    print(p1.precio)       # 500
    print(p1.stock)        # 10

    p1.stock = 15          # Cambia el stock a 15
    p1.modificar_stock(-20) # Baja el stock a 10
    print(p1)              # Pan - $500 - Stock: 10