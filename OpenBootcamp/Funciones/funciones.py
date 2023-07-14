def mifuncion(nombre):
    print("Hola", nombre)

def suma(num1, num2):
    print(num1 + num2)

def resta(num1, num2):
    return num1 - num2


nombre = input("Introduzca nombre >> ")
mifuncion(nombre)

uno = int(input("Introduzca primer numero >> "))
dos = int(input("Introduzca segundo numero >> "))

suma(uno, dos)
result = resta(uno, dos)

print(result)

#Funciones anonimas
anonima = lambda nombre: print("Hola", nombre)
anonima("a")