"""
Este pequeño programa funciona para calcular el índice de masa corporal
de una persona ingresando su peso (Kg) y su altura (m). 
Ambos datos puede ser ingresados cómo un dato de tipo flotante.
"""

def run():

    bmi = bmi_calculator()
    print("Su índice de masa corporal (BMI) es de " + bmi)


def bmi_calculator():

    height = (input("Ingresa tu altura en metros (m): "))
    height = float(height)

    weight = input("Ingresa tu peso en kilogramos (Kg): ")
    weight = float(weight)

    bmi = weight / height ** 2
    bmi = round(bmi, 2)
    bmi = str(bmi)

    return bmi
   

if __name__ == "__main__":
    run()


# height = input("Ingrese su altura: ")
# height = float(height)
# weight = input("Ingrese su peso: ")
# weight = float(weight)
# bmi = weight / height ** 2
# bmi = str(bmi)
# print(bmi)