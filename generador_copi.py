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

- Imprimo el mensaje

abecedaario =        "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
abecedario inverso = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

"""


def mensaje_encriptado():

# Ingreso mensaje, quito espacios y pongo en mayúscula
    mensaje = input("Escribe el mensaje a encriptar: ").upper().replace(" ", "")
    print(mensaje)
    
# Desgloso el mensaje en el abecedario
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    abecedario_invertido = abecedario[::-1]

# Reemplazo el mensaje por su equivalente en el abecedario invertido
    mensaje_encriptado = ""
    for letra in mensaje:
        mensaje_encriptado += abecedario_invertido[abecedario.index(letra)]
    print(mensaje_encriptado)


if __name__ == "__main__":
    mensaje_encriptado()
    