import matplotlib.pyplot as plt
import os
import csv

def ingresar_cliente():
    cliente = input("")
    return cliente

def ingresar_servicio():
    servicio = input("...")
    return servicio

def visualizar_cliente(cliente):
    print(cliente)

def visualizar_servicios(servicio):
    print(servicio)

def mostrar_grafico(clientes):
    ejex_nombres = []
    ejey_presp = []

    for cliente in clientes:
        nombre = f"{cliente[1]} {cliente[2]}"
        ejex_nombres.append(nombre)
        ejey_presp.append(cliente[7])

    plt.figure(figsize = (10,6))
    plt.bar(ejex_nombres, ejey_presp, color = "steelblue")
    plt.title("Grafico de Barras")
    plt.ylabel("Presupuesto disponible")
    plt.xlabel("Clientes")
    plt.tight_layout
    plt.show()

while True:
    print("\tSISTEMA DE CONSULTORIA GENERAL")
    print("1. Ingresar datos de clientes")
    print("2. Ingresar servicios de consultoria")
    print("3. Visualizar datos de clientes")
    print("4. Visualizar servicios registrados")
    print("5. Visualizar gráfico del presupuesto disponible de los clientes")
    print("6. Salir del programa")

    try:
        op = int(input("Seleccione una opción:  "))
        
        if op ==1:
            client = ingresar_cliente()

        elif op ==2:
            serv = ingresar_servicio()

        elif op ==3:

            visualizar_cliente(client)

        elif op ==4: visualizar_servicios(serv)

        elif op ==5:
            mostrar_grafico()

        elif op ==6:
            print("Saliendo del programa...")
            break

        else:
            print("Ingrese una opción valida (1-6).")

    except ValueError:
        print("Opcion no valida, intente otra vez con un numero entero (1-6).")
    