# Uma variável é um contêiner para um valor, que pode ser de vários tipos

'''
Este é um comentário de várias linhas ou docstring 
(usado para definir a finalidade de uma função) 
pode ser aspas simples ou duplas
'''

"""
Regras Variáveis:

 -Os nomes das variáveis ​​diferenciam maiúsculas de minúsculas (nome e NOME são variáveis ​​diferentes);
 -Deve começar com uma letra ou um sublinhado;
 -Pode ter números, mas não pode começar com um;
"""

x = 1           # int
y = 2.5         # float
name = 'John'   # str
is_cool = True  # bool

# Multiplas Atribuições
x, y, name, is_cool = (1, 2.5, 'John', True)

print(x, y, name, is_cool)

# Matemática básica
a = x + y

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)
