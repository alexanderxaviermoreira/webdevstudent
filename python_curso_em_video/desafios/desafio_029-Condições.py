print('\n')
velocidade = float(input('O radar informou sua velocidade: '))
excesso = velocidade - 80
multaMinima = 7.00
if velocidade > 80:
    print('=> Você ultrapassou os 80 Km/h.')
    print('=> Sua multa será de R$ {:.2f}.\nSão R$ 7,00 (sete reais) por cada quilômetro excedido.'.format(excesso * multaMinima))
else:
    print('Sua velocidade registrada foi {} Km/h.\nBoa Viagem...'.format(velocidade))
