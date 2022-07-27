# Leer con DictReader y escribir datos en otro csv si se
# cumple condición.
# En el archivo 'salida.csv' se escribirán todos los datos
# con el carácter “;".
import csv

archivoCSV=open('municipios.csv')
entrada = csv.DictReader(archivoCSV)
salidaCSV = open('salida.csv', 'w')
salida = csv.writer(salidaCSV, delimiter=';')

print('Escribiendo archivo "salida.csv"...')

salida.writerow(["nombre","poblacion"])

for reg in entrada:
   if int(reg['poblacion']) > 200000:
      salida.writerow([reg['nombre'], reg['poblacion']]) # Escribir registro

print('El proceso de escritura ha terminado.')
del entrada, salida, reg
salidaCSV.close()
del salidaCSV
