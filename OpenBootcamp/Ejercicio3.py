peso = float(input("Ingresa tu peso en kg >> "))
estatura = float(input("Ingresa tu estatura en metros >> "))

imc = peso / (estatura ** 2)
imc_redondeado = round(imc, 2)

print("Tu índice de pasa corporal es >> ", imc_redondeado)