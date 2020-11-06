from time import sleep

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
lista = [n1, n2, n3]
print('\n => Analisando..... \n')
sleep(2)
menor = min(lista)
maior = max(lista)
print('\n Menor número: \033[4;30;44m {} \033[m \n'.format(menor))
print('\n Maior número: \033[4;30;44m {} \033[m \n'.format(maior))

print('-x' * 20, '\n\n')

a = int(input('Nr 01: '))
b = int(input('Nr 02: '))
c = int(input('Nr 03: '))
_menor = a
if b < a and b < c:
    _menor = b
if c < a and c < b:
    _menor = c

_maior = a
if b > a and b > c:
    _maior = b
if c > a and c > b:
    _maior = c

print('Menor: {}'.format(_menor))
print('Maior: {}'.format(_maior))
