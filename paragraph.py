def run():
    paragraph = input("Ingresa un parrafo: ")
    print(count_letters(paragraph))
    print(count_letters_two(paragraph))
    

def count_letters(paragraph):
    count = 0
    for letter in paragraph:
        count += 1
    return count

def count_letters_two(paragraph):
    return len(paragraph)            

if __name__ == "__main__":
    run()

