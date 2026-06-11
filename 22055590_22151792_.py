import matplotlib.pyplot as plt
import os
import csv
ARCHIVO_SERVICIOS="servicios.txt"
ARCHIVO_CLIENTES="clientes.txt"

#Este es un iniciador del archivo tanto de clientes como servicios
def inicializar_archivos():
    if not os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "w") as f:
            pass
    if not os.path.exists(ARCHIVO_SERVICIOS):
        with open(ARCHIVO_SERVICIOS, "w") as f:
            pass
#este es un auxiliar para guardar los diccionarios dentro de los archivos
def guardar_dato(nombre_archivo, diccionario):
    # Convertimos los valores del diccionario a una lista de textos y los unimos con ";"
    valores = [str(val) for val in diccionario.values()]
    linea = ";".join(valores) + "\n"
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write(linea)

def ingresar_cliente():
    print("\n--- INGRESO DE DATOS DE CLIENTE ---")
    #utilizamos el input para ingresar los datos del cliente
    rut = input("Introduzca su Rut: ")
    nombres = input("Introduzca su Nombres: ")
    apellido_p = input("Introduzca su Apellido paterno: ")
    apellido_m = input("Introduzca su Apellido materno: ")
    telefono = input("Introduzca su Teléfono: ")
    email = input("Introduzca su Email: ")
    empresa = input("Introduzca su Empresa: ")
    #
    while True:
        presupuesto = input("Presupuesto disponible: ")
        if presupuesto.isdigit(): #analiza los numeros ingresados y verifica que sean enteros
            presupuesto=float(presupuesto)
            break #interrumpe el ciclo del presupuesto al ser valido
        else:#en caso de no ser valido mostraria el siguiente mensaje
            print("ERROR, ingrese un valor numérico válido.")
    #en este diccionario estan las claves con los valores que corresponden a los datos del cliente
    cliente = {
        "rut": rut, "nombres": nombres, "apellido_paterno": apellido_p,
        "apellido_materno": apellido_m, "telefono": telefono, "email": email,
        "empresa": empresa, "presupuesto": presupuesto
    }
    guardar_dato(ARCHIVO_CLIENTES, cliente)#aqui se guarda el diccionario "cliente" dentro del ARCHIVO_CLIENTES
    print("¡Cliente registrado con éxito!")


def ingresar_servicio():
    print("--- INGRESO DE SERVICIOS DE CONSULTORÍA ---")
    #pasaremos a verificar que el usuario este registrado, para saber cuanto es su presupuesto
    rut= input("Ingrese el Rut del cliente que contrata el servicio:")
    detec = open(ARCHIVO_CLIENTES, "r")
    for linea in detec:
        datos = linea.strip().split(";")
        if datos[0] == rut:
            presupuesto = float(datos[7])
            break
    detec.close()
        else:
            print("Error: El Rut del cliente no existe en el sistema.")
            return
    
    #el usuario debera ingresar los datos del servicio que quiere costear
    cod = input("Introduzca el Código del servicio: ")
    nom_ser = input("Introduzca el Nombre del servicio: ")
    area = input("Introduzaca el Área de consultoría: ")
    consultor = input("Introduzaca el Consultor responsable: ")
    duracion = input("Introduzaca la Duración estimada (ej: 3 meses): ")
     

    while True:
        costo1 = (input("Costo del servicio:$ ")
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
        "RUT": rut”, "Código del servicio": cod, "Nombre del servicio": nom_ser, "Área de consultoría": area,
        "Consultor responsable": consultor, "Duracion estimada":duracion, "Costo del servicio": costo,
        "Observacion": observacion
    }
    guardar_dato(ARCHIVO_SERVICIOS, servicio)
    print("¡Servicio contratado y registrado con éxito!")


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
