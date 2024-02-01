from model import Pessoa

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
            
    @classmethod
    def ler(cls):
        try:
            with open("pessoas.txt", "r") as arq:
                arq_pessoas = arq.read()
            return arq_pessoas
        except FileExistsError:
            return "Usuário não encontrado"
