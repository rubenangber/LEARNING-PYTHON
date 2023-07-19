import tkinter

def show_selection():
    selection_label.config(text="Elemento seleccionado >> " + str(var.get()))

ventana = tkinter.Tk()

var = tkinter.StringVar()

radio_button1 = tkinter.Radiobutton(ventana, text="Opcion 1", variable=var, value="Elemento 1", command=show_selection)
radio_button2 = tkinter.Radiobutton(ventana, text="Opcion 2", variable=var, value="Elemento 2", command=show_selection)
radio_button3 = tkinter.Radiobutton(ventana, text="Opcion 3", variable=var, value="Elemento 3", command=show_selection)

selection_label = tkinter.Label(ventana, text="Elemento seleccionado >> ")

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
selection_label.pack()

ventana.mainloop()
