# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:46:37 2021

@author: TAURET
"""
import random

def generar_contrasena():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g"]
    simbolos = ["!", "#", "&", "$", "/","(",")"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    caracteres = mayusculas + minusculas + simbolos + numeros
    
    contrasena = []
    
    for i in range(30):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    contrasena = "".join(contrasena)
    return contrasena    
        

def main():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)
    
    
if __name__ == "__main__":
    main()