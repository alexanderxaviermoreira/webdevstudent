# Importação de bilbliotecas
# import math - importa todas a biblioteca
#       math.sqrt(variavel)
# from math import sqrt - importa só o "sqrt"
#       sqrt(variavel) - sem o "math"
# from math import sqrt, floor, ceil - importa algumas

from math import sqrt, floor, ceil
import random
import emoji

numFirst = random.random()
numSec = random.randint(1, 1000)  # Aleatório entre 1 e 100
print(numFirst)
print(numSec)
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrade de {} é {}'.format(num, raiz))
print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))
print('A raiz quadrada de {} é {}'.format(num, ceil(raiz)))

print(emoji.emojize('Olá Mundo  :earth_africa:', use_aliases=True))

