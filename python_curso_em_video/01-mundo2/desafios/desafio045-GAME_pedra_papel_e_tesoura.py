''' Jogo do Jokenpô Pedra, Papel, Tesoura '''

import random
from time import sleep

escolha = str(input('\nEscolha pedra, papel ou tesoura: '))
print('Você escolheu: {}'.format(escolha))

j1 = 'pedra'
j2 = 'papel'
j3 = 'tesoura'
jokenpo = [j1, j2, j3]
sorteio = random.choice(jokenpo)
print('Aguarde o sorteio...')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('\033[30;41m{:=^40}\033[m'.format('O computador sorteou: {}').format(sorteio))

if escolha == 'pedra' and sorteio == j1 or escolha == 'papel' and sorteio == j2 or escolha == 'tesoura' and sorteio == j3:
    print('=> Deu empate.\nJogue outra vez.')
elif escolha == 'pedra' and sorteio == j2:
    print('=> O computador ganhou.')
elif escolha == 'pedra' and sorteio == j3:
    print('=> Você ganhou.')
elif escolha == 'papel' and sorteio == j3:
    print('=> O computador ganhou.')
elif escolha == 'pedra' and sorteio == j2:
    print('=> O computador ganhou.')
elif escolha == 'tesoura' and sorteio == j1:
    print('=> O computador ganhou.')
elif escolha == 'papel' and sorteio == j1:
    print('=> Você ganhou.')
elif escolha != 'pedra' or escolha != 'papel' or escolha != 'tesoura':
    print('Escolha outra vez!!!')



'''
from random import randint
variavel = randint(0, 2)
'''