# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:48:29 2021

@author: TAURET
"""

# COP to USD
pesos = input("Ingrese su cantidad en pesos colombianos: ")
pesos = float(pesos)
valor_dolar = 3441 #COP
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Usted tiene $" + dolares + "  dólares")

# USD to COP
dolares = input("Ingrese su cantidad en dólares: ")
dolares = float(dolares)
valor_peso = 0.00029 #USD
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Usted tiene " + pesos + "  pesos colombianos")


