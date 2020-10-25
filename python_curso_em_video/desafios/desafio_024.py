cidade = input(str('Nome de cidade que inicia com SANTO: '))
iniciais = cidade[:6]
print(iniciais)
nomeCorreto = 'Santo' in iniciais
print('Inicia com SANTO: {}'.format(nomeCorreto))
