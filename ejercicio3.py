from re import I


banco = {}

def menu():
    print("Menú")
    print("1. Ingresar un cliente")
    print("2. Informacion de la cuenta")
    print("3. Consultar saldo")
    print("4. Ingresar dinero")
    print("5. Retirar dinero")
    print("0. salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion != 0:
        if opcion == 1:
            ingresarCliente()
            
def ingresarCliente():
    banco["nombre"] = input("Ingrese el nombre: ")
    banco["apellido"] = input("Ingrese el apellido: ")
    banco["cedula"] = input("Ingrese la cedula: ")
    banco["ciudad"] = input("Ingrese la ciudad: ")
    banco["cuenta"] =[input("Ingrese el número de la cuenta: "), input("Saldo: ")]

    print("Se agregó un nuevo cliente.")
    opt = int(input("Desea seguir con el menu: (1. Si, 2. No)"))