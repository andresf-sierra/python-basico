def sumacubos(n):
    return sum(i**3 for i in range(1,n+1))
    # for i in range(n):
        


def main():
    #numero = int(input("Inserte el número el cuál desea conocer la suma de cubos: "))  
    numero = int(3) 
    # n = numero + 1
    # for i in range(numero):
    #     n = n - 1
    print("El resultado es: ", sumacubos(numero))

main()    
