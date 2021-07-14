# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:19:42 2021

@author: TAURET
"""
"""
1 - Necesito que el usuario ingrese un mensaje 
2 - El mensaje se imprime encriptado

¿Cómo se encripta?
- Ingreso un mensaje
    - Quito los espacios
    - Todo lo pongo en mayúscula
    
- Desgloso el mensaje en el abecedadario sin invertir
    - Cada letra es la letra inversa en el abecedario
- Tomo el abecedario y el abecedario invertido

- Y transformo cada letra en su equivalente invertido
    -
- Imprimo el mensaje

"""

# def abece(ascii_uppercase):
#     abece_inv = ascii_uppercase[::-1]
# def main():
    
#     mensaje = input("Escribe el mensaje a encriptar: ")
#     mensaje = mensaje.strip().upper()
#     for letra in mensaje:
        
    
    # print(mensaje)

# list(print(abece))
import string 



abcd_string = string.ascii_uppercase
abcd_list = list(abcd_string)
abcd_inv = string.ascii_uppercase[::-1]
abcd_invlist = list(abcd_inv)
print(abcd_list)
print(abcd_invlist)

mensaje = input("Escribe el mensaje a encriptar: ")
mensaje = mensaje.strip().upper()
print(mensaje)
    
    
    
    # print(string.ascii_uppercase)
     # invertida = string.ascii_uppercase[::-1]
    
    
    
    
# if __name__ == "__main__":
#         main()    