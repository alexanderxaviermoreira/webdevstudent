# Sorteio de nome

import random
''' names = ['Alexander', 'Maria', 'Gabriela', 'Ana sofia']
sortName = random.choice(names)
print('O aluno que apagará o quadro é {}'.format(sortName))'''

n1 = str(input('Aluno 01 '))
n2 = str(input('Aluno 02 '))
n3 = str(input('Aluno 03 '))
n4 = str(input('Aluno 04 '))
listaAlunos = [n1, n2, n3, n4]
sortName = random.choice(listaAlunos)
print('\nO aluno escolhido foi {}'.format(sortName))

