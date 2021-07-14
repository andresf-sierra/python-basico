# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:39:39 2021

@author: TAURET
"""

# def run(num, rept):
#     if num <= rept:
#         cont = num
#         print(str(2 ** cont) )
#         run(num+1, rept)
#     else:
#         print("Fin!")

# if __name__ == "__main__":
#     repeticiones = int(input("Cuantas potencias: "))
#     run(0, repeticiones)


def main():
    LIM = 1000000
    
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIM:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador
    


if __name__ == "__main__":
    main()
    