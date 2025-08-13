class Pessoa: # Superclasse
    def __init__(self, nomeuser, idadeuser):
        self.nome = nomeuser
        self.idade = idadeuser
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'O {self.nomeclasse} {self.nome} está falando...')

class Cliente(Pessoa): # Subclasse - herda os métodos e atributos da superclasse
    def comprar(self):
         # super().falar() - chama o método da superclasse dentro do método da subclasse, caso chame o método comprar() ele já irá chamar dentro dele falar()
         print(f'O {self.nomeclasse} {self.nome} está comprando...')

class Aluno(Pessoa): # Subclasse
    def estudar(self):
         print(f'O {self.nomeclasse} {self.nome} está estudando...')

c1 = Cliente('Ana', 19)
c1.falar() # método herdado
c1.comprar() # método específico de cliente

a1 = Aluno('Arthur', 19)
a1.falar()
a1.estudar()

p1 = Pessoa('Camila', 12 )
p1.falar()