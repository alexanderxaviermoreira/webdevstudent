# if, elif e else

nome = str(input('Qual o seu nome? '))
if nome == 'Alexander':
    print('Você é o Papai!!!')
elif nome == 'Maria' or nome == 'Gabriela' or nome == 'Sofia':
    print('Vocẽ é meu parente!!')
elif nome in 'Helena Carminha':
    print('Você é a Vovó!!!')
else:
    print('Você não é meu parente!!!')
print('Tenha um bom dia, {}.'.format(nome))
