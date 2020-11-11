print('''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
- O programa vai perguntar:
1 - o valor da casa,
2 - o salário do comprador e
3 - em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
''')

valorCasa = float(input('\nQual o valor do imóvel: '))
salario = float(input('Qual o seu salário? '))
salario30 = (salario/100)*30
numeroDeAnos = int(input('Quantos anos para pagar o imóvel? '))
valorDaPrestacao = (valorCasa / numeroDeAnos) / 12
if(valorDaPrestacao < salario30):
    print('\033[1;30;43m Empréstino APROVADO. \033[m \n => O valor da prestação será R$ {:.2f}.\nO valor não ultrapassou 30% (\033[7;31;40mR$ {:.2f}\033[m) do salario.'.format(valorDaPrestacao, salario30))
else:
    print('\n \033[1;30;41m O empréstimo foi recusado.\033[m')
    print(' => O valor da prestação será R$ {:.2f}.\nUltrapassou 30% (\033[7;31;40mR$ {:.2f}\033[m) do salario.'.format(valorDaPrestacao, salario30))
    print('\n => Valor do Imóvel: R$ {:.2f}'.format(valorCasa))
    print(' => Salário: R$ {:.2f}'.format(salario))
    print(' => Qtde de Anos para pagar: {}'.format(numeroDeAnos))
    