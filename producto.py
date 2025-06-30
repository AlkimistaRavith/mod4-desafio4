class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        #Stock será 0 si se ingresa un valor negativo.
        self.__stock = stock if stock >= 0 else 0

    # Getters (encapsulamiento: solo lectura pública)
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    # Método para modificar el stock
    def modificar_stock(self, cantidad):
        nuevo_stock = self.__stock + cantidad
        self.__stock = nuevo_stock if nuevo_stock >= 0 else 0

    # Sobrecarga de igualdad: compara por nombre
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.__nombre.lower() == other.obtener_nombre().lower()
        return False

    # Sobrecarga de suma: suma stock (precio no cambia)
    def __add__(self, other):
        if self == other:
            nuevo_stock = self.__stock + other.obtener_stock()
            return Producto(self.__nombre, self.__precio, nuevo_stock)
        return self

    # Sobrecarga de resta: resta stock
    def __sub__(self, cantidad):
        if isinstance(cantidad, int):
            nuevo_stock = self.__stock - cantidad
            self.__stock = nuevo_stock if nuevo_stock >= 0 else 0
        return self

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio} - Stock: {self.__stock}"



#PRUEBA
if __name__ == "__main__":
    p1 = Producto("Pan", 1000, 5)
    p2 = Producto("Pan", 1000, 3)
    p3 = p1 + p2
    print(p3)  # Pan - $1000 - Stock: 8

    p3 - 2
    print(p3.obtener_stock())  # 6

    p3.modificar_stock(-10)
    print(p3.obtener_stock())  # 0