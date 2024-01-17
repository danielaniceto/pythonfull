def is_teste_soma_inteiros( numeros_inteiros, targetSum):

    armazena_numeros_lista = {}

    for elemento in numeros_inteiros:
        indentifica_elemento = targetSum - elemento

        if indentifica_elemento in armazena_numeros_lista:
            return [indentifica_elemento, elemento]
        
        armazena_numeros_lista[elemento] = True

    else:
        return[]
    
def main():
    numeros_inteiros = [4, 5, -8, -4, 12, 22, 7]
    targetSum = 9

    resultado = is_teste_soma_inteiros(numeros_inteiros, targetSum)
    print (resultado)

if __name__ == "__main__":
    main()
