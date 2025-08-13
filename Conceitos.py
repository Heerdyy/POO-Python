from datetime import datetime

# Classe - uma estrutura de dados personalizada usada para construir determinado objeto
class SemDado():
    pass # caso queira criar a classe sem nenhum dado dentro

# Métodos
class Gato():
    # Atributo - característica particular da uma ocorrência da classe 
    # Atributo de Classe
    tipo_animal = 'Felino'
    ano_atual = datetime.today().year


    # Método Construtor - um comportamento que inicializa atributos automaticamente
    def __init__(self, nome, idade):
        self.nome = nome  # g1.nome = nome_gato 
        self.idade = idade
        print(f'O nome do seu gato é {self.nome} e ele tem {self.idade} anos')

    # Método de Instância - um comportamento que precisa ser chamado para operar
    def peso_gato(self, peso):
        self.peso = peso
        if self.peso >= 5:
            print('O seu gato está goridinho >3')
        elif 5 > self.peso > 3.5:
            print('Seu gato está normal :)')
        else:
            print('Seu gato está magrinho :(') 

    # Métodos Utilitários

    # Método de Classe
    @classmethod
    def idade_gatinho(cls, nome, nasc):
        idade = cls.ano_atual - nasc
        return cls(nome, idade)
        
    # Método Estático - funciona sem o recebimento da classe ou instância
    @staticmethod        
    def num_aleatorio():
        from random import randint
        num = randint(0,10) 
        return num
        
# Objeto - são instânciados por classes 
g1 = Gato('kiki', 12)
g1.peso_gato(4) # chama o método peso_gato()

# usando o método de classe
# g1 = Gato.idade_gatinho('kiki', 2006)
# print(g1.nome, g1.idade)

# Atributos - representam os status do objeto  
print(g1.nome) # Atributo Instância
g1.tipo_animal = 'Pet'# Mudando o atributo da instância herdado pela classe
print(g1.tipo_animal)

print(Gato.tipo_animal) # Atributo Classe
Gato.tipo_animal = 'Animal' # Trocando o atributo da Classe
print(Gato.tipo_animal)

# OBS: O ideal para interagir com atributos é a utilização de métodos getters e setters

# Métodos Getters e Setters
class Teste():
    def __init__(self, valor):
        self.valor = valor

    # Método Getter
    @property
    def valor(self):
        return self._valor
    
    # Método Setter
    @valor.setter
    def valor(self, nvalor):
        self._valor = nvalor # ._valor necessário para indicar que é um atributo e não entrar em loop

numero = Teste(10)
print(numero.valor) # get


numero.valor = 5 # set 
print(numero.valor)