#Esse programa terá por função, receber do usuário 3 numeros, processar e apresentar o maior deste 3 numeros digitados

def is_validation_number(first_number, second_number, third_number):
    if not isinstance(first_number, (float, int)):
        raise Exception("Please, enter a valid number!!!\n")
    
    elif not isinstance(second_number,(float, int)):
        raise Exception("Please, enter a valid number!!!\n")
    
    elif not isinstance(third_number,(float, int)):
        raise Exception("Please, enter a valid number!!!\n")
    
    else:
        return "It's OK.\n"
    
def is_processing_higher_number(first_number, second_number, third_number):
    if first_number > second_number and first_number > third_number:
        return f"The largest number entered was the {first_number}\n"
    
    elif second_number > first_number and second_number > third_number:
        return f"The largest number entered was the {second_number}\n"
    
    elif first_number == second_number and first_number == third_number:
        return f"The tre numbens are equal's {first_number}, {second_number}, {third_number}"

    else:
        return f"The largest number entered was the {third_number}\n"

def main():
    first_number = float(input("Enter the first number here:"))
    second_number = float(input("Enter the second number here:"))
    third_number = float(input("Enter the third number here:"))

    validation_numbers = is_validation_number(first_number, second_number, third_number)
    print(validation_numbers)

    higher_number = is_processing_higher_number(first_number, second_number, third_number)
    print(higher_number)

main()