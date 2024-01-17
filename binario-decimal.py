import tkinter as tk

def convertir_a_binario():
    direccion_ip = entry_ip.get()
    try:
        # Verificar si la dirección IP tiene el formato correcto
        partes = direccion_ip.split('.')
        if len(partes) == 4 and all(0 <= int(p) <= 255 for p in partes):
            # Convertir cada parte a binario y juntarlas con puntos
            direccion_binaria = '.'.join(format(int(p), '08b') for p in partes)
            resultado_text.delete(1.0, tk.END)  # Limpiar el resultado anterior
            resultado_text.insert(tk.END, f'{direccion_binaria}')
        else:
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, 'Formato de dirección IP incorrecto')
    except ValueError:
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, 'Formato de dirección IP incorrecto')

def convertir_a_decimal():
    direccion_binaria = entry_binario.get()
    try:
        # Verificar si la dirección binaria tiene el formato correcto
        partes = direccion_binaria.split('.')
        if len(partes) == 4 and all(0 <= int(p, 2) <= 255 for p in partes):
            # Convertir cada parte a decimal y juntarlas con puntos
            direccion_decimal = '.'.join(str(int(p, 2)) for p in partes)
            resultado_text_binario.delete(1.0, tk.END)
            resultado_text_binario.insert(tk.END, f'{direccion_decimal}')
        else:
            resultado_text_binario.delete(1.0, tk.END)
            resultado_text_binario.insert(tk.END, 'Formato de dirección binaria incorrecto')
    except ValueError:
        resultado_text_binario.delete(1.0, tk.END)
        resultado_text_binario.insert(tk.END, 'Formato de dirección binaria incorrecto')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Conversor IP')

# Configurar pesos de columnas y filas para hacer la ventana responsive
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(4, weight=1)

# Primera fila: Label y Entry para ingresar la dirección IP
label_ip = tk.Label(ventana, text='Ingrese la dirección IP >> ')
label_ip.grid(row=0, column=0, padx=10, pady=10, sticky='e')

entry_ip = tk.Entry(ventana)
entry_ip.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

# Segunda fila: Resultado en formato binario
resultado_text = tk.Text(ventana, height=1, wrap=tk.WORD)
resultado_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Tercera fila: Botón para realizar la conversión a binario
boton_convertir = tk.Button(ventana, text='Convertir a Binario', command=convertir_a_binario)
boton_convertir.grid(row=2, column=0, columnspan=2, pady=10)

# Cuarta fila: Label y Entry para ingresar la dirección binaria
label_binario = tk.Label(ventana, text='Ingrese la dirección binaria >> ')
label_binario.grid(row=3, column=0, padx=10, pady=10, sticky='e')

entry_binario = tk.Entry(ventana)
entry_binario.grid(row=3, column=1, padx=10, pady=10, sticky='ew')

# Quinta fila: Resultado en formato decimal
resultado_text_binario = tk.Text(ventana, height=1, wrap=tk.WORD)
resultado_text_binario.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

# Sexta fila: Botón para realizar la conversión a decimal
boton_convertir_binario = tk.Button(ventana, text='Convertir a Decimal', command=convertir_a_decimal)
boton_convertir_binario.grid(row=5, column=0, columnspan=2, pady=10)

# Hacer los resultados seleccionables
resultado_text.tag_configure("center", justify='center')
resultado_text.tag_add("center", "1.0", "end")

resultado_text_binario.tag_configure("center", justify='center')
resultado_text_binario.tag_add("center", "1.0", "end")

# Iniciar el bucle principal
ventana.mainloop()