import csv

# Abrir el archivo CSV
with open("pregunta.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila como una lista