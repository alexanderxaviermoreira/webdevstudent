'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:     - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. / - Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
'''

from datetime import date

anoNasc = int(input('\nQual o seu ano de nascimento? '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 18:
    print('\nVocê tem \033[1;31;40m{}\033[m anos e ainda fará seu alistamento.'.format(idade))
    print('\nAinda falta(m) \033[1;31;40m{}\033[m ano(s) para seu alistamento.'.format(18-idade))
elif idade == 18:
    print('\nVocê tem \033[1;31;40m{}\033[m anos. Está na hora do seu alistamento.'.format(idade))
else:
    print('\nVocê tem \033[1;31;40m{}\033[m anos. Já passou do prazo de alistamento.'.format(idade))
    print('\nVocê ultrapassou o prazo de alistamento em \033[1;31;40m{}\033[m ano(s).'.format(idade - 18))
