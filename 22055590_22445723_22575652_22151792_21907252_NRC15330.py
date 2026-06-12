import matplotlib.pyplot as plt
import os
ARCHIVO_SERVICIOS="servicios.txt"
ARCHIVO_CLIENTES="clientes.txt"

class Cliente():

    """ 
        Representa a un cliente del sistema de consultoría.
    Almacena sus datos de contacto y el presupuesto disponible.
    """

    def __init__(self, rut, nombres, apellido_paterno, apellido_materno, telefono, email, empresa, presupuesto):
        self.rut = rut
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.email = email
        self.empresa = empresa
        self.presupuesto = presupuesto

class Servicio():

    """
        Representa un servicio de consultoría contratado.
        Guarda los detalles operativos, el costo y el RUT del cliente asociado.
    """

    def __init__(self, cod, nom_ser, area, consultor, duracion, costo, observacion, rut_cliente):
        self.codigo = cod
        self.nombre = nom_ser
        self.area = area
        self.consultor = consultor
        self.duracion = duracion
        self.costo = costo
        self.observacion = observacion
        self.rut_cliente = rut_cliente

def inicializar_archivos():
    """
        Crea los archivos de texto si no existen en el sistema.
    """
    if not os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "w") as f:
            pass
    if not os.path.exists(ARCHIVO_SERVICIOS):
        with open(ARCHIVO_SERVICIOS, "w") as f:
            pass


def ingresar_cliente():
    """ 
    Solicita los datos de un nuevo cliente y los guarda en el archivo.
    Verifica que el presupuesto reciba un numero entero.
    """
    print("Ingrese los siguientes datos")
    #utilizamos el input para ingresar los datos del cliente
    rut = input("Rut: ")
    nombres = input("Nombres: ")
    apellido_p = input("Apellido paterno: ")
    apellido_m = input("Apellido materno: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    empresa = input("Empresa: ")

    while True:
        try:
            presupuesto = float(input("Presupuesto disponible: "))
            break # Interrumpe el ciclo del presupuesto al ser valido
        except ValueError: # Si el usuario ingresa texto en lugar de un número
            print("ERROR, ingrese un valor numérico válido.")
    nuevo_cliente = Cliente(rut, nombres, apellido_p, apellido_m, telefono, email, empresa, presupuesto)
    
    linea_texto = f"{nuevo_cliente.rut};{nuevo_cliente.nombres};{nuevo_cliente.apellido_paterno};{nuevo_cliente.apellido_materno};{nuevo_cliente.telefono};{nuevo_cliente.email};{nuevo_cliente.empresa};{nuevo_cliente.presupuesto}\n"

    with open(ARCHIVO_CLIENTES, "a", encoding="utf-8") as f:
        f.write(linea_texto)
        
    print("¡Cliente registrado con éxito!")


def ingresar_servicio():
    """
    Solicita los datos de un servicio. Verifica que el rut corresponda al de
    un cliente ya registrado, verifica que el presupuesto y tiempo de ejecución
    del servicio se ingresen como valores enteros validos, y que el costo
    sea menor o igual al presupuesto.
    Ingresa los datos al archivo de servicios.
    """
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
        except ValueError: #Si no se ingresa un entero
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

    nuevo_servicio = Servicio(cod, nom_ser, area, consultor, duracion, costo1, observacion, rut)
    
    # 2. Armamos la línea de texto extrayendo cada atributo del objeto
    linea_texto = f"{nuevo_servicio.codigo};{nuevo_servicio.nombre};{nuevo_servicio.area};{nuevo_servicio.consultor};{nuevo_servicio.duracion};{nuevo_servicio.costo};{nuevo_servicio.observacion};{nuevo_servicio.rut_cliente}\n"
    
    # 3. Guardamos esa línea directamente en el archivo
    with open(ARCHIVO_SERVICIOS, "a", encoding="utf-8") as f:
        f.write(linea_texto)
    print("¡Servicio contratado y registrado con éxito!")



def visualizar_cliente(archivo=ARCHIVO_CLIENTES):
    """
    Si el archivo de clientes existe, lo abre y con un for lo recorre para sacar
    los datos y mostrarlos al usuario en orden.
    Si no existe, retorna al menu principal enviando un mensaje segun el error.
        """
    print("\n--- VISUALIZACIÓN DE CLIENTES ---")
    try:
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
    except FileNotFoundError:
        print("El archivo de clientes no existe. Ingrese un clliente.")

def visualizar_servicios(archivo=ARCHIVO_SERVICIOS):
    """
    Esta funcion revisa que exista el archivo de servicios, si existe, lo lee 
    y recorre con un for para mostrar los servicios al usuario.
    Si no existe, retorna un mensaje de error.
    """
    print("\n========================================")
    print("Visualización de los datos de las consultorías")
    print("========================================\n")
    try:
        with open(archivo, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            
            if not lineas:
                print("No hay servicios registrados en el sistema.")
                return

            for linea in lineas:
                datos = linea.strip().split(";")
                if len(datos) == 8:
                    rut, codigo, nombre, area, consultor, duracion, costo, observacion = datos
                    print(f"Rut: {rut}")
                    print(f"Código del servicio: {codigo}")
                    print(f"Nombre del servicio: {nombre}")
                    print(f"Área de consultoría: {area}")
                    print(f"Consultor responsable: {consultor}")
                    print(f"Duración estimada: {duracion}")
                    print(f"Costo del servicio: {costo}")
                    print(f"Observación: {observacion}")
                    print("-" * 40) 
                else:
                    continue
    except FileNotFoundError:
        print("Error: El archivo de servicios no existe. Registre un servicio primero.")
    except Exception as e: # captura cualquier otro error inesperado del sistema
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")


    
def mostrar_grafico(archivo=ARCHIVO_CLIENTES):
    """
    Genera un gráfico de barras interactivo con los presupuestos de los clientes.
    Verifica que exista el archivo clientes, si es así, lo lee y recopila tres datos,
    guarda el nombre en la lista para el eje x, guarda el presupuesto en la lista del eje y.
    Si no existe, imprime un error y pide ingresar clientes.
    """
    ejex_nombres = []
    ejey_presp = []

    try:
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
    except FileNotFoundError:
        print("No se encontró el archivo para generar el grafico. Ingrese clientes.")

def main():
    """
    Función principal para controlar el memú interactivo de la aplicación.
    Utiliza try-except para comprobar que se ingresen opciones validas en 
    el menú principal.
    """
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


#Integrantes:
# Carla Campos - 22.055.590-9
# Vicente Duarte - 22.151.792-K
# Antonia Hernández - 22.445.723-5
# Lukas Ortiz - 21.907.252-K
# Antonia Roca - 22.575.652-K