def esBisiesto(anio):
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

anio = int(input("Introduce el año >> "))
if esBisiesto(anio):
    print("Es una año bisiesto")
else:
    print("No es una año bisiesto")