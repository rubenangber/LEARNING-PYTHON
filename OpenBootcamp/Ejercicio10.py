f = open('ejercicio.txt', 'w')
f.write("Primera escritura\n")
f.close()

f = open('ejercicio.txt', 'a')
f.write("Segunda escritura\n")
f.close()