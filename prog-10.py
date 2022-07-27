#!/usr/bin/python3
import csv

# Abrir archivo csv
archivoCSV = open('municipios.csv')

# Leer todos los registros
entrada = csv.reader(archivoCSV)

# Cada línea se muestra como una lista de campos
suma = 0
for registro in entrada:
  print(registro[0], registro[1])
  if registro[1]!="poblacion" :
  	suma = suma + int(registro[1])


print ("La población de sinaloa es: %d" % suma)


