from functools import reduce

#Ejecuta de forma recursiva una funcion
#hasta que la lista se queda con 1 valor

def suma(a, b):
    print(f'a >> {a}\tb >> {b}\tres >> {a + b}')
    return a + b

resultado = reduce(suma, [1, 2, 3, 4, 5])
print(resultado)