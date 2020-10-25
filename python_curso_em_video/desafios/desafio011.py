# Conversão para dólar, ou outra moeda

real = float(input('Quantos reais você tem na carteira? R$ '))
dolarHoje = float(input('Qual o valor do dolar hoje? '))
realDolar = real/dolarHoje
print('Tenho R$ {:.2f}.'.format(real))
print('Em dólares são: US$ {:.2f}.'.format(realDolar))