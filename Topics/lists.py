# Uma lista é uma coleção ordenada e mutável. Permite membros duplicados

# Criar lista
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']


# Usar um construtor
# numbers2 = list((1, 2, 3, 4, 5))

# Obter valor
print(fruits[1])

# Obter o tamnho da lista
print(len(fruits))

# Acrescentar um item na lista
fruits.append('Mangos')

# Remover da lista
fruits.remove('Grapes')

# Inserir na posição
fruits.insert(2, 'Strawberries')

# Alterar valor
fruits[0] = 'Bluberries'

# Remover com pop
fruits.pop(2)

# Lista Reversa => Ela inverte a ordem da lista
fruits.reverse()

# Lista de classificação
fruits.sort()

# Lista de classificação reversa
fruits.sort(reverse=True)

print(fruits)
