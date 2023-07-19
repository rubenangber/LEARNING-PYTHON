import tkinter

def saludar(event):
    print("Han hecho click en saludar")
    
def salir(event):
    print("Adios")
    ventana.quit()

ventana = tkinter.Tk()

boton = tkinter.Button(ventana, text="Haz click")
boton.pack()
boton.bind('<Button-1>', saludar)

botonSalir = tkinter.Button(ventana, text="Salir")
botonSalir.pack()
botonSalir.bind('<Button-1>', salir)

ventana.mainloop()