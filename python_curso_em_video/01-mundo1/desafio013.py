# Calcular desconto de um produto

valorProduto = float(input('\n=> Qual o valor do produto? R$ '))
percentualDesconto = float(input('=> Qual o percentual de desconto? '))

valorDesconto = (valorProduto/100)*percentualDesconto
valorComDesconto = valorProduto - valorDesconto
print('=> O valor do produto: R$ {:.2f}'.format(valorProduto))
print('=> Percentual de desconto: {}%'.format(percentualDesconto))
print('=> Valor do produto com o desconto é: R$ {:.2f} '.format(valorComDesconto))