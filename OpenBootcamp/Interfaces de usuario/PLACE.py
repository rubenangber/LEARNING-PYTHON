import random
import tkinter

ventana = tkinter.Tk()

colors = ['blue', 'red', 'yellow', 'purple', 'green', 'black']

for x in range(0, 10):
    color1 = random.randint(0, len(colors)- 1)
    color2 = random.randint(0, len(colors) - 1)
    label = tkinter.Label(ventana, text="Etiqueta!", bg=colors[color1], fg=colors[color2])
    label.place(x=random.randint(0, 100), y=random.randint(0, 100))

label1 = tkinter.Label(ventana, text="Posicionamiento absoluto", bg="blue")
label1.place(x=10, y=50)

label2 = tkinter.Label(ventana, text="Otro", bg="red")
label2.place(relx=0.1, rely=0.15, relwidth=0.5, anchor='ne')

ventana.mainloop()