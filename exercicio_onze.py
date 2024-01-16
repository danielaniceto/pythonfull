"""Defina um usuário e senha, e faça a validação deste,
recenbendo do user seus acesso e depois validando"""

def is_validation_user():


def main():
    user = "Daniel"
    password = "1234abcd"

    user_validation = input("Please, enter your user for login in this program: ")
    password_validation = input("Please, enter your passowrd now: ")

    user_validation_system = is_validation_user(user_validation, user)
    print(user_validation_system)

    password_validation_system = ins_validation_password(password_validation, password)
    print(password_validation_system)

    if user_validation_system == True and password_validation_system == True:
