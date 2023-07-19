from getpass import getpass

nombre = input("Como te llamas >> ")
print(nombre)

contraseña = getpass("Introduce contraseña >> ") #No lo muestra
print(contraseña)

secretro = 50
valor = 0
while valor != secretro:
    valor = int(input("Introduce valor >> "))
    if valor > secretro:
        print("Muy alto")
    else: 
        print("Muy bajo")
print("Correcto")