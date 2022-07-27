import csv

archivoCSV=open('empleados.csv')
entrada = csv.DictReader(archivoCSV)
salidaCSV = open('mujeres-1965.csv', 'w')
salida = csv.writer(salidaCSV, delimiter=',')

print('Escribiendo archivo de salida...')

# encabezado
salida.writerow(["fecha", "nombre","apellido"])

for reg in entrada:
   fecha = reg['birth_date'].split("-")
   if reg['gender'] == "F" and fecha[0]=="1965" :
      salida.writerow([reg['birth_date'],reg['first_name'], reg['last_name']]) # Escribir registro

print('El proceso de escritura ha terminado.')
del entrada, salida, reg
salidaCSV.close()
del salidaCSV
