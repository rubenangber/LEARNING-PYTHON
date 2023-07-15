#VERSION VIEJA --> NO USAR
numero = 511
texto = "quijote"
otromas = 1.2

print("El numero es %d, el texto es %s y tiene %f" % (numero, texto, otromas))
print("Valor flotante %.1f" % otromas)

#OTRA VERSION
#                   {0}             {1}        {3}
print("El numero es {}, el texto es {} y tiene {}".format(numero, texto, otromas))
print("El numero es {1}, el texto es {2} y tiene {0}".format(numero, texto, otromas))
print("El numero es {n}, el texto es {t} y tiene {f}".format(n = numero, t = texto, f = otromas))

#OTRA VERSION --> MAS COMUN
def suma(a, b):
    return a + b

print(f'El numero es {numero}, el texto es {texto} y tiene {otromas}')
print(f'El numero es {suma(numero, numero)}, el texto es {texto.upper()} y tiene {otromas}')

