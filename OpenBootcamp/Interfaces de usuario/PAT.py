import tkinter

ventana = tkinter.Tk()  #Crear ventana

#Creacion de widgets
#Geometria PAT
label_saludo = tkinter.Label(ventana, text="HOLA!", bg="yellow", fg="blue") #Crear etiqueta
label_saludo.pack() #"Colocar" etiqueta

label_adios = tkinter.Label(ventana, text="ADIOS!", bg="red", fg="blue")
label_adios.pack(ipadx=50, ipady=50)

label_texto1 = tkinter.Label(ventana, text="Texto1!", bg="green")
label_texto1.pack(ipadx=50, ipady=50, fill='x', side='left')

label_texto2 = tkinter.Label(ventana, text="Texto2!", bg="orange")
label_texto2.pack(ipadx=50, ipady=50, fill='y', side='right')

label_texto3 = tkinter.Label(ventana, text="Texto3!", bg="purple")
label_texto3.pack(fill='both', side='top')

label_texto4 = tkinter.Label(ventana, text="Texto4!", bg="purple")
label_texto4.pack(fill='both', expand=True, side='bottom')

ventana.mainloop()  #"Mantener" la ventana