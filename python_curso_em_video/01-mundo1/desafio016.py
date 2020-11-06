# Aluguel de carro - kilometragem e conbustível

print('\nAluguel de carro\n')

valorDia = 60
Kmvalor = 0.15
diasAlugados = int(input('\nDias alugados: '))
km = float(input('Quilometragem rodada: '))
aPagar = (valorDia * diasAlugados) + (Kmvalor * km)
print('Valor do aluguel ficou por: R$ {:.2f}\n'.format(aPagar))