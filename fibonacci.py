ant = 0
desp = 1

interacciones = int(input("Introduce el numero de interacciones >> "))

print(ant, desp, end=' ')

for i in range(interacciones):
    suma = ant + desp
    ant = desp
    desp = suma
    print(suma, end=' ')