from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
            
    @classmethod
    def ler(cls):
        nome = "Daniel"
        idade = 32
        cpf = 12123566565
        return Pessoa(nome, idade, cpf)

p1 = Pessoa("Daniel", 32, "12102910291")
PessoaDal.salvar(p1)

print(PessoaDal.ler().nome)
print(PessoaDal.ler().idade)
print(PessoaDal.ler().cpf)
