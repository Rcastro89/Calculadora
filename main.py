#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import math
import re
from operaciones import realizar_operacion, validar_estatus


class Ventana_calculadora():
    """clase para crear la ventana visual"""

    val_1 = ""
    val_2 = ""
    controlar = False
    num_activo = False
    ope_ant = ""
    total = 0

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(0, 0)

    def contenedor_principal(self):
        self.contenedor = Frame(self.ventana)
        self.contenedor.config(bg='gray', width=313, height=320)
        self.contenedor.pack(expand=YES, fill=BOTH)
        self.frame_pantalla = Frame(self.contenedor, width=300, height=50)
        self.frame_pantalla.pack_propagate(False)
        self.frame_pantalla.grid(row=0, column=0, columnspan=4)
        self.texto_pantalla = Label(
            self.frame_pantalla, anchor='e', font=('Arial', 24))
        self.texto_pantalla.pack(expand=YES, fill=BOTH)
        self.boton_Ce = Button(self.contenedor, width=5,
                               height=2, text='CE',
                               command=lambda: self.but("Escape"))
        self.boton_Ce.grid(row=1, column=0)
        self.boton_Rc = Button(self.contenedor, width=5,
                               height=2, text='√',
                               command=lambda: self.but("Raiz"))
        self.boton_Rc.grid(row=1, column=1)
        self.boton_Potencia = Button(self.contenedor, width=5,
                               height=2, text='x²',
                               command=lambda: self.but("Potencia"))
        self.boton_Potencia.grid(row=1, column=2)
        self.boton_borrar = Button(self.contenedor, width=5,
                                   height=2, text='<--',
                                   command=lambda: self.but("BackSpace"))
        self.boton_borrar.grid(row=1, column=3)
        self.boton_7 = Button(self.contenedor, width=5,
                              height=2, text='7',
                              command=lambda: self.but("7"))
        self.boton_7.grid(row=2, column=0)
        self.boton_8 = Button(self.contenedor, width=5,
                              height=2, text='8',
                              command=lambda: self.but("8"))
        self.boton_8.grid(row=2, column=1)
        self.boton_9 = Button(self.contenedor, width=5,
                              height=2, text='9',
                              command=lambda: self.but("9"))
        self.boton_9.grid(row=2, column=2)
        self.boton_por = Button(self.contenedor, width=5, height=2, text='x',
                                command=lambda: self.but("asterisk"))
        self.boton_por.grid(row=2, column=3)
        self.boton_4 = Button(self.contenedor, width=5,
                              height=2, text='4',
                              command=lambda: self.but("4"))
        self.boton_4.grid(row=3, column=0)
        self.boton_5 = Button(self.contenedor, width=5,
                              height=2, text='5',
                              command=lambda: self.but("5"))
        self.boton_5.grid(row=3, column=1)
        self.boton_6 = Button(self.contenedor, width=5,
                              height=2, text='6',
                              command=lambda: self.but("6"))
        self.boton_6.grid(row=3, column=2)
        self.boton_entre = Button(self.contenedor, width=5, height=2, text='/',
                                  command=lambda: self.but("slash"))
        self.boton_entre.grid(row=3, column=3)
        self.boton_1 = Button(self.contenedor, width=5,
                              height=2, text='1',
                              command=lambda: self.but("1"))
        self.boton_1.grid(row=4, column=0)
        self.boton_2 = Button(self.contenedor, width=5,
                              height=2, text='2',
                              command=lambda: self.but("2"))
        self.boton_2.grid(row=4, column=1)
        self.boton_3 = Button(self.contenedor, width=5,
                              height=2, text='3',
                              command=lambda: self.but("3"))
        self.boton_3.grid(row=4, column=2)
        self.boton_menos = Button(self.contenedor, width=5, height=2, text='-',
                                  command=lambda: self.but("minus"))
        self.boton_menos.grid(row=4, column=3)
        self.boton_0 = Button(self.contenedor, width=5,
                              height=2, text='0',
                              command=lambda: self.but("0"))
        self.boton_0.grid(row=5, column=0)
        self.boton_punto = Button(self.contenedor, width=5, height=2, text='.',
                                  command=lambda: self.but("period"))
        self.boton_punto.grid(row=5, column=1)
        self.boton_igual = Button(self.contenedor, width=5, height=2, text='=',
                                  command=lambda: self.but("Return"))
        self.boton_igual.grid(row=5, column=2)
        self.boton_mas = Button(self.contenedor, width=5, height=2, text='+',
                                command=lambda: self.but("plus"))
        self.boton_mas.grid(row=5, column=3)
        self.ventana.bind('<Any-KeyPress>', self.but)
        self.ventana.mainloop()

    def but(self, event):
        try:
            num = event.keysym
        except AttributeError:
            num = event
        ope = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/',
               'KP_Add': '+', 'KP_Subtract': '-', 'KP_Multiply': '*',
               'KP_Divide': '/', 'Raiz': 'Rc', 'Potencia': 'Po'}
        if num in ope.keys():
            self.definir_valores(ope[num])
        elif num == "Return" or num == 'KP_Enter':
            if self.val_1 != "":
                self.definir_valores('=')
        elif num == 'Escape':
            self.val_1, self.val_2, self.ope_ant = "", "", ""
            self.controlar = False
            self.num_activo = False
            self.total = 0
            self.texto_pantalla['text'] = ""
        elif num == 'BackSpace':
            if len(self.texto_pantalla['text']) > 1:
                self.actualizar_pantalla("borrar")
            else:
                self.texto_pantalla['text'] = ''
        else:
            dic_num = {'KP_1': '1', 'KP_2': '2', 'KP_3': '3',
                       'KP_4': '4', 'KP_5': '5',
                       'KP_6': '6', 'KP_7': '7', 'KP_8': '8',
                       'KP_9': '9', 'KP_0': '0'}
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
            if self.controlar:
                self.texto_pantalla['text'] = ""
            self.actualizar_pantalla(agrego)
            self.controlar = False
            self.num_activo = True
        largo = len(self.texto_pantalla['text'])
        if largo > 15 and largo < 21:
            self.texto_pantalla.config(font=('Arial', 16))
        elif largo <= 15:
            self.texto_pantalla.config(font=('Arial', 24))
        elif largo > 21:
            self.texto_pantalla.config(font=('Arial', 12))

    def definir_valores(self, ope):
        self.controlar = True
        self.total = 0
        if self.num_activo or ope == 'Rc' or ope == 'Po':
            self.num_activo = False
            if self.ope_ant == "":
                self.ope_ant = ope
            if self.val_1 == "":
                self.definir_val1()
            elif self.val_2 == "":
                self.definir_val2()
            if ope == 'Rc' or ope == 'Po':
                self.val_2 = '1'
                self.ope_ant = ope
            if self.val_1 != "" and self.val_2 != "":
                self.total = realizar_operacion(self.val_1, self.val_2, self.ope_ant)
                self.ope_ant = ope
                if self.ope_ant != '=':
                    self.val_1 = str(self.total)
                    self.val_2 = ""
                else:
                    self.val_1, self.val_2, self.ope_ant = "", "", ""
                    self.num_activo = True
                self.texto_pantalla['text'] = ""
                self.actualizar_pantalla(str(self.total))
        else:
            self.ope_ant = ope

    def definir_val1(self):
        self.val_1 = re.sub(',', "", self.texto_pantalla['text'])

    def definir_val2(self):
        self.val_2 = re.sub(',', "", self.texto_pantalla['text'])

    def actualizar_pantalla(self, agregar):
        if agregar == '.':
            self.texto_pantalla['text'] = self.texto_pantalla['text'] + agregar
            return
        elif agregar == "borrar":
            numero = float(re.sub(',', "", self.texto_pantalla['text'][0:-1]))
        else:
            numero = float(
                re.sub(',', "", self.texto_pantalla['text'] + agregar))
        decimal, entera = math.modf(numero)
        numero = int(numero) if decimal == 0 else numero
        self.texto_pantalla['text'] = '{0:,}'.format(numero)


abrir = Ventana_calculadora()
abrir.contenedor_principal()
