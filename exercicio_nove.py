"""O objetivo deste programa e de realizar uma tabuada dado o numero que o user inserir"""

def is_check_number(number_multiplication_table):
    if type(number_multiplication_table) != int:
        raise Exception ("Please, your number is not valid!!\n")
    
    else:
        return "Its ok!!!\n"

def is_multiplication_table(number_multiplication_table):
    i = 1
    while i <= 10:
        print(f"{number_multiplication_table} x {i} = {number_multiplication_table * i}")
        i += 1

def main():
    number_multiplication_table = int(input("Enter the number for multiplication table here: \n"))

    number_check = is_check_number(number_multiplication_table)
    print(number_check)

    multiplication_table = is_multiplication_table(number_multiplication_table)

main()
