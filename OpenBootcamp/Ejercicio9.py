import time

hora_actual = time.localtime()

if hora_actual.tm_hour >= 19:
    print("Es hora de ir a casa")
else:
    tiempo_restante = (19 - hora_actual.tm_hour) * 60 - hora_actual.tm_min
    print("Aun quedan {} minutos de trabajo".format(tiempo_restante))
