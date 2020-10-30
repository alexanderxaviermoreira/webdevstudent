cidade = str(input('Nome de cidade que inicia com SANTO: ')).replace(' ', '').lower()
iniciais = cidade[:5]
nomeCorreto = 'santo' in iniciais
print('\nInicia com SANTO: {}'.format(nomeCorreto))
