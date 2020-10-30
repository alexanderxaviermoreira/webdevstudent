nome = str(input('Qual o seu nome: '))
if nome == 'Alexander':
    print('Que nome lindo você tem!')
    print('Bom dia {}'.format(nome))
else:
    print('Que nome feio você tem, {}!'.format(nome))
    print('Bom dia seu Feio. KKKKK')

print('\n')

nota1 = float(input('Digite um nota: '))
nota2 = float(input('Digite outra nota: '))
media = (nota1 + nota2) / 2
print('Sua média foi {}'.format(media))
if media < 5:
    print('Você foi Reprovado!')
else:
    print('Você foi Aprovado!')