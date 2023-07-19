numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#filter(FUNCION, lista)
#Si la funcion return true, mantiene el numero
#Si la funcion return false, elimina el numero

def miFuncion(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
resultado = filter(miFuncion, numeros)
print(list(resultado))