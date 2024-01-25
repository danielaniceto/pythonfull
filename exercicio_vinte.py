"""Fazer um programa onde o usuário possa armazenar um numero indeterminado de
pessoas, usando lista e dicionários, os atributos são, nome, idade, altura das
pessoas"""

def is_add_info_pleoples(name, age, height, decision):
    peoples = []
    if decision == 1:
        people = {'nome' : name, 'age' : age, 'heigth' : height}

        peoples.append(people)

    return peoples

def main():
    while True:
        decision = int(input("Press 2 for out or 1 for new register: "))
        if decision == 2:
            break

        name = input("Please enter the name here: ")
        age = input("Please, enter the age here: ")
        height = input("Please, enter the height here: ")

        add_inf_peoples = is_add_info_pleoples(name, age, height)

    print(add_inf_peoples)

if __name__ == "__main__":
    main()
    