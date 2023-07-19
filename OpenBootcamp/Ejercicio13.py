from functools import reduce

numeros = [5, 4, 6, 8, 2, 10, 1, 7, 1, 8, 3]

def miFuncion(x):
    if x % 2 != 0:
        return True
    else:
        return False

def suma(a, b):
    print(f'a >> {a}\tb >> {b}\tres >> {a + b}')
    return a + b
    
resultado = filter(miFuncion, numeros)
print(list(resultado))

resultado2 = reduce(suma, filter(miFuncion, numeros))
print(resultado2)