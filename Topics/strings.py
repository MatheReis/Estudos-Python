# Strings em python são cercadas por aspas simples ou duplas. Vejamos a formatação de string e alguns métodos de string de string

# name = 'Brad'
# age = 37

# Concatenado
# print('Hello, my name is ' + name + ' and I am ' + str(age))

# Formatação de string


# Argumentos por posição
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age}')

# Métodos Strings

from turtle import position


s = 'hello world'

# Strings Maiúsculas
print(s.capitalize())

# Todas as letras em Maiúscula
print(s.upper())

# Swap case
print(s.swapcase())

# Comprimento/tamanho da String
print(len(s))

# Substituir
print(s.replace('world', 'everyone'))

# Contar
sub = 'h'
print(s.count(sub))

# Inicia com
print(s.startswith('hello'))

# Termina com
print(s.endswith('d'))

# Dividir em uma lista
print(s.split())

# Encontrar posição
print(s.find('r'))

# É tudo alfanumérico
print(s.isalnum())

# É tudo alfabético
print(s.isalpha())

# É tudo numerico
print(s.isnumeric())
