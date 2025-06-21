class Amigo:
    def __init__(self, nome, idade, descricao):
        self.nome = nome
        self.idade = idade
        self.descricao = descricao
    
    def Amigo_Esquizofrenico (self):
        print(f"Meu amigo esquizofrenico é {self.nome}, ele tem {self.idade} anos e {self.descricao}")



nome = input()
idade = input()
descricao = input()

amigo1 = Amigo(nome, idade, descricao)
amigo1.Amigo_Esquizofrenico()