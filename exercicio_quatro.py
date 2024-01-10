#receber 4 notas de um aluno, e apontar se ele foi aprovado ou reprovado em um curso

def is_notas_validation(primeira_nota, segunda_nota, terceira_nota, quarta_nota):
    if not isinstance(primeira_nota,  (float, int)):
        raise Exception("Digite um valor de nota válido por favor!!!")
    
    elif not isinstance(segunda_nota, (float, int)):
        raise Exception("Digite um valor de nota válido por favor!!!")
    
    elif not isinstance(terceira_nota, (float, int)):
        raise Exception("Digite um valor de nota válido por favor!!!")
    
    elif not isinstance(quarta_nota, (float, int)):
        raise Exception("Digite um valor de nota válido por favor!!!")

    elif primeira_nota < 0 or segunda_nota < 0 or terceira_nota < 0 or quarta_nota < 0:
        raise Exception ("Suas notas não podem ser menores que zero")
    
    else:
        return "Validação ok!!!\n"
    
def is_aluno_analisation(nome_aluno, nota_media):
      
    if nota_media >= 6:
        return f"Caro aluno {nome_aluno} sua nota média foi de {nota_media}, e você foi aprovaado!!!, PARABENS\n"
    
    elif nota_media <= 4:
        return f"Caro aluno {nome_aluno} sua nota média foi de {nota_media}, e você foi reprovado!!!, DESCULPE\n"

def is_media_calculation(primeira_nota, segunda_nota, terceira_nota, quarta_nota):
    nota_media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

    return nota_media

def main():
    nome_aluno = input("Digite seu nome aqui: ")
    primeira_nota = float(input("Digite sua primeira nota: "))
    segunda_nota = float(input("Digite sua segunda nota: "))
    terceira_nota = float(input("Digite sua terceira nota: "))
    quarta_nota = float(input("Digite sua quartaa nota: "))

    validacao_notas = is_notas_validation(primeira_nota, segunda_nota, terceira_nota, quarta_nota)
    nota_media = is_media_calculation(primeira_nota, segunda_nota, terceira_nota, quarta_nota)
    situacao_aluno = is_aluno_analisation(nome_aluno, nota_media)

    print(validacao_notas)
    print(situacao_aluno)

main()