# Classe - uma estrutura de dados personalizada usada para construir determinado objeto
class SemDado():
    pass # caso queira criar a classe sem nenhum dado dentro

# Métodos
class Gato():
    # Atributo - característica particular da uma ocorrência da classe 
    # Atributo de Classe
    tipo_animal = 'Felino'

    # Método Construtor - um comportamento que inicializa atributos automaticamente
    def __init__(self, nome):
        self.nome = nome # g1.nome = nome_gato 
        print(f'O nome do seu gato é {self.nome}')

    # Método geral - um comportamento que precisa ser chamado para operar
    def peso_gato(self, peso):
        self.peso = peso
        if self.peso >= 5:
            print('O seu gato está goridinho >3')
        elif 5 > self.peso > 3.5:
            print('Seu gato está normal :)')
        else:
            print('Seu gato está magrinho :(') 
    
    # Método Utilitário - usado para realizar tarefas específicas dentro da classe, podendo ser acessado também por outros métodos
    def _dieta_gato(self):
        self.status = 'Tudo certo!!'
        if self.peso > 5:
            self.status = 'Diminua a ração do seu felino'
        if self.peso < 3.5:
            self.status = 'Aumente a ração do seu felino'
        return self.status
        
    def formulario(self):
        print(f'O nome do seu gatinho é {self.nome} e ele pesa {self.peso}kg')
        print(self._dieta_gato())

# Objeto - são instânciados por classes 
nome_gato = str(input('Qual o nome do seu gato? '))
g1 = Gato(nome_gato)

peso = float(input('Qual o peso do seu gatinho? '))
g1.peso_gato(peso) # chama o método peso_gato()

g1.formulario()

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
    def get_valor(self):
        return self.valor
    
    # Método Setter
    def set_valor(self, nvalor):
        self.valor = nvalor

numero = Teste(10)
print(numero.get_valor())

valor_novo = int(input('Digite um valor: '))
numero.set_valor(valor_novo)
print(numero.get_valor())