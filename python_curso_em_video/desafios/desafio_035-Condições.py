from time import sleep

print('\n Insira os comprimentos dos lados de um triângulo: ')
r1 = float(input('\nReta Um: '))
r2 = float(input('Reta Dois: '))
r3 = float(input('Reta Três: '))
#condicao01 = r1 > abs(r2 - r3) and r1 < (r2 + r3)
#condicao02 = r2 > abs(r1 - r3) and r2 < (r1 + r3)
#condicao03 = r3 > abs(r1 - r2) and r3 < (r1 + r2)

condicao = r1 > abs(r2 - r3) and r1 < (r2 + r3) and r2 > abs(r1 - r3) and r2 < (r1 + r3)and r3 > abs(r1 - r2) and r3 < (r1 + r2)

# condicao1 = r1 < r2+r3 and r2 < r1+r3 and r3 = r1+r2

print('\n Analisando... \n')
sleep(2)

if condicao == True:
    print('\n \033[30;41m O triãngulo é possível. \033[m \n')
else:
    print('\n \033[30;42m O triângulo nao é possível.\033[m \n')
