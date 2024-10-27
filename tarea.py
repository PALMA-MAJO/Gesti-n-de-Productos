import os

productos = []

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for linea in file:
                try:
                    nombre, precio, cantidad = linea.strip().split(", ")
                    productos.append({
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    })
                except ValueError:
                    print("Error al cargar datos, verifica el formato del archivo.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")
    print("Datos guardados exitosamente.")

def añadir_producto():
    nombre = input("Nombre del producto: ")
    
    
    while True:
        precio_input = input("Precio del producto: ")
        try:
            precio = float(precio_input)
            if precio < 0:
                print("El precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: Ingresa un número válido para el precio.")
    
    while True:
        cantidad_input = input("Cantidad del producto: ")
        try:
            cantidad = int(cantidad_input)
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Error: Ingresa un número válido para la cantidad.")
    
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        for i, producto in enumerate(productos, start=1):
            print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print("Producto encontrado. Ingresa los nuevos valores (deja en blanco para mantener el valor actual).")
            
            # Actualizar nombre
            nuevo_nombre = input("Nuevo nombre: ") or producto["nombre"]
            
            while True:
                nuevo_precio_input = input("Nuevo precio: ")
                if nuevo_precio_input == "":
                    nuevo_precio = producto["precio"]
                    break
                try:
                    nuevo_precio = float(nuevo_precio_input)
                    if nuevo_precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        break
                except ValueError:
                    print("Error: Ingresa un número válido para el precio.")
        
            while True:
                nueva_cantidad_input = input("Nueva cantidad: ")
                if nueva_cantidad_input == "":
                    nueva_cantidad = producto["cantidad"]
                    break
                try:
                    nueva_cantidad = int(nueva_cantidad_input)
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    else:
                        break
                except ValueError:
                    print("Error: Ingresa un número válido para la cantidad.")
            
            producto.update({
                "nombre": nuevo_nombre,
                "precio": nuevo_precio,
                "cantidad": nueva_cantidad
            })
            print("Producto actualizado exitosamente.")
            return
    print("Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("Producto no encontrado.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()  
            break
        else:
            print("Por favor, selecciona una opción válida.")


if __name__ == "__main__":
    menu()