# Alterar a ordem

import random
name = ['Alexander', 'Maria Moreira', 'Gabriela Lins', 'Ana Sofia']
sortName = random.shuffle(name)
osItens = ', '.join(name)
print('Essa é a sequencia de\napresentação dos trabalhos:\n{}'.format(osItens))
