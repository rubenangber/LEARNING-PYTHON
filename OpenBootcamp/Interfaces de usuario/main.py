import tkinter
from tkinter import StringVar, ttk

ventana = tkinter.Tk()

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

frame = ttk.Frame(ventana)

label = ttk.Label(frame, text="Hola")
label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)

frame.grid(column=0, row=0, sticky=tkinter.W)

lista = ["Windows", "Mac", "Linux", "BeOS"]
listaItems = StringVar(value=lista)
listbox = tkinter.Listbox(ventana, height=5, listvariable=listaItems)
listbox.grid(column=0, row=0, sticky=tkinter.W)

selecionado = tkinter.StringVar()
r1 = ttk.Radiobutton(ventana, text="Si", value=1, variable=selecionado)
r2 = ttk.Radiobutton(ventana, text="No", value=2, variable=selecionado)
r3 = ttk.Radiobutton(ventana, text="tal vez", value=3, variable=selecionado)
r1.grid(column=0, row=1, pady=5, padx=5)
r2.grid(column=0, row=2, pady=5, padx=5)
r3.grid(column=0, row=3, pady=5, padx=5)

checkBox = ttk.Checkbutton(ventana, text="Acepto las condiciones", variable=selecionado)
checkBox.grid(column=0, row=1, pady=5, padx=5)

ventana.mainloop()