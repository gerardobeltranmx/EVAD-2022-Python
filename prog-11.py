# Leer un archivo y mostrarlo ordenado por primer
# campo con la función itemgetter() del módulo operator:

import csv, operator

archivoCSV = csv.reader(open('municipios.csv'))

# salta el encabezado
next(archivoCSV, None)

listaordenada = sorted(archivoCSV,
	key=operator.itemgetter(1),
	reverse=False)

for registro in listaordenada:
	print(registro[0], registro[1])

