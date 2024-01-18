"""O foco deste programa e usar o laço FOR para montar uma tabuada completa
sem influência do usuário"""

def main():
    for i in range(0, 11):
        for j in range(0, 11):
            print(f"{i} x {j} = {i * j}")
        i += 1
        j += 1
if __name__ == "__main__":
    main()
