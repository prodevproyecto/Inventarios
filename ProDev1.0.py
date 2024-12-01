import os
import uuid


inventario = {}

def limpiar():
    os.system("cls")

def Registrar_producto():
        codigo = str(uuid.uuid1(4))
        descripcion = str(input("Descripcion del producto: "))
        precio = float(input("Valor del producto [Unidad]: "))
        stock = int(input("Ingrese la cantidad del producto: "))

        inventario[codigo] = {"Descripcion": descripcion , "Precio": precio,  "Stock": stock}

        print(inventario)
        print("El producto se registro exitosamente...")


def Inventario_productos():
    if not inventario:
        print("El inventario está vacío")
        return
    print("Inventario de Productos")
    for codigo, informacion in inventario.items():
        print(f"Código: {codigo}")
        print(f"  Descripción: {informacion['Descripcion']}")
        print(f"  Precio: ${informacion['Precio']}")
        print(f"  Stock: {informacion['Stock']}")


def Entrada_productos ():
    codigoBusqueda = input("Ingrese el codigo del producto: ")
    if codigoBusqueda in inventario:
            cantidadIngresada = int(input("Cantidad a ingresar del producto: "))
            inventario[codigoBusqueda]["Stock"] += cantidadIngresada
            print(inventario)
            print("Se actualizo el stock..")
    else:
            print("Producto no encontrado, No se actualizo el stock...")

def Salida_productos():
    codigo = input("Ingrese el codigo del producto: ")
    if codigo != codigo:
        print("No se puede registra la salida de un producto que no existe")
    else:      
        cantidaSalidad = int(input("Cantidad vendida del poducto: "))
    if codigo in inventario :
        inventario[codigo]["Stock"] -= cantidaSalidad
        total = cantidaSalidad * inventario[codigo]["Precio"]
        with open("recibo.txt", "w") as archivo:
            archivo.write("RECIBO DE VENTA\n")
            archivo.write(f"Producto: {inventario[codigo]["Descripcion"]}\n")
            archivo.write(f"Cantidad: {cantidaSalidad}\n")
            archivo.write(f"Precio unitario: ${inventario[codigo]["Precio"]}\n")
            archivo.write(f"Total: ${total}\n")
        
        print("La compra se realizó con éxito. Recibo generado en 'recibo.txt'.")

def salir():
     print("Saliendo del programa...")

def menuPrincipal():
    print("1 - Registrar producto: ")
    print("2 - Inventario de productos: ")
    print("3 - Entrada de productos: ")
    print("4 - Salida de productos: ")
    print("5 - Salir...")


while True:
    menuPrincipal()
    op = int(input("Eliga la opcion a realizar: "))
    limpiar()
    if op == 1:
        Registrar_producto()
    elif op == 2:
        Inventario_productos()
    elif op == 3:
        Entrada_productos()
    elif op == 4:
        Salida_productos()
    elif op == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
    input("Presione Enter para continuar...")

    