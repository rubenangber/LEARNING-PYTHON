class Alumno:
    nombre = None
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __del__ (self):
        pass
    
    def resultado(self):
        if self.nota >= 5:
            return True
        else:
            return False

alum1 = Alumno("Ruben", 7)
alum2 = Alumno("Andres", 4)
if alum1.resultado():
    print(alum1.nombre, "ha aprobado con un", alum1.nota)
else:
    print(alum1.nombre, "ha suspendido con un", alum1.nota)

if alum2.resultado():
    print(alum2.nombre, "ha aprobado con un", alum2.nota)
else:
    print(alum2.nombre, "ha suspendido con un", alum2.nota)