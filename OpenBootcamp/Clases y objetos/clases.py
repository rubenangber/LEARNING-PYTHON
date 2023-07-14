class Dino:
    _encendido = True

    #Metodos
    def enciende(self):
        self._encedido = True

    def apaga(self):
        self._encedido = False

    def isEncendido(self):
        return self._encedido
    
d1 = Dino() #Creacion del objeto
d1.apaga()
print(d1.isEncendido())

d2 = Dino()
d2.enciende()
print(d2.isEncendido())

print(d1.isEncendido())