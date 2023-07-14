class Vehiculo:
    color = None
    Ruedas = None
    Puertas = None

class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __del__ (self):
        print("Borrado de coche")

car = Coche("Verde", 4, 5, 120, 1500)
print(car.color, car.ruedas, car.puertas, car.velocidad, car.cilindrada)