import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
etiqueta_temp_celsius = ttk.Label(text="Temperatura en ºC:")
etiqueta_temp_celsius.place(x=20, y=20)
#insertamos una caja de texto vacia
caja_temp_celsius = ttk.Entry()
#colocamos caja de texto  en posicion xy y, y damos ancho de 60
caja_temp_celsius.place(x=140, y=20, width=60)
#creamos un boton con texto convertir
boton_convertir = ttk.Button(text="Convertir")
#posicionamos el boton en relacion a la ventana x y y
boton_convertir.place(x=20, y=60)
#agregamos 2 etiquetas de texto y lo pocisionamos
etiqueta_temp_kelvin = ttk.Label(text="Temperatura en K: n/a")
etiqueta_temp_kelvin.place(x=20, y=120)
etiqueta_temp_fahrenheit = ttk.Label(text="Temperatura en ºF: n/a")
etiqueta_temp_fahrenheit.place(x=20, y=160)
ventana.mainloop()
