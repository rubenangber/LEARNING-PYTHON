# r --> lectura
# a --> adjuntar
# w --> escritura
# x --> crear

# t --> texto
# b --> binario

# +

f = open('fichero.txt', 'r')
#       f.read(numero de bytes a leer)
datos = f.read()
print(datos)
f.close()

f = open('fichero.txt', 'r')
while datos != "":
    datos = f.readline()
    print(datos)
f.close()


def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
        
        f.write(linea)

    f.close()

lista = [
    'Una linea\n',
    'Dos lineas',
    'Tres lineas'
]

escribe('fichero2.txt', lista)