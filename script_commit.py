import subprocess
import time
from datetime import datetime, timedelta
import os

def obtener_fecha_actual():
    ahora = datetime.now()
    return ahora.strftime("%d/%m/%Y")

def ejecutar_comando(comandos):
    # Ejecutar los comandos
    for comando in comandos:
        subprocess.run(comando, shell=True)

def obtener_tiempo_hasta_hora_deseada(hora, minutos):
    ahora = datetime.now()
    hora_deseada = datetime(ahora.year, ahora.month, ahora.day, hora, minutos, 0)
    if ahora > hora_deseada:
        # Si ya pasó la hora deseada, calcular el tiempo hasta la próxima ocurrencia
        hora_deseada += timedelta(days=1)
    tiempo_restante = hora_deseada - ahora
    return tiempo_restante.total_seconds()

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Hora y minutos deseados
hora_deseada = 00
minutos_deseados = 00

# Comandos a ejecutar
comandos = [
    f'cd "{directorio_actual}"', 
    "git add .",
    f'git commit -m "{obtener_fecha_actual()}"',
    "git push"
]

# Calcular el tiempo hasta la hora deseada
tiempo_hasta_hora_deseada = obtener_tiempo_hasta_hora_deseada(hora_deseada, minutos_deseados)

# Esperar hasta la hora deseada
print(f'Esperando a las {hora_deseada:02}:{minutos_deseados:02}... ({tiempo_hasta_hora_deseada} segundos)')
time.sleep(tiempo_hasta_hora_deseada)

# Ejecutar los comandos
ejecutar_comando(comandos)
