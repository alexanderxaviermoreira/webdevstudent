nome = str(input('Digite seu nome completo: '))
print('\n => ', nome)

print('\n => Em maiúsculas: {}'.format(nome.upper()))
print(' => Em minúscuslas: {}'.format(nome.lower()))
print(' => Número de caracteres, sem espaços: {}'.format(len(nome) - nome.count(' ')))

novoNome = nome.replace(' ', '')
print(' => Número de caracteres, sem espaços: {}'.format(len(novoNome)))

nomeDividido = nome.split()
print(' => Primeiro nome: {}'.format(nomeDividido[0]))
print(' => Número de caracteres, do primeiro nome: {}'.format(len(nomeDividido[0])))

print(' => Resposta do Prof: {}'.format(nome.find(' ')))
