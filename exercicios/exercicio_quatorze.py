"""Esse programa tem por função fazer a identificação de elementos de uma string, analisar
e retornar a quantidade de elementos, limitado a no maximo 10 unidades de cada, acima de 10
deve retornar o valor referente as dezenas de dados"""

def is_compressao_da_strind(u):
    if not u:
        return ""

    compressao = ""
    contador = 1

    for i in range(1, len(u)):
        if u[i] == u[i - 1]:
            contador += 1

        else:
            compressao += str(contador) + u[i - 1] if contador > 1 else u[i - 1]
            contador = 1

    compressao += str(contador) + u[-1] if contador > 1 else u[-1]

    return compressao

def main():
    stringe_recebida = "XXXXXX##44444@@@@FFFFFDDDD*****"
    string_analisada = is_compressao_da_strind(stringe_recebida)
    print(string_analisada)

if __name__ == "__main__":
    main()
