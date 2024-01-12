#esse programa, deve receber F referente ao sexo feminino, e M referente ao sexo masculino, analizar e retornar ao usuário seu sexo.

def is_validation_letter(letter):
    if letter != "M" or letter != "F":
        return ""


def main():
    letter = input("Enter the letter here, the options is M for Marculine and F for Feminine: ")

    the_validation_letter = is_validation_letter(letter)