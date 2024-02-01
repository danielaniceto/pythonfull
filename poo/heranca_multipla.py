"""O objetivo deste codigo e de trabalhar e entender mais sobre a herança multipla!!!"""

class Animal():
    def andar(self):
        print("Estou andando como um animal")
    
    def correr(self):
        print("Estou correndo")
    
    def pular(self):
        print("Estou pulando")

class Felino(Animal):
    def felino(self):
        print("Eu sou um felino!!!")
    
class Gato(Felino):
    def miar(self):
        print("Eu estou miando!!!\n")
    
class Cachorro(Animal):
    def latir(self):
        print("Eu estou latindo!!!\n")

print("Gato!!!")
gato = Gato()
gato.andar()
gato.correr()
gato.pular()
gato.miar()

print("Cachorro!!!")
cachorro = Cachorro()
cachorro.andar()
cachorro.correr()
cachorro.pular()
cachorro.latir()

