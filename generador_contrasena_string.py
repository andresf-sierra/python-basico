import random
import string

def make_password():

    MAYUS = list(string.ascii_uppercase)
    MINUS = list(string.ascii_lowercase)
    NUMS = list(string.digits)
    CHARS = list(string.punctuation)
   

    character = MAYUS + MINUS + NUMS + CHARS

    password = []

    for i in range(15):
        character_random = random.choice(character)
        password.append(character_random)

    password = ''.join(password) 
    return password   


def run():
    password = make_password()
    print("Tu nueva contraseña es: "+ password)

if __name__ == "__main__":
    run()
