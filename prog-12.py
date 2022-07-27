import csv
# Leer un archivo y lo mostrar ordenado por segundo
# campo numérico con notación lambda

archivoCSV = csv.reader(open('municipios.csv'))
# salta el encabezado
next(archivoCSV, None)

listaordenada = sorted(archivoCSV, key=lambda x: int(x[1]),
		reverse=True)

for municipio in listaordenada:
	print("%-20s - %08d" % (municipio[0], int(municipio[1])))
