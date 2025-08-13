# Ocultação de atributos para o bem do sistema
# public, protected, private (outras linguagens)

# 1. _ "protected" (funciona mais como uma recomendação)

class Pessoa():
    def __init__(self, nomeuser):
        self._nome = nomeuser # atributo nome protected

p1 = Pessoa('Ana')
print(p1._nome)

# Caso ocorra a tentativa de trocar esse atributo ainda é posível, mas, não é recomendado
p1._nome = 'Júlia'
print(p1._nome)

#  2. __ private

class Num():
    def __init__(self, numerouser):
        self.__numero = numerouser # atributo nome private

n1 = Num(2)
# print(n1.__numero) # o atributo quando privado é renomeado para impedir o acesso
print(n1._Num__numero) # só podendo ser acessado assim, mas, ainda é possivel acessá-lo externamente apenas torna mais complicado
n1._Num__numero = 4 
print(n1._Num__numero)

# Ambos sinalizam que o atributo deve ser acessado apenas dentro da classe ou é recomendado no caso
# Para interagir com o atributo é uma boa prática a utilização de métodos getters e setters