# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:53:56 2021

@author: TAURET
"""

def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def main():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    main()
