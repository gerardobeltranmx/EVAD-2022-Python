# Leer un archivo csv como lista de diccionarios con
# DictReader() y mostrar sólo datos de algunas columnas:

import csv

archivoCSV=open('municipios.csv')

entrada = csv.DictReader(archivoCSV)

for reg in entrada:
	print("%-20s - %8s" % (reg['nombre'], reg['poblacion']))

