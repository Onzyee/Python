cadastro = False
class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome 
        self.turma = turma
        self.nota = nota
        self.cadastro = cadastro


    def Pessoa (self):
        self.nome = []
        self.turma = []
        self.nota = []
        cont = 0
        cond = True
        resp = ""
        cadastro = True
        if cadastro == True:
            while cond == True:
                print("Nome do aluno: ")
                nometemp = input()
                while cont <= len(self.nome):
                    if self.nome[cont] == nometemp:
                        cont = cont+1
                    elif len(self.nome[cont]) >= cont:
                        print("Aluno já cadastrado!")
                        cont = 999
                    else:
                        self.nome.append = input()
                        cont = 999
                        cond = False
            cond = True
            cont = 0
            while cond == True:
                print("Turma do aluno: ")
                turmatemp = input()
                while cont <= turma:
                    if self.turma[cont] == turmatemp:
                        cont = cont+1
                    elif self.turma[cont] >= cont:
                        print("Aluno já cadastrado!")
                        cont = 999
                    else:
                        self.turma.append = input()
                        cont = 999
                        cond = False
            cadastro = False
        print("Deseja cadastrar as notas deste aluno? [S/N]")
        resp.lower = input()
        if resp == "s" or resp == "sim":
            cadastro = True
            while cadastro == True:
                cond = True
                while cond == True:
                    while cont <= nome:
                        if nome[cont] == nometemp:
                            id_aluno = cont
                            cond = False
                            cont = 999
                        elif nome[cont] >= cont:
                            
                            cont = 999
                        else:
                            nome.append = input()
                            cont = 999
                            cond = False

nome = input
turma = input
nota = input
Aluno1 = Aluno(nome, turma, nota)
Aluno1.Pessoa()
        
"""
class Notas:
    def __init__(self):
        
    def Add_Nota(self):
    
    def Media(self):


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
"""
