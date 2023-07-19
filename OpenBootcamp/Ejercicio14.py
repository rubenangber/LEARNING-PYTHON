import tkinter 

def reset_selection():
    var.set(None)

window = tkinter.Tk()

var = tkinter.IntVar()

radio_button1 = tkinter.Radiobutton(window, text="Opción 1", variable=var, value=1)
radio_button2 = tkinter.Radiobutton(window, text="Opción 2", variable=var, value=2)
radio_button3 = tkinter.Radiobutton(window, text="Opción 3", variable=var, value=3)

reset_button = tkinter.Button(window, text="Reiniciar", command=reset_selection)

radio_button1.pack()
radio_button2.pack()
radio_button3.pack()
reset_button.pack()

window.mainloop()
