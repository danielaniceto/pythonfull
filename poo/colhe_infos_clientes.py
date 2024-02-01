"""O objetivo desse programa e trabalhar e aprimorar a construção e o uso de funções e classes"""

from class_pessoa import PessoasClientes

def main():

    nome_cliente = input("Digite seu nome para cadastro: ")
    idade_cliente = int(input("Digite sua idade: "))
    cpf_cliente = int(input("Digite seu CPF aqui: "))
    endereco_cliente = input("Digite seu endereço aqui: ")

    PessoasClientes(nome_cliente, idade_cliente, cpf_cliente, endereco_cliente)

if __name__ == "__main__":
    main()
