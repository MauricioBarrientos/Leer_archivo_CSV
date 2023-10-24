import csv

def leer_archivo_csv(nombre_archivo):
    datos = []

    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)

        # Lee y procesa cada fila del archivo CSV
        for fila in lector_csv:
            datos.append(fila)  # Agrega la fila a la lista de datos

    return datos


# Ejemplo de uso
nombre_archivo = 'AgentesRetenedores.csv'  # Reemplaza 'datos.csv' con el nombre de tu archivo CSV
datos = leer_archivo_csv(nombre_archivo)

# Imprime los datos obtenidos del archivo CSV
for fila in datos:
    print(fila)