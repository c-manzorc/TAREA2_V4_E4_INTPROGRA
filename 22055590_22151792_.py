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
    print("Ingrese los siguientes datos")
    #utilizamos el input para ingresar los datos del cliente
    rut = input("Rut: ")
    nombres = input("Nombres: ")
    apellido_p = input("Apellido paterno: ")
    apellido_m = input("Apellido materno: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    empresa = input("Empresa: ")
    #
    while True:
        try:
            presupuesto = float(input("Presupuesto disponible: "))
            break # Interrumpe el ciclo del presupuesto al ser valido
        except ValueError:
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
    print("Ingrese los siguientes datos")
    #pasaremos a verificar que el usuario este registrado, para saber cuanto es su presupuesto
    rut= input("Ingrese el Rut del cliente que contrata el servicio:")
    cliente_encontrado = False
    detec = open(ARCHIVO_CLIENTES, "r")
    for linea in detec:
        datos = linea.strip().split(";")
        if len(datos) >= 8 and datos[0] == rut:
                presupuesto = float(datos[7])
                cliente_encontrado = True
                break
    if not cliente_encontrado:
        print("Error: El Rut del cliente no existe en el sistema.")
        return
    detec.close()
    
    #el usuario debera ingresar los datos del servicio que quiere costear
    cod = input("Introduzca el Código del servicio: ")
    nom_ser = input("Introduzca el Nombre del servicio: ")
    area = input("Introduzaca el Área de consultoría: ")
    consultor = input("Introduzaca el Consultor responsable: ")
    while True:
        try:
            duracion = int(input("Introduzaca la Duración estimada en meses: "))
            break
        except ValueError:
            print("Ingrese una respuesta valida.")

    while True:
        try:
            costo1 = int(input("Costo del servicio: $ "))
            break
        except ValueError:
            print("ERROR, ingrese un valor numérico válido (ej:50000): $")

    if costo1 > presupuesto:
        print(f"El servicio no se puede ejecutar debido a que  el costo {costo1} supera su presupuesto {presupuesto}")
        return
    else:
        print(f"Su presupuesto disponible es de {presupuesto}, el costo del servicio a contratar es de {costo1}")
        
    observacion = input("Observación: ")  

    servicio = {
        "RUT: ": rut, "Código del servicio": cod, "Nombre del servicio": nom_ser, "Área de consultoría": area,
        "Consultor responsable": consultor, "Duracion estimada":duracion, "Costo del servicio": costo1,
        "Observacion": observacion
    }
    guardar_dato(ARCHIVO_SERVICIOS, servicio)
    print("¡Servicio contratado y registrado con éxito!")

    return servicio

def visualizar_cliente(archivo=ARCHIVO_CLIENTES):
    print("\n--- VISUALIZACIÓN DE CLIENTES ---")
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        if len(lineas) == 0:
            print("No hay clientes registrados aún.")
        else:
            for linea in lineas:
                datos = linea.strip().split(";")
                if len(datos) == 8:
                    print(f"Rut: {datos[0]}")
                    print(f"Nombres: {datos[1]}")
                    print(f"Apellido paterno: {datos[2]}")
                    print(f"Apellido materno: {datos[3]}")
                    print(f"Teléfono: {datos[4]}")
                    print(f"Email: {datos[5]}")
                    print(f"Empresa: {datos[6]}")
                    print(f"Presupuesto disponible: {datos[7]}")
                    print("") #Dejamos una línea en blanco para separar un cliente del siguiente


def visualizar_servicios(archivo=ARCHIVO_SERVICIOS):
    print("\n--- VISUALIZACIÓN DE CLIENTES ---")
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        if len(lineas) == 0:
            print("No hay clientes registrados aún.")
        else:
            for linea in lineas:
                datos = linea.strip().split(";")
                if len(datos) == 8:
                    print(f"Rut: {datos[0]}")
                    print(f"Código del servicio: {datos[1]}")
                    print(f"Nombre del servicio: {datos[2]}")
                    print(f"Área de consultoría: {datos[3]}")
                    print(f"Consultor responsable: {datos[4]}")
                    print(f"Duración estimada: {datos[5]}")
                    print(f"Costo del servicio: {datos[6]}")
                    print(f"Observación: {datos[7]}")
                    print("") #Se deja una línea en blanco para separar un servicio del siguiente

def mostrar_grafico(archivo=ARCHIVO_CLIENTES):
    ejex_nombres = []
    ejey_presp = []

    with open(archivo, "r", encoding="utf-8") as arch:
        lineas = arch.readlines()
        if len(lineas) == 0:
            print("No hay clientes para generar el gráfico.")
            return

        for linea in lineas:
            datos = linea.strip().split(";")
            if len(datos) >= 8:
                nombre = f"{datos[1]} {datos[2]}"
                ejex_nombres.append(nombre)
                ejey_presp.append(float(datos[7]))

    plt.figure(figsize = (10,6))
    plt.bar(ejex_nombres, ejey_presp, color = "steelblue")
    plt.title("Grafico de Barras")
    plt.ylabel("Presupuesto disponible")
    plt.xlabel("Clientes")
    plt.tight_layout()
    plt.show()

def main():
    inicializar_archivos()
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
                ingresar_cliente()

            elif op ==2:
                ingresar_servicio()

            elif op ==3:
                visualizar_cliente()

            elif op ==4: 
                visualizar_servicios()

            elif op ==5:
                mostrar_grafico()

            elif op ==6:
                print("Saliendo del programa...")
                break

            else:
                print("Ingrese una opción valida (1-6).")

        except ValueError:
            print("Opcion no valida, intente otra vez con un numero entero (1-6).")
        
main()