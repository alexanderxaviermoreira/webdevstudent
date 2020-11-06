from time import sleep
print('\nNúmero par ou ímpar.\n')
numero = int(input('\nDiga um número qualquer: '))
print('ANALISANDO...')
sleep(3)
if numero % 2 == 0:
    print('O número \33[2;31m {} \33[m é PAR.'.format(numero))
else:
    print('O número \33[2;34m {} \33[m é ÌMPAR.'.format(numero))
