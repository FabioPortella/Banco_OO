from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod  
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV ...")
        print("Desligada!")

    @property
    def marca(self):
        return "Samsung"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controleTV = ControleTV()
controleTV.ligar()
controleTV.desligar()
print(controleTV.marca)

controleAC = ControleArCondicionado()
controleAC.ligar()
controleAC.desligar()
print(controleAC.marca)