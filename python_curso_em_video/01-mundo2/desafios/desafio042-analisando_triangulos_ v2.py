'''Rfazendo a verificação da possibilidade ser criado um trinângulo com as medidas de retas informadas, yambém diga que tipo de triângulo seria possível'''

from time import sleep

print('\n Insira os comprimentos dos lados de um triângulo: ')
r1 = float(input('\nReta Um: '))
r2 = float(input('Reta Dois: '))
r3 = float(input('Reta Três: '))

condicao = r1 > abs(r2 - r3) and r1 < (r2 + r3) and r2 > abs(r1 - r3) and r2 < (r1 + r3)and r3 > abs(r1 - r2) and r3 < (r1 + r2)

print('\n Analisando... \n')
sleep(2)

if condicao == True and r1 == r2 == r3:
    print('\n\033[30;41mO triãngulo é possível. \033[m\nÉ um Triângulo Equilátero.')
elif condicao == True and r1==r2 or r1==r3 or r2==r3:
    print('\n\033[30;41mO triãngulo é possível. \033[m\nÉ um Triângulo Isósceles.')
elif condicao == True and r1 != r2 and r1 != r3 and r2 != r3:
    print('\n\033[30;41mO triãngulo é possível. \033[m\nÉ um Triângulo Escaleno.')
else:
    print('\n\033[30;42m O triângulo nao é possível.\033[m \n')
