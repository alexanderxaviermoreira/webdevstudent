nome = str(input('Digite um nome: ')).replace(' ', '').lower()
quantidade = nome.count('a')
print('A letra "A" aparece {} vezes'.format(quantidade))
primeiraPosicao = nome.find('a')
print('A letra "A" aparece pela primeira vez na posiçao {}'.format(primeiraPosicao))
ultimaPosicao = nome.rfind('a')
print('A letra "A" aparece pela última vez na posição {}'.format(ultimaPosicao))