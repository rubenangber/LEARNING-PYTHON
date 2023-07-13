print("WHILE")
contador = 0
while contador <= 10:
    print("Contador >>", contador)
    contador += 1

print("\nWHILE IF")
contador = 0
while contador <= 10:
    if contador % 2 == 0:
        print("Contador >>", contador, "es par")
    contador += 1
    
print("\nWHILE BREAK")
contador = 0
while contador <= 10:
    print("Contador >>", contador)
    if contador == 5:
        break #Finaliza la ejecucion
    contador += 1

print("\nWHILE CONTINUE")
contador = 0
while contador <= 10:
    contador += 1
    print("Contador >>", contador)
    if contador % 2 == 0:
        print("Es par")
        continue #Fuerza la siguiente iteraccion