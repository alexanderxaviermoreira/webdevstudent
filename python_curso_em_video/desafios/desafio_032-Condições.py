from datetime import date

print('\n Se "é" ou "não" ano BISSEXTO.\n')
ano = int(input('Digite um ano qualquer, com quatro digitos, our "0" para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('\n   =>  O ano de {} "é BISSEXTO":\n'.format(ano))
else:
    print('\n   =>  O ano de {} "não é BISSEXTO".\n'.format(ano))


# Regra do ano bissexto: múltiplo de 4, exceto multiplos "100" que não são multiplos de "400"
