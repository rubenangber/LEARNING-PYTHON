#import operaciones
import operaciones as op
import math #Modulo de python

import packOperaciones.multiplicacion

def main():
    #res = operaciones.suma(2, 2)
    res = op.suma(2, 2)
    print(res)

    res = packOperaciones.multiplicacion.mul(4, 5)
    print(res)
    print("Hola en main")

if __name__ == '__main__':
    main()