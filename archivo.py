import csv
respuestas = {}

# Leer un CSV con encabezados
with open("preguntas.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["preguntas"]] = fila["respuestas"]
        # Imprime cada fila como un diccionario

    