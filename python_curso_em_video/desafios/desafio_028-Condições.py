advinha = int(input('Diga um número entre "0" e "5": '))
if advinha <= 5:
    print('Você disse {} e acertou. Parabéns!!!'.format(advinha))
else:
    print('Você errou. Tente outra vez.')
    