import matplotlib.pyplot as plt
import os
import csv

def ingresar_cliente():
    print("Ingreso de cliente nuevo:")
    rut = input("RUT:   ")
    nombre = input("Nombre: ")
    apellido_p = input("Apellido paterno:   ")
    apellido_m = input("Apellido materno:   ")
    presupuesto = int(input("Presupuesto disponible:    "))
    cliente = [rut, nombre, apellido_p, apellido_m, "9999","correo@gmail.com", "Empresa SPA", presupuesto]

    return cliente

def ingresar_servicio():
<<<<<<< Updated upstream
    cod = input("service code:  ")
    nombre_serv = input("Nombre serv")
    costo = int(input("Costo:   "))
    servicio = [cod, nombre_serv, "Area","Consultor", "10 hrs", costo, "Sin observaciones"]
=======
    print("--- INGRESO DE SERVICIOS DE CONSULTORÍA ---")
    #pasaremos a verificar que el usuario este registrado, para saber cuanto es su presupuesto
    rut= input("Ingrese el Rut del cliente que contrata el servicio:")
    detec = open(ARCHIVO_CLIENTES, "r")
    for linea in detec:
        datos = linea.strip().split(";")
        if datos[0] == rut:
            presupuesto = float(datos[7])
            break
        else:
            print("Error: El Rut del cliente no existe en el sistema.")
            detec.close()
            return
    detec.close()
    
    #el usuario debera ingresar los datos del servicio que quiere costear
    cod = input("Introduzca el Código del servicio: ")
    nom_ser = input("Introduzca el Nombre del servicio: ")
    area = input("Introduzaca el Área de consultoría: ")
    consultor = input("Introduzaca el Consultor responsable: ")
    duracion = input("Introduzaca la Duración estimada (ej: 3 meses): ")
    

    while True:
        costo1 = int(input("Costo del servicio:$ "))
        if costo1.isdigit(): 
            costo=float(costo1)
            break
        else:
            print("ERROR, ingrese un valor numérico válido (ej:50000): $")

    if costo > presupuesto:
        print(f"El servicio no se puede ejecutar debido a que  el costo{costo} supera su presupuesto{presupuesto}")
        return
    else:
        print(f"Su presupuesto disponible es de {presupuesto}, el costo del servicio a contratar es de {costo}")
        
    observacion = input("Observación: ")  

    servicio = {
        "RUT": rut, "Código del servicio": cod, "Nombre del servicio": nom_ser, "Área de consultoría": area,
        "Consultor responsable": consultor, "Duracion estimada":duracion, "Costo del servicio": costo,
        "Observacion": observacion
    }
    guardar_dato(ARCHIVO_SERVICIOS, servicio)
    print("¡Servicio contratado y registrado con éxito!")
>>>>>>> Stashed changes

    return servicio

def visualizar_cliente(lista_clientes):
    print("\n--- VISUALIZACIÓN DE CLIENTES ---")
    if len(lista_clientes) == 0:
        print("No hay clientes registrados aún.")
    else:
        for c in lista_clientes:
            print(f"Rut: {c[0]} | Nombre: {c[1]} {c[2]} | Presupuesto: ${c[7]}")

def visualizar_servicios(lista_servicios):
    print("\n--- VISUALIZACIÓN DE SERVICIOS ---")
    if len(lista_servicios) == 0:
        print("No hay servicios registrados aún.")
    else:
        for s in lista_servicios:
            print(f"Código: {s[0]} | Servicio: {s[1]} | Costo: ${s[5]}")

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
    plt.tight_layout()
    plt.show()

def main():
    clientes = []
    servicios = []
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
                clientes.append(ingresar_cliente())

            elif op ==2:
                servicios.append(ingresar_servicio())

            elif op ==3:
                if len(clientes) != 0:
                    visualizar_cliente(clientes)
                else:
                    print("Falta ingresar datos de clientes.")

            elif op ==4: 
                if len(servicios) != 0:
                    visualizar_servicios(servicios)
                else:
                    print("Faltan servicios por ingresar.")

            elif op ==5:
                mostrar_grafico(clientes)

            elif op ==6:
                print("Saliendo del programa...")
                break

            else:
                print("Ingrese una opción valida (1-6).")

        except ValueError:
            print("Opcion no valida, intente otra vez con un numero entero (1-6).")
        
main()