class Juguete:
    _encendido = True

    def enciende(self):
        self._encedido = True

    def apaga(self):
        self._encedido = False

    def isEncendido(self):
        return self._encedido
    
class Dino(Juguete):
    def quitarOreja(self):
        pass
    
    def ponerOreja(self):
        pass

d = Dino()
d.enciende()
print(d.isEncendido())
d.apaga()
print(d.isEncendido())
d.quitarOreja()
