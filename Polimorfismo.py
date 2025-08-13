# Polimorfismo - o mesmo método assumindo comportamentos diferentes
class Pessoa():
    def __init__(self,nomeuser):
        self.nome = nomeuser

    def fazendo_algo(self):
        print(f'{self.nome} está falando...')
    
class Aluno(Pessoa): 
    def fazendo_algo(self): # override
        print(f'Aluno {self.nome} está comendo...')

p1 = Pessoa('Arthur')
p1.fazendo_algo()

a1 = Aluno('Ana')
a1.fazendo_algo() 