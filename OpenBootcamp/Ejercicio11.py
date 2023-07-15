from pickle import *

class Vehiculo:
    color = None
    ruedas = None

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'{self.color} {self.ruedas}'
    
coche = Vehiculo("Verde", 4)
print(coche)
f = open('ejercicio2.txt', 'w+b')
dump(coche, f)

f.seek(0)
coche2 = load(f)

print(coche2)
f.close()