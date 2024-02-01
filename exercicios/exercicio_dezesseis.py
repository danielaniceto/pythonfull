""" O foco desse programa e trabalhar o uso do FOR, pra isso vamos montar um codigo
que mostre a tabuada de um numero recebido pelo usuário, usando o laço FOR. """

def is_validation_type_number_user(number_multiplication_table):
    if type(number_multiplication_table) != int:
        raise Exception ("Please, your number is not valid!!\n")
    
    else:
        return "Its ok!!!\n"
    
def is_multiplication_table(number_multiplication_table):
    i = 1
    for i in range(0, 11):
        print(f"{i} x {number_multiplication_table} = {i * number_multiplication_table}")
        i += 1

def main():
    number_multiplication_table = int(input("Enter the number for multiplication table here: "))

    validation_number_user = is_validation_type_number_user(number_multiplication_table)
    print(validation_number_user)

    is_multiplication_table(number_multiplication_table)

if __name__ == "__main__":
    main()
