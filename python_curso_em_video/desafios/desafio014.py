# Percentual de aumento salarial

salario = float(input('\nSalário do funcionário: R$ '))
reajuste = float(input('Percentual de reajuste: '))
salarioReajustado = ((salario / 100) * reajuste) + salario
print('O novo salário é R$ {:.2f}'.format(salarioReajustado))