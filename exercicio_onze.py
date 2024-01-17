"""Defina um usuário e senha, e faça a validação deste,
recenbendo do user seus acesso e depois validando"""

def is_validation_user(user_validation, USER):
    if user_validation == USER:
        return True
    else:
        return "\n Sorry, user or password is not ok, please check your acess \n"

def ins_validation_password(password_validation, PASSWORD):
    if password_validation == PASSWORD:
        return True
    
    else:
        return "Sorry, user or password is not ok, please check your acess \n"

def is_validation_acess_user(password_validation_system, user_validation_system):
    if password_validation_system == True and user_validation_system == True:
        return "Acess ok!!!"
    
    else:
        return "Acess blocked"

def main():
    while True:
        USER = "Daniel"
        PASSWORD = "1234abcd"

        user_validation = input("Please, enter your user for login in this program: ")
        password_validation = input("Please, enter your passowrd now: ")

        user_validation_system = is_validation_user(user_validation, USER)
        print(user_validation_system)

        password_validation_system = ins_validation_password(password_validation, PASSWORD)
        print(password_validation_system)

        validation_acess_user = is_validation_acess_user(user_validation_system, password_validation_system)
        print(validation_acess_user)
        
        if validation_acess_user == "Acess ok!!!":
            break

if __name__ == "__main__":
    main()
