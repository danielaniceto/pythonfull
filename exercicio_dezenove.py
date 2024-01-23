"""Receber 10 valores, e mostrar a soma de todos eles, isso usando listas, a ideia e
sempre separar todas as partes do codigo em funções diferentes"""

def is_sum_numbers_list(list_numbers):
    
    return sum(list_numbers)

"""e o mesmo que fazer assim
sum = 0
for i in list_numbers:
    sum = sum + i"""

def is_verification_list(list_numbers):
    if isinstance(list_numbers, (float, int)):
        return False
        
    else:
        return True   

def main():
    list_numbers = []
    cont = 0

    for cont in range (0, 10):
        numbers = float(input("Insert the number here: "))
        list_numbers.append(numbers)
        cont +=1

    verification_list = is_verification_list(list_numbers)
    if verification_list == False:
        print("there is something wrong with your numbers, please review")

    numbers_sum = is_sum_numbers_list(list_numbers)
    print(numbers_sum)

if __name__ == "__main__":
    main()
