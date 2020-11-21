'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida: - Media abaixo de 5.0: REPROVADO / - Média entre 5.0 e 6.9: RECUPERAÇÃO / - Média 7.0 ou superior: APROVADO
'''

aluno = str(input('\nQual o seu nome? '))
nota01 = float(input('Insira a primeira nota: '))
nota02 = float(input('Insira a segunda nota: '))
media = (nota01 + nota02) / 2
print('     =>Primeira Nota:', nota01)
print('     =>Segunda Nota: ', nota02)
print('     =>Média:', media)

if media < 5.00:
    print('{}, sua Média foi \033[30;41m{:.2f}\033[m.\nVocê foi \033[30;41m REPROVADO \033[m'.format(aluno, media))
elif media >= 5.00 and media <= 6.99:
    print('{}, sua média foi \033[30;44m{:.2f}\033[m.\nVocê está em \033[30;44m RECUPERAÇÃO \033[m'.format(aluno, media))
elif media >= 7.00:
    print('{}, sua média foi \033[30;43m{:.2f}\033[m.\nVocê está \033[30;43m APROVADO \033[m.'.format(aluno, media))
else:
    print('Vamos verificar suas notas.')