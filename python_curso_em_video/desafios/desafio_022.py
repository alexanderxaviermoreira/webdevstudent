nome = 'Alexander Xavier Moreira'
print('\n => ', nome)

print('\nEm maiúsculas: {}'.format(nome.upper()))
print('Em minúscuslas: {}'.format(nome.lower()))
print(' => Número de caracteres: {}'.format(len(nome)))

novoNome = nome.replace(' ', '')
print('Número de caracteres, sem espaços: {}'.format(len(novoNome)))

nomeDividido = nome.split(' ', 2)
print(' => Primeiro nome: {}'.format(nomeDividido[0]))
print('Número de caracteres, do primeiro nome: {}'.format(len(nomeDividido[0])))
