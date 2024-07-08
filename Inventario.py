
nombres = {}
cantidades = {}
precios = {}
numRepuestos = 0

# Productos 
productos_predefinidos = [
    {"nombre": "Aceite", "cantidad": 10, "precio": 20.0},
    {"nombre": "Filtro de Aire", "cantidad": 15, "precio": 10.0},
    {"nombre": "Bujía", "cantidad": 30, "precio": 5.0},
    {"nombre": "Amortiguador", "cantidad": 5, "precio": 50.0},
    {"nombre": "Llantas", "cantidad": 20, "precio": 100.0}
]

# Función para inicializar los productos 
def inicializarProductos():
    global nombres, cantidades, precios, numRepuestos
    for producto in productos_predefinidos:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio"]
        nombres[nombre] = nombre
        cantidades[nombre] = cantidad
        precios[nombre] = precio
        numRepuestos += 1

# Función para imprimir el menú
def imprimirMenu():
    print("\n=== Menú ===")
    print("1. Ingresar nuevo repuesto")
    print("2. Editar repuesto")
    print("3. Eliminar repuesto")
    print("4. Listar repuestos")
    print("5. Calcular total de dinero")
    print("6. Salir")
    print("============")

# Función para ingresar un nuevo repuesto
def ingresarRepuesto():
    global numRepuestos, nombres, cantidades, precios
    if numRepuestos >= 20:
        print("Error: inventario lleno.")
        return

    nombre = input("Ingrese el nombre del repuesto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))

    # Verificar si el repuesto ya existe
    if nombre in nombres:
        cantidades[nombre] += cantidad
        print(f"Cantidad actualizada correctamente para '{nombre}'.")
    else:
        nombres[nombre] = nombre
        cantidades[nombre] = cantidad
        precios[nombre] = precio
        numRepuestos += 1
        print(f"Repuesto '{nombre}' ingresado correctamente.")

# Función para editar un repuesto
def editarRepuesto():
    global nombres, cantidades
    nombreEditar = input("Ingrese el nombre del repuesto a editar: ")

    if nombreEditar in nombres:
        nuevaCantidad = int(input("Ingrese la nueva cantidad: "))
        cantidades[nombreEditar] = nuevaCantidad
        print(f"Repuesto '{nombreEditar}' editado correctamente.")
    else:
        print(f"Repuesto '{nombreEditar}' no encontrado.")

# Función para eliminar un repuesto
def eliminarRepuesto():
    global numRepuestos, nombres, cantidades, precios
    if numRepuestos == 0:
        print("No hay repuestos para eliminar.")
        return

    nombreEliminar = input("Ingrese el nombre del repuesto a eliminar: ")

    if nombreEliminar in nombres:
        cantidadEliminar = int(input(f"Ingrese la cantidad de '{nombreEliminar}' a eliminar: "))
        if cantidadEliminar > 0 and cantidadEliminar <= cantidades[nombreEliminar]:
            cantidades[nombreEliminar] -= cantidadEliminar
            if cantidades[nombreEliminar] == 0:
                del nombres[nombreEliminar]
                del cantidades[nombreEliminar]
                del precios[nombreEliminar]
                numRepuestos -= 1
                print(f"Repuesto '{nombreEliminar}' eliminado completamente del inventario.")
            else:
                print(f"{cantidadEliminar} unidades de '{nombreEliminar}' eliminadas correctamente.")
        else:
            print(f"Cantidad inválida o no hay suficientes unidades de '{nombreEliminar}' en el inventario.")
    else:
        print(f"Repuesto '{nombreEliminar}' no encontrado en el inventario.")

# Función para listar todos los repuestos
def listarRepuestos():
    global nombres, cantidades, precios
    print("\n=== Inventario de Repuestos ===")
    for nombre, cantidad in cantidades.items():
        print(f"Nombre: {nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio: {precios[nombre]:.2f}")
        print(f"Total: {cantidad * precios[nombre]:.2f}")
        print("-----------------------------")
    print(f"Total de repuestos: {numRepuestos}")
    print("==============================")

# Función para calcular el total de dinero en el inventario
def calcularTotalDinero():
    global cantidades, precios
    total = 0
    for nombre, cantidad in cantidades.items():
        total += cantidad * precios[nombre]
    return total

# Función principal
def main():
    inicializarProductos()  # Inicializar productos predefinidos al inicio del programa
    opcion = 0
    while opcion != 6:
        imprimirMenu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                ingresarRepuesto()
            elif opcion == 2:
                editarRepuesto()
            elif opcion == 3:
                eliminarRepuesto()
            elif opcion == 4:
                listarRepuestos()
            elif opcion == 5:
                print(f"El total de dinero en el inventario es: {calcularTotalDinero():.2f}")
            elif opcion == 6:
                print("Saliendo del programa...")
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()

