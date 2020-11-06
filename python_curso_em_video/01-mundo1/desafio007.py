# Dobro, Triplo e Raiz Quadrada
# Raiz quadrada (outra forma) - pow(valor, (1/2)

valor = int(input('Digite um valor: '))
print('O dobro de {} é {}.'.format(valor, valor*2))
print('O triplo de {} é {}.'.format(valor, valor*3))
print('A raiz quadrada é {:.2f}.'.format(valor**(1/2)))
print('Outra forma de calcular a raiz quadrada {:.2f}.'.format(pow(valor,(1/2))))