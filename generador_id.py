import random


def id_generator():
    id_card = input("Ingrese su número de cédula: ")
    last_name = input("Ingrese su nombre: ")
    first_name = input("Ingrese su apellido: ")
    nationality = input("Ingrese su nacionalidad: ")
    input_date = input("Ingrese su fecha de entrada MM/DD/AA (Ej. 03/20/21): ")

    random_number = random.randint(1000,9999)

    # id_card = str(id_card)
    # input_date = str(input_date)
    random_number = str(random_number)

    first_name = first_name[:3]
    last_name = last_name[:3]
    nationality = nationality[:3]
    id_card = id_card[:3]
    input_date = input_date[:3]

    list_id_card = list(id_card)
    list_first_name = list(first_name)
    list_last_name = list(last_name)
    list_nationality = list(nationality)
    list_input_date = list(input_date)
    list_random_number = list(random_number)

    join_list = list_id_card + list_first_name + list_last_name + list_nationality + list_input_date + list_random_number

    exclusive_id = []

    for i in range(15):
        random_id = random.choice(join_list)
        exclusive_id.append(random_id)

    exclusive_id = "".join(exclusive_id)
    return exclusive_id

        

def run():
    exclusive_id = id_generator()
    print("Tu ID único y exclusivo es: "+ exclusive_id)
    

if __name__ == "__main__":
    run()