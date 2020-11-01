print('\nSorteio um número definido pelo póprio programa.')

from random import randint
from time import sleep

# sorteio = random.randrange(0, 5)
sorteio = randint(0, 5)

numero = int(input('\nDiga um número entre "0" e "5": '))

print('\nPENSANDO.....\n')
sleep(3)

if sorteio == numero:
    print('=> O número está correto.')
else:
    print('=> O número está incorreto. Tente outra vez.')



