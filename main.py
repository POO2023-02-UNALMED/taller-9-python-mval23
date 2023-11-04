from tkinter import Tk, Button, Entry
import time as t

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("300x255")

# Configuracion operaciones

def agregar_numero(numero):
    # agregar numero o simbolo a la pantalla
    pantalla.insert(len(pantalla.get()), numero + " ")

def borrar_pantalla():
    # borrar pantalla
    pantalla.delete(0, 'end')

def realizar_operacion():
    expresion = pantalla.get()
    try:
        resultado = eval(expresion)
        pantalla.delete(0, 'end')
        pantalla.insert(0, str(resultado))
    except:
        pantalla.delete(0, 'end')
        pantalla.insert(0, "Math Error xd")
        t.sleep(2)
        pantalla.delete(0, 'end')
        agregar_numero("")


# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=80, padx=1, pady=1)


# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("1"))
boton_1.grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("2"))
boton_2.grid(row=1, column=1, padx=1, pady=1)

boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("3"))
boton_3.grid(row=1, column=2, padx=1, pady=1)

boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("4"))
boton_4.grid(row=2, column=0, padx=1, pady=1)

boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("5"))
boton_5.grid(row=2, column=1, padx=1, pady=1)

boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("6"))
boton_6.grid(row=2, column=2, padx=1, pady=1)

boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("7"))
boton_7.grid(row=3, column=0, padx=1, pady=1)

boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("8"))
boton_8.grid(row=3, column=1, padx=1, pady=1)

boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("9"))
boton_9.grid(row=3, column=2, padx=1, pady=1)

boton_0 = Button(root, text="0", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("0"))
boton_0.grid(row=4, column=1, padx=1, pady=1)

boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=realizar_operacion)
boton_igual.grid(row=4, column=0, columnspan=2, padx=1, pady=1)

boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: agregar_numero("."))
boton_punto.grid(row=4, column=2, padx=1, pady=1)

boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("+"))
boton_mas.grid(row=1, column=3, padx=1, pady=1)

boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("-"))
boton_menos.grid(row=2, column=3, padx=1, pady=1)

boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("*"))
boton_multiplicacion.grid(row=3, column=3, padx=1, pady=1)

boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: agregar_numero("/"))
boton_division.grid(row=4, column=3, padx=1, pady=1)


root.mainloop()
