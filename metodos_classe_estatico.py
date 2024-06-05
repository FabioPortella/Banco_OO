class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome 
        self.idade = idade

    @classmethod
    def criar_por_data_nascimento(cls, dia, mes, ano, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_por_data_nascimento(17, 6, 1970, "Fabio")
print(p.nome, p.idade)

print(Pessoa.maior_idade(17))
print(Pessoa.maior_idade(54))