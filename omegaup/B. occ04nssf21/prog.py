linea = input()
palabras = linea.split (" ")

palabra1 = list(palabras[0])
palabra2 = list(palabras[1])

palabra1.sort()
palabra2.sort()

sep = ""
palabra1 = sep.join(palabra1)
palabra2 = sep.join(palabra2)


if palabra1==palabra2 :
  print("SI")
else:
  print ("NO")


