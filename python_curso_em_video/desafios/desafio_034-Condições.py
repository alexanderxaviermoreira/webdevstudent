salario = float(input('\n Qual o seu salário: '))
novoSalario = 0
if salario > 1250:
    novoSalario = salario + ((salario * 10) / 100)
    print('\n   =>      Seu novo salario é: R$ \033[4;30;43m {:.2f} \033[m \n'.format(novoSalario))
else:
    novoSalario = salario + ((salario * 15) / 100)
    print('\n   =>      Seu novo salario é: R$ \033[4;30;43m {:.2f} \033[m \n'.format(
        novoSalario))


