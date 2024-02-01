"""O objetivo deste programa e apresentar apenas numeros pares, em um range de
numeros, começando por 0 a 1000, usando o laço de repetição FOR"""

def main():
    cont = 0
    for cont in range(0, 1000):
            if cont % 2 == 0:
                print(cont)
            cont += 1
            
if __name__ == "__main__":
    main()