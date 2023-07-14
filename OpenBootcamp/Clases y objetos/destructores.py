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

    def __del__(self):
       print("Estoy en el destructor de la clase", self.__class__)

p = Dino("Ruben", "Verde")
print(p.nombre)
