"""O objetivo deste programa e de verificar se seria ou não possível, tirar fotos de alunos,
levando em consideração sua altura e cores de uniformes usados"""

def is_verifica_possibilidade(metade_uniforme_laranja, metade_uniforme_preto):
    if len(metade_uniforme_preto) != len(metade_uniforme_laranja):
        return False

    metade_uniforme_preto.sort()
    metade_uniforme_laranja.sort()

    for u in range(len(metade_uniforme_preto)):
        if metade_uniforme_preto[u] >= metade_uniforme_laranja[u]:
            return False
        
    return True

def main():
    metade_uniforme_laranja = [162, 175, 153, 128, 199]
    metade_uniforme_preto = [187, 139, 207, 165, 168]

    verificar_possibilidade_foto = is_verifica_possibilidade(metade_uniforme_laranja, metade_uniforme_preto)
    print(verificar_possibilidade_foto)

if __name__ == "__main__":
    main()
    