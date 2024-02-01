"""Esse programa deve identificar e processar os numeros pares em um range de 0
ate o valor que o user digitar, mostrando-os em tela após o processo."""

def is_validation_type_number(number):
    if type(number)!= int:
        return "Please, enter the number correct!! \n"
    
    else:
        return "Every ok, number valid !!!\n"

def is_even_number_separations(number):
    cont = 0
    while cont <= number:
        if cont % 2 == 0:
            print(cont)
        cont += 1

def main():
    number = int(input("Enter the number here: "))

    validation_type_number = is_validation_type_number(number)
    print(validation_type_number)

    even_numbers = is_even_number_separations(number)
    print(even_numbers)

if __name__ == "__main__":
    main()
