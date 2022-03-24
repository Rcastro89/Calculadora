#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


class Ventana_calculadora():
    """clase para crear la ventana visual"""

    x_v = 500
    y_v = 500
    val_1 = ""
    val_2 = ""
    controlar = False
    num_activo = False
    totalizar = False
    ope_ant = ""
    total = 0

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(0,0)

    def contenedor_principal(self):
        self.contenedor = Frame(self.ventana)
        self.contenedor.config(bg='gray', width=500, height=200)
        self.contenedor.pack(expand=YES, fill=BOTH)
        self.texto_pantalla = Label(self.contenedor, width=15, anchor='e', font=('Arial', 24))
        self.texto_pantalla.grid(
            ipady=10, padx=5, pady=5, row=0, column=0, columnspan=4)
        self.boton_Ce = Button(self.contenedor, width=5,
                              height=2, text='CE', command=lambda: self.but("Escape"))
        self.boton_Ce.grid(row=1, column=0)
        self.boton_borrar = Button(self.contenedor, width=5,
                              height=2, text='<--', command=lambda: self.but("BackSpace"))
        self.boton_borrar.grid(row=1, column=3) 
        self.boton_7 = Button(self.contenedor, width=5,
                              height=2, text='7', command=lambda: self.but("7"))
        self.boton_7.grid(row=2, column=0)
        self.boton_8 = Button(self.contenedor, width=5,
                              height=2, text='8', command=lambda: self.but("8"))
        self.boton_8.grid(row=2, column=1)
        self.boton_9 = Button(self.contenedor, width=5,
                              height=2, text='9', command=lambda: self.but("9"))
        self.boton_9.grid(row=2, column=2)
        self.boton_por = Button(
            self.contenedor, width=5, height=2, text='x', command=lambda: self.but("asterisk"))
        self.boton_por.grid(row=2, column=3)
        self.boton_4 = Button(self.contenedor, width=5,
                              height=2, text='4', command=lambda: self.but("4"))
        self.boton_4.grid(row=3, column=0)
        self.boton_5 = Button(self.contenedor, width=5,
                              height=2, text='5', command=lambda: self.but("5"))
        self.boton_5.grid(row=3, column=1)
        self.boton_6 = Button(self.contenedor, width=5,
                              height=2, text='6', command=lambda: self.but("6"))
        self.boton_6.grid(row=3, column=2)
        self.boton_entre = Button(
            self.contenedor, width=5, height=2, text='/', command=lambda: self.but("slash"))
        self.boton_entre.grid(row=3, column=3)
        self.boton_1 = Button(self.contenedor, width=5,
                              height=2, text='1', command=lambda: self.but("1"))
        self.boton_1.grid(row=4, column=0)
        self.boton_2 = Button(self.contenedor, width=5,
                              height=2, text='2', command=lambda: self.but("2"))
        self.boton_2.grid(row=4, column=1)
        self.boton_3 = Button(self.contenedor, width=5,
                              height=2, text='3', command=lambda: self.but("3"))
        self.boton_3.grid(row=4, column=2)
        self.boton_menos = Button(
            self.contenedor, width=5, height=2, text='-', command=lambda: self.but("minus"))
        self.boton_menos.grid(row=4, column=3)
        self.boton_0 = Button(self.contenedor, width=5,
                              height=2, text='0', command=lambda: self.but("0"))
        self.boton_0.grid(row=5, column=0)
        self.boton_punto = Button(
            self.contenedor, width=5, height=2, text='.', command=lambda: self.but("period"))
        self.boton_punto.grid(row=5, column=1)
        self.boton_igual = Button(
            self.contenedor, width=5, height=2, text='=', command=lambda: self.but("Return"))
        self.boton_igual.grid(row=5, column=2)
        self.boton_mas = Button(
            self.contenedor, width=5, height=2, text='+', command=lambda: self.but("plus"))
        self.boton_mas.grid(row=5, column=3)
        self.ventana.bind('<Any-KeyPress>', self.but)
        self.ventana.mainloop()

    def but(self, event):
        num = event.keysym
        ope = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '//',
               'KP_Add': '+', 'KP_Subtract': '-', 'KP_Multiply': '*', 'KP_Divide': '//'}
        if num in ope.keys():
            self.definir_valores(ope[num])
        elif num == "Return" or num == 'KP_Enter':
            if self.val_1 != "":
                self.definir_valores('=')
        elif num == 'Escape':
            self.val_1 = ""
            self.val_2 = ""
            self.controlar = False
            self.num_activo = False
            self.totalizar = False
            self.ope_ant = ""
            self.total = 0
            self.texto_pantalla['text'] = ""
        elif num == 'BackSpace':
            if len(self.texto_pantalla['text']) > 1:
                self.texto_pantalla['text'] = self.texto_pantalla['text'][0:-1]
            else:
                self.texto_pantalla['text'] = ''
        else:
            dic_num = {'KP_1': '1', 'KP_2': '2', 'KP_3': '3', 'KP_4': '4', 'KP_5': '5',
                       'KP_6': '6', 'KP_7': '7', 'KP_8': '8', 'KP_9': '9', 'KP_0': '0'}
            dic_num_num = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                       '6': '6', '7': '7', '8': '8', '9': '9', '0': '0'}
            dic_punto = {'period': '.', 'KP_Decimal': '.'}
            agrego = ""
            if num in dic_num.keys():
                agrego = dic_num[num]
            elif num in dic_punto.keys():
                agrego = '.' if '.' not in self.texto_pantalla['text'] else ""
            elif num in dic_num_num.keys():
                agrego = num
            if self.controlar == True:
                self.texto_pantalla['text'] = ""
            self.controlar = False
            self.num_activo = True
            self.texto_pantalla['text'] = self.texto_pantalla['text'] + agrego

    def definir_valores(self, ope):
        self.controlar = True
        self.total = 0
        if self.num_activo == True:
            self.num_activo = False
            if self.ope_ant == "":
                self.ope_ant = ope
            if self.val_1 == "":
                self.definir_val1()
            elif self.val_2 == "":
                self.definir_val2()
            if self.val_1 != "" and self.val_2 != "":
                try:
                    self.total = int(eval(self.val_1 + self.ope_ant + self.val_2))
                except ZeroDivisionError:
                    messagebox.showerror("Error", "No se puede dividir entre 0")
                self.ope_ant = ope
                if self.ope_ant != '=':
                    self.val_1 = str(self.total)
                    self.val_2 = ""
                else:
                    self.val_1, self.val_2, self.ope_ant = "", "", ""
                    self.num_activo = True
                self.texto_pantalla['text'] = ""
                self.texto_pantalla['text'] = str(self.total)
    
    def definir_val1(self):
        if '.' in self.texto_pantalla['text']:
            intermedio = int(self.texto_pantalla['text']) if self.texto_pantalla['text'] != '' else ''
        else:
            intermedio = float(self.texto_pantalla['text']) if self.texto_pantalla['text'] != '' else ''
        self.val_1 = str(intermedio)
    
    def definir_val2(self):
        if '.' in self.texto_pantalla['text']:
            intermedio = int(self.texto_pantalla['text']) if self.texto_pantalla['text'] != '' else ''
        else:
            intermedio = float(self.texto_pantalla['text']) if self.texto_pantalla['text'] != '' else ''
        self.val_2 = str(intermedio)


abrir = Ventana_calculadora()
abrir.contenedor_principal()
