class Juguete:
    _encendido = True

    def enciende(self):
        self._encedido = True

    def apaga(self):
        self._encedido = False

    def isEncendido(self):
        return self._encedido
    
class Dino(Juguete):
    nombre = None
    color = None

    def __init__(self, nombre, color):
       self.nombre = nombre
       self.color = color

p = Dino("Ruben", "Verde")
print(p.nombre)
print(p.color)