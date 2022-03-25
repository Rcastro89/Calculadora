#!/usr/bin/python3


def seleccion_operacion(val1, val2, operador):
    resultado = 0.00
    if operador == '+':
        resultado = float(val1) + float(val2)
    elif operador == '-':
        resultado = float(val1) - float(val2)
    elif operador == '*':
        resultado = float(val1) * float(val2)
    elif operador == '/':
        resultado = float(val1) / float(val2)
    return resultado
