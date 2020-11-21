'''print('For com range\n')

for counter in range(0, 6):
    print(counter, 'Counter')
print('\nFIM\n')

print('For com range. Nada acontece\n')

for counter1 in range(6, 1):
    print(counter1, 'Counter 1')
print('\nFIM\n')

print('For com range. Reverso um a um\n')

for counter2 in range(6, 0, -1):
    print(counter2, 'Counter 2')
print('\nFIM\n')

print('For com range. 0 a 7 de dois em dois\n')

for counter3 in range(0, 7, 2):
    print(counter3, 'Counter 3')
print('\nFIM\n')

print('For com range. Limite\n')

numero  = int(input('Diga um número: '))
for i in range(0, numero):
    print('Número: ', i)
print('\nEND')

print('For com range. Com intervalo pedido\n')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for couter4 in range(i, f, p):
    print('Número: ', couter4)
print('\nEND')

print('For com range. Com intervalo\n')

for counter5 in range(1, 20, 3):
    print('Número: ', counter5)
print('\nEND\n')

print('For com range. Input no laço\n')

for counter6 in range(0, 5):
    num = int(input('Digite um número: '))
print('\nEND\n')'''

print('For com range. Somátório\n')

s = 0
for counter7 in range(0, 5):
    num = int(input('Digite um número: '))
    s += num
print('Somatório: {}'.format(s))