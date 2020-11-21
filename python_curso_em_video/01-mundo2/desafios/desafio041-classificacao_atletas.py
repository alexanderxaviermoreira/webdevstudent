''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM / - Até 14 anos: INFANTIL / - Até 19 anos: JÚNIOR / - Até 20 anos: SÊNIOR / - Acima: MAASTER
'''

from datetime import date

nomeNadador = str(input('\nQual o seu nome? '))
anoNasc = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - anoNasc

if idade <= 9:
    print('Olá {}, você tem {} anos.\nSua categoria é \033[4;31mMIRIM\033[m.'.format(nomeNadador, idade))
elif idade >= 10 and idade <= 14:
    print('Olá {}, você tem {} anos.\nSua categoria é \033[4;31mINFANTIL\033[m.'.format(nomeNadador, idade))
elif idade > 14 and idade <= 19:
    print('Olá {}, você tem {} anos.\nSua categoria é \033[4;31mJÚNIOR\033[m.'.format(nomeNadador, idade))
elif idade > 19 and idade <= 25:
    print('Olá {}, você tem {} anos.\nSua categoria é \033[4;31mSÊNIOR\033[m.'.format(nomeNadador, idade))
elif idade > 25:
    print('Olá {}, você tem {} anos.\nSua categoria é \033[4;31mMASTER\033[m.'.format(nomeNadador, idade))








