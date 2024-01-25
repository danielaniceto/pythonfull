"""Fazer um programa onde o usuário possa armazenar um numero indeterminado de
pessoas, usando lista e dicionários, os atributos são, nome, idade, altura das
pessoas"""

def is_add_info_pleoples(name, age, height, peoples):
    people = {'nome' : name, 'age' : age, 'heigth' : height}
    
    peoples.append(people)

    return peoples      

def main():
    peoples = []

    while True:
        decision = int(input("Press 2 for out or 1 for new register: "))
        if decision == 2:
            break

        name = input("Please enter the name here: ")
        age = input("Please, enter the age here: ")
        height = input("Please, enter the height here: ")
        
        is_add_info_pleoples(name, age, height, peoples)

    print(peoples)

if __name__ == "__main__":
    main()
    