import os

def crear_archivo_inicial():
    if not os.path.exists("productos.txt"):
        with open("productos.txt", "w") as archivo:
            
            archivo.write("Lapicera,120.5,30\n")
            archivo.write("Cuaderno,350.0,15\n")
            archivo.write("Goma,80.0,50\n")

def cargar_productos():
    productos = []
    with open("productos.txt", "r") as archivo:
        
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })
    return productos

def mostrar_productos(productos):
    print("\nPRODUCTOS EN STOCK:")
    
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto(productos):
    print("\nAgregar un nuevo producto:")
    
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })

def buscar_producto(productos):
    nombre_buscar = input("\nIngrese el nombre a buscar: ")

    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"\nEncontrado: {p['nombre']} - Precio: ${p['precio']} - Cantidad: {p['cantidad']}")
            return
    print("\nEl producto no existe.")

def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("\nArchivo actualizado correctamente.")

def main():
    crear_archivo_inicial()

    productos = cargar_productos()
    mostrar_productos(productos)

    opcion = input("\n¿Querés agregar un producto? (s/n): ").lower()
    if opcion == "s":
        agregar_producto(productos)

    buscar_producto(productos)

    guardar_productos(productos)


#Principal
main()