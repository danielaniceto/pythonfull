"""O objetivo deste programa e de realizar uma tabuada dado o numero que o user inserir"""

def is_check_number(number_multiplication_table):
    if type(number_multiplication_table) != int:
        raise Exception ("Please, your number is not valid!!")
    
    else:
        return "Its ok!!!"


def main():
    number_multiplication_table = int(input("Enter the number for multiplication table here: "))

    number_check = is_check_number(number_multiplication_table)
    print(number_check)