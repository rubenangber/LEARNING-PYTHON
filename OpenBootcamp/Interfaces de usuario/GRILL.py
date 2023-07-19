import tkinter
from tkinter import ttk

ventana = tkinter.Tk()

#(0,0)   (1,0)   (2,0)
#(0,1)   (1,1)   (2,1)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

#Usuario
label_username = ttk.Label(ventana, text="Username >> ")
label_username.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(ventana)
username_entry.grid(column=1, row=0, sticky=tkinter.W, padx=5, pady=5)

#Contraseña
label_password = ttk.Label(ventana, text="Password >> ")
label_password.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(ventana, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.W, padx=5, pady=5)

#Boton
label_button = ttk.Button(ventana, text="Siguiente")
label_button.grid(column=1, row=3, sticky=tkinter.E, padx=5, pady=5)

ventana.mainloop()