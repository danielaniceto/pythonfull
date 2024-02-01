from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    def ler(self):
        nome = "Daniel"
        idade = 32
        cpf: 123445667755
        return Pessoa(nome, idade, cpf)

p1 = Pessoa("Daniel", 32, "12102910291")
PessoaDal.salvar(p1)