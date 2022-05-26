"""
Quiero replicar el encriptado Ceasar con rotación 13

- Ingresa el mensaje a encriptar
  - Quito los espacios y pongo en mayúscula

- Encripto el mensaje en cifrado Ceasar con rotación 13

- Imprimo el mensaje encriptado   
"""

def rotacion_13():

# Ingreso mensaje, quito espacios y pongo en mayúscula
    mensaje = input("Escribe el mensaje a encriptar: ").upper().replace(" ", "")

# Encripto el mensaje en cifrado Ceasar con rotación 13
    abecedario =    "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_13 = "NOPQRSTUVWXYZABCDEFGHIJKLM"

# Reemplazo el mensaje por su equivalente en el abecedario rotado 13
    mensaje_encriptado = ""
    for letra in mensaje:
        mensaje_encriptado += abecedario_13[abecedario.index(letra)]
    print(mensaje_encriptado)



if __name__ == "__main__":
    rotacion_13()    