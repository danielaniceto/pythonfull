class Pessoa():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente

class Vendedor(Pessoa):
    def __init__(self, id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

print("Dados Pessoas!!!")

pessoa1 = Pessoa("Daniel", "1234456676")
print(pessoa1.nome)
print(pessoa1.cpf + "\n")

print("Dados Cliente!!!")

cliente1 = Cliente(1, "Sara", "2992339844984598")
print(cliente1.id_cliente)
print(cliente1.nome)
print(cliente1.cpf + "\n")

print("Dados Vendedor!!!")

vendedor1 = Vendedor(1, "Cintia", "2129183998434343")
print(vendedor1.id_vendedor)
print(vendedor1.nome)
print(vendedor1.cpf)
