#Receber 10 valores, e mostrar a soma de todos eles, isso usando listas, a ideia e sempre separar todas as partes do codigo em funções diferentes

def is_sum_numbers_list(list_numbers):
    cont = 0
    for cont in range(0, 10):
        numbers_sum = list_numbers[cont]


def main():
    list_numbers = []
    cont = 0

    for cont in range (0, 10):
        numbers = int(input("Take the number here: "))
        list_numbers.append(numbers)
        cont +=1

    numbers_sum = is_sum_numbers_list(list_numbers)
    print(numbers_sum)

if __name__ == "__main__":
    main()


        

