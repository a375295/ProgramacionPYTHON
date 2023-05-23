import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calculadora Operaciones Basicas")
root.geometry("374x290+0+0")
root.resizable(0,0)

# METODOS
def suma():
    try:
        n1 = int(num.get())
        n2 = int(num2.get())
        result.set(n1+n2)
        signo.set("+")
    except ValueError:
        result.set("Syntax_Error")

def resta():
    try:
        n1 = int(num.get())
        n2 = int(num2.get())
        result.set(n1-n2)
        signo.set("-")
    except ValueError:
        result.set("Syntax_Error")

def multi():
    try:
        n1 = int(num.get())
        n2 = int(num2.get())
        result.set(n1*n2)
        signo.set("*")
    except ValueError:
        result.set("Syntax_Error")
def divi():
    try:
        n1 = int(num.get())
        n2 = int(num2.get())
        result.set(n1/n2)
        signo.set("/")
    except ValueError:
        result.set("Syntax_Error")
        
# DECLARACION DE VARIABLES
num = StringVar()
num.set("0")

num2 = StringVar()
num2.set("0")

signo = StringVar()
signo.set(" ")


result = StringVar()
result.set("0")

# GUI
mi_frame = tk.Frame(root, width=374, height=290)
mi_frame.pack()

gp = tk.LabelFrame(mi_frame, width=341, height=100, text="Operaciones")
gp2 = tk.LabelFrame(mi_frame, width=341, height=76, text="Operaciones Aritmeticos")

lbl = tk.Label(mi_frame, text="numero 1")
lbl2 = tk.Label(mi_frame, text="numero 2")
signo_result = tk.Label(mi_frame, text="Resultado")
signos = tk.Label(mi_frame, textvariable=signo)
sg_igual = tk.Label(mi_frame, text="=")

input_n1 = tk.Entry(mi_frame, width=12, textvariable=num)
input_n2 = tk.Entry(mi_frame,width=12, textvariable=num2)
input_result = tk.Entry(mi_frame, width=12, textvariable=result)

btn_mas = tk.Button(mi_frame, text="+", width=8, command=suma)
btn_menos = tk.Button(mi_frame, text="-", width=8, command=resta)
btn_multi = tk.Button(mi_frame, text="*", width=8, command=multi)
btn_div = tk.Button(mi_frame, text="/", width=8, command=divi)

lbl_nombre = tk.Label(mi_frame, text="By_Emiliano")

lbl.place(x=45, y=66)
lbl2.place(x=162, y=66)
signo_result.place(x=265, y=66)
input_n1.place(x=36, y=97)
input_n2.place(x=150, y=97)
input_result.place(x=265, y=97)
gp.place(x=16, y=48)
gp2.place(x=16, y=183)
signos.place(x=122, y=96)
sg_igual.place(x=235, y=96)
btn_mas.place(x=39, y=209)
btn_menos.place(x=116, y=209)
btn_multi.place(x=194, y=209)
btn_div.place(x=271, y=209)

lbl_nombre.place(x=286, y=265)

mainloop()