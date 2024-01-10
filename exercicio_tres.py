#Crie um programa onde o usuário insira duas notas, e tenha como retorno a nota média

def is_valida_notas(nota_um, nota_dois):
    if not isinstance(nota_um, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif not isinstance(nota_dois, (float, int)):
        raise Exception ("Por favor, digite um numero correto!!!")
    
    elif nota_um and nota_dois < 0:
        raise Exception ("Não existem notas negativas!!!")
       
    else:
        return "Validação ok"
    
def is_calcula_media(nota_um, nota_dois):
    nota_media = (nota_um + nota_dois) / 2

    return f"Sua nota media e {nota_media} pontos"

def main():
    nota_um = float(input("Digite sua primeira nota: "))
    nota_dois = float(input("Digite sua segunda nota: "))

    validacao_notas = is_valida_notas(nota_um, nota_dois)

    calcula_media = is_calcula_media(nota_um, nota_dois)

    print(validacao_notas)
    print(calcula_media)

main()


