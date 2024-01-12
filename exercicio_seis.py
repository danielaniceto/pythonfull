# Esse programa deve receber um numero, processa-lo e retornar se este numero e positivo ou negativo
def is_validation_number(number):
    if type(number) == str:
        return "Sorry, but this object is not a number"
    
    elif not isinstance(number, (float, int)):
        raise Exception ("Sorry, this number is not valid!!!, please enter a valid number")
    
    else:
        return "It's OK, your number is valid!!!\n"

def is_to_analyze_number(number):
    if number < 0:
        return "This is a negative number\n"
    
    elif number == 0:
        return "Zer is a neutral number\n"
    
    else:
        return "This is a positive number\n"

def main():
    number = float(input("Enter the number here: "))

    validation_number = is_validation_number(number)
    print(validation_number)

    number_analyzed = is_to_analyze_number(number)
    print(number_analyzed)

main()