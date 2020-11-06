nome = str(input('Digite um nome: ')).strip()
nomeSemEspaco = nome.split()
nomeComp = len(nomeSemEspaco)

print('Primeiro nome: {}'.format(nomeSemEspaco[0]))
print('Último nome: {}'.format(nomeSemEspaco[nomeComp - 1]))








