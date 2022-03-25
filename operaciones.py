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
    elif operador == 'Po':
        resultado = float(val1) ** 2
    decimal = math.modf(resultado)
    resultado = int(resultado) if decimal[0] == 0 else resultado
    return resultado

def validar_estatus(val1, val2, controlar, num_activo, ope_ant, total):
    print('val 1 = {}'.format(val1))
    print('val 2 = {}'.format(val2))
    print('controlar = {}'.format(controlar))
    print('num_activo = {}'.format(num_activo))
    print('ope_ant = {}'.format(ope_ant))
    print('total = {}'.format(total))
    # validar_estatus(self.val_1, self.val_2, self.controlar, self.num_activo, self.ope_ant, self.total)
