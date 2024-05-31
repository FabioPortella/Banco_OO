class Estudante:
    escola = "DIO"  # Atributo de classe

    def __init__(self, nome, matricula) -> None:
        # Atributos de instância - self.xxx
        self.nome = nome  
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

fabio = Estudante("Fabio", 1)
joao = Estudante("João Pedro", 2)
mostrar_valores(fabio, joao)

Estudante.escola = "Soares de Oliveira"
fabio.matricula = 3
mostrar_valores(fabio, joao)
