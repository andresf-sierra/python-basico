import random
from typing import Mapping


def run():
    numerorandom = random.randint(1, 100)
    numeroelegido = int(input("Introduce el número del 1 a 100:"))
    vidas = 6
    while numerorandom != numeroelegido:
        if numerorandom < numeroelegido:
            print("Elige un número más pequeño")
            vidas -= 1
        elif numerorandom > numeroelegido:
            print("Eige un número más grande")
            vidas -= 1
        if vidas == 0:
            print("¡FALLASTE!")
            break
        print("Tienes", vidas, "vidas")
        numeroelegido = int(input("Introduce un número de 1 a 100: "))
    if numerorandom == numeroelegido:
        print("FELICIDADES, HAS GANADO")            


if __name__ == '__main__':
    run()



