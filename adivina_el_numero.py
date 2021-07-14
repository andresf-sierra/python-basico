# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:56:34 2021

@author: TAURET
"""
import random

def main():
    numero_random = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Elige otro número: "))
    print("¡Has Ganado!")
    
    
    
if __name__ == "__main__":
    main()    