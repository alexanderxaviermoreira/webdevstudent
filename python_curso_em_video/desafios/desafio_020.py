# Alterar a ordem

import random
al01 = str(input('Aluno 01 '))
al02 = str(input('Aluno 02 '))
al03 = str(input('Aluno 03 '))
al04 = str(input('Aluno 04 '))
names = [al01, al02, al03, al04]
random.shuffle(names)
osItens = ', '.join(names)
print('Essa é a sequencia de\n'
      'apresentação dos trabalhos:\n'
      '{}'.format(osItens))
