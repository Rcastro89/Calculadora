#!/usr/bin/python3

import math
from tkinter import messagebox


def realizar_operacion(val1, val2, operador):
    resultado = 0.00
    if operador == '+':
        resultado = float(val1) + float(val2)
    elif operador == '-':
        resultado = float(val1) - float(val2)
    elif operador == '*':
        resultado = float(val1) * float(val2)
    elif operador == '/':
        try:
            resultado = float(val1) / float(val2)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre 0")
            resultado = 0
    elif operador == 'Rc':
        try:
            resultado = math.sqrt(float(val1))
        except ValueError:
            messagebox.showerror("Error", "No se calcula Raiz de numeros negativos")
            resultado = 0
    decimal = math.modf(resultado)
    resultado = int(resultado) if decimal == 0 else resultado
    return resultado
