from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    print("Elige el tipo de tienda:")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")

    opcion = input("Opción (1/2/3): ")
    nombre = input("Nombre de la tienda: ")
    costo = int(input("Costo de delivery: "))

    if opcion == "1":
        return Restaurante(nombre, costo)
    elif opcion == "2":
        return Supermercado(nombre, costo)
    elif opcion == "3":
        return Farmacia(nombre, costo)
    else:
        print("Opción inválida.")
        return crear_tienda()

def menu_tienda(tienda):
    while True:
        print("\n--- MENÚ ---")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            tienda.ingresar_producto()
        elif opcion == "2":
            print(tienda.listar_productos())
        elif opcion == "3":
            tienda.realizar_venta()
        elif opcion == "4":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    print("Bienvenido al sistema de tiendas.")
    tienda = crear_tienda()
    menu_tienda(tienda)