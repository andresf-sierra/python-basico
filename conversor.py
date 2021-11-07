# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:35:18 2021

@author: TAURET
"""
"""
Crearemos un programa que convierta de pesos colombianos a dólares
"""
def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingrese su cantidad en pesos" + tipo_pesos + ": ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + "  dólares")
    
menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS 

~ Cambia de pesos colombianos, mexicanos y argentinos a dólares ~

******************************
1 - Pesos Colombianos
2 - Pesos Mexicanos
3 - Pesos Argentinos
****************************** 

Elige tu moneda local: """

opcion = input(menu)

if opcion == '1':
   conversor(" colombianos", 3774)
elif opcion == '2':
    conversor(" mexicanos", 19.77 )
elif opcion == '3':
    conversor(" argentinos", 84.91)
else:
    print("Ingresa una opción número, por favor: ")
    




