from dal import PessoaDal
from controller import PessoaController

while True:
    decisao = int(input("Digite 1 para salvar, 2 para ver uma pessoa, ou 3 para sair: "))

    if decisao == 3:
        break
    
    elif decisao == 1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ")
        if PessoaController.cadastrar(nome, idade, cpf):
            print("Usuário cadastrado com sucesso")
        else:
            print("Digite valores válidos")
    
    elif decisao == 2:
        arq_pessoas = PessoaDal.ler()
        print(arq_pessoas)
