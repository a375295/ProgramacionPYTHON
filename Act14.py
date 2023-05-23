import math
import tkinter as Tk
import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('290x380')
root.configure(bg='grey23')
root.resizable(0,0)
root.title('Calculadora 2')

def entrada(val):
    x = entry.get()
    entry.set(x + val)

def entrada_signo(val):
    x = entry.get()
    # Validar si el último carácter es un signo aritmético
    if x and x[-1] in ['+', '-', '*', '/', '%', '.']:
        # No permitir agregar otro signo aritmético consecutivo
        return
    entry.set(x + val)

def limpiar():
    entry.set("")

def resultado():
    try:
        x = entry.get()
        y = eval(x)
        entry.set(y)
    except Exception as e:
        entry.set('Error')

def raiz():
    numero = entry.get()
    try:
        numero = float(numero)
        resultado = math.sqrt(numero)
        entry.set(resultado)
    except ValueError:
        entry.set('Error')

def cambiar_signo():
    x = entry.get()
    if x and x[0] != '-':
        entry.set('-' + x)
    elif x and x[0] == '-':
        entry.set(x[1:])

def on_key(event):
    key = event.char
    if key.isdigit():
        entrada(key)
    elif key in ['+', '-', '*', '/', '%', '.']:
        entrada_signo(key)
    elif event.keycode == 13:
        resultado()
    return
    

entry = StringVar()
entry.set("")

pantalla = Entry(root, bg="#87CEEB", fg='black', font=('Courier', 14, 'bold'), bd=3, justify='right', textvariable=entry)
pantalla.config(width=21, state='disabled')
pantalla.place(x=25, y=52)

btn_MC = Button(root, text="MC", bg='red', font=('Arial', 9, 'bold'), fg='white', command=limpiar)
btn_MC.config(width=5, height=2)
btn_MC.place(x=26, y=109)

btn_MR = Button(root, text="MR", bg='red', font=('Arial', 9, 'bold'), fg='white')
btn_MR.config(width=5, height=2)
btn_MR.place(x=74, y=109)

btn_MS = Button(root, text="MS", bg='red', font=('Arial', 9, 'bold'), fg='white')
btn_MS.config(width=5, height=2)
btn_MS.place(x=122, y=109)

btn_M = Button(root, text="M+", bg='red', font=('Arial', 9, 'bold'), fg='white')
btn_M.config(width=5, height=2)
btn_M.place(x=170, y=109)

btn_SQR = Button(root, text="SQR", bg='red', font=('Arial', 9, 'bold'), fg='white', command=raiz)
btn_SQR.config(width=5, height=2)
btn_SQR.place(x=220, y=109)

btn_7 = Button(root, text="7", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada('7'))
btn_7.config(width=5, height=2)
btn_7.place(x=26, y=167)

btn_8 = Button(root, text="8", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada('8'))
btn_8.config(width=5, height=2)
btn_8.place(x=74, y=167)

btn_9 = Button(root, text="9", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada('9'))
btn_9.config(width=5, height=2)
btn_9.place(x=122, y=167)

btn_mn = Button(root, text="+-", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command=cambiar_signo)
btn_mn.config(width=5, height=2)
btn_mn.place(x=170, y=167)

btn_porcentaje = Button(root, text="%", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada_signo('%'))
btn_porcentaje.config(width=5, height=2)
btn_porcentaje.place(x=218, y=167)

btn_4 = Button(root, text="4", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada('4'))
btn_4.config(width=5, height=2)
btn_4.place(x=26, y=210)

btn_5 = Button(root, text="5", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada('5'))
btn_5.config(width=5, height=2)
btn_5.place(x=74, y=210)

btn_6 = Button(root, text="6", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada('6'))
btn_6.config(width=5, height=2)
btn_6.place(x=122, y=210)

btn_mult = Button(root, text="*", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada_signo('*'))
btn_mult.config(width=5, height=2)
btn_mult.place(x=170, y=210)

btn_div = Button(root, text="1/x", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command=lambda:entrada_signo('/'))
btn_div.config(width=5, height=2)
btn_div.place(x=218, y=210)

btn_1 = Button(root, text="1", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada('1'))
btn_1.config(width=5, height=2)
btn_1.place(x=26, y=253)

btn_2 = Button(root, text="2", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada('2'))
btn_2.config(width=5, height=2)
btn_2.place(x=74, y=253)

btn_3 = Button(root, text="3", background="white", bd=2, relief=tk.GROOVE, font=('Helvetica', 9, 'bold'), command= lambda: entrada('3'))
btn_3.config(width=5, height=2)
btn_3.place(x=122, y=253)

btn_menos = Button(root, text="-", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada_signo('-'))
btn_menos.config(width=5, height=2)
btn_menos.place(x=170, y=253)

btn_igual = Button(root, text="=", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command=resultado)
btn_igual.config(width=5, height=5)
btn_igual.place(x=218, y=253)

btn_mas = Button(root, text="+", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada_signo('+'))
btn_mas.config(width=5, height=2)
btn_mas.place(x=170, y=296)

btn_punto = Button(root, text=".", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE,  command= lambda: entrada_signo('.'))
btn_punto.config(width=5, height=2)
btn_punto.place(x=122, y=296)

btn_cero = Button(root, text="0", background="white", font=('Helvetica', 9, 'bold'), bd=2, relief=tk.GROOVE, command= lambda: entrada('0'))
btn_cero.config(width=12, height=2)
btn_cero.place(x=26, y=296)
root.bind('<Key>', on_key)
mainloop()