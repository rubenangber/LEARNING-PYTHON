lista = [1, 2, 3, 4, 5]

for valorActual in lista:
    print(valorActual)

                  #min max-1
for numero in range(5, 10):
    print(numero)

longitud = len(lista)
for numero in range(longitud):
    print(lista[numero])

if 5 in lista:
    print("Hay un 5 en la lista")

if 6 not in lista:
    print("No hay un 6 en la lista")


lista2 = [5, 3, 1, 5, 1, 4, 8]
listaOrdenada = sorted(lista2)
print(listaOrdenada)
listaOrdenada = sorted(lista2, reverse = True)
print(listaOrdenada)