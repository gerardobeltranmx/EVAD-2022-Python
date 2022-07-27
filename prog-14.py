# Muestra lista de diccionarios a partir CSV y
# consultar número de líneas (registros), dialecto y campos:
import csv

archivoCSV = open('municipios.csv')

entrada = csv.DictReader(archivoCSV)

listadicc = list(entrada) # Obtener lista de diccionarios

print('Lista:', listadicc) # Mostrar lista de diccionarios

print('Líneas:', entrada.line_num) # Obtener número de registros

print('Dialecto:', entrada.dialect) # Obtener dialecto

print('Campos:', entrada.fieldnames) # Obtener nombre de campos

del entrada, listadicc

archivoCSV.close()

del archivoCSV

