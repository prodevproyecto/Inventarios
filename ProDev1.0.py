import os
import uuid


inventario = {}

#limpiar






#Opcion 1 resgistrar producto













#Opcion 2 inventario de productos
















#Opcion 3 entrada de productos



















#Opcion 4 salida de productos




















#Salir
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

    