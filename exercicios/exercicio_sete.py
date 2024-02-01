#esse programa, deve receber F referente ao sexo feminino, e M referente ao sexo masculino, analizar e retornar ao usuário seu sexo.

def is_validation_letter(letter):
    if letter != "M" and letter != "F" and letter != "m" and letter != "f":
        return "Your letter is not valid!!!, please take a 'M' or 'F'\n"
    
    elif type(letter) != str:
        return "Your enter is not a letter, please take a 'M' or 'F'\n"
    
    elif type(letter) == str:
        return "It's OK, your letter is valid!!!\n"

def is_avaliation_letter(letter):
    if letter == "M" or letter == "m":
        return "You are male\n"
    
    elif letter == "F" or letter == "f":
        return "You are female\n"
    
    else:
       return "Bye"

def main():
    letter = input("Enter the letter here, the options is M for Male and F for Female: ")

    the_validation_letter = is_validation_letter(letter)
    print(the_validation_letter)

    the_letter_avaliation = is_avaliation_letter(letter)
    print(the_letter_avaliation)

main()