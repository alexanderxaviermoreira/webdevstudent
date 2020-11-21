''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:     - à vista em dinheiro ou cheque: 10% de desconto - à vista no cartão: 5% de desconto - em até 2x no cartão: preço normal - 3x no cartão: 20% de juros
'''

print('\n')
print('#'*10, ' LOJÃO TIO ALEKA ', '#'*10)
valorProduto = float(input('\nValor da compra: R$ '))
print('''
    [ 1 ] - À vista (dinheiro ou cheque) c/ 10% de desconto
    [ 2 ] - À vista (no cartão) c/ 5% de desconto
    [ 3 ] - 2x no cartão (preço normal) 
    [ 4 ] - 3x ou mais no cartão (20% de juros) 
''')
c1 = valorProduto - ((valorProduto / 100) * 10)
c2 = valorProduto - ((valorProduto / 100) * 5)
c3 = valorProduto
c4 = valorProduto + ((valorProduto / 100) * 20)
condicao = int(input(('Escolha a condição: ')))

if condicao == 1:
    print('Valor final: R$ {:.2f}'.format(c1))
elif condicao == 2:
    print('Valor final: R$ {:.2f}'.format(c2))
elif condicao == 3:
    print('Valor final: R$ {:.2f}, com parcelas de R$ {:.2f}'.format(c3, c3/2))
elif condicao == 4:
    nParcelas = int(input('Número de parcelas: '))
    print('Valor final: R$ {:.2f}, com parcelas de R$ {:.2f}'.format(c4, c4 / nParcelas))
else:
    print('Informação incorreta')
