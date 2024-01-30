"""O objetivo desse programa e trabalhar e aprimorar a construção e o uso de funções e classes"""

from class_pessoa import PessoasClientes

def forma_mensagem_cliente(self):

    infos_pessoa = (f"Olá {PessoasClientes.nome}, seu cadastro foi feito com sucesso, sua idade e de {PessoasClientes.idade},
        seu CPF e {PessoasClientes.cpf}, e seu endereço e {PessoasClientes.endereco}")
    
    return infos_pessoa
