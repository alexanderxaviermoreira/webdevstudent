''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status de acordo com a tabela abaixo:     - Abaixo de 18.5: Abaixo do Peso - Entre 18.5 e 25: Peso Ideal - De 25 a 30: Sobrepeso = De 30 a 40: Obesidade - Acima de 40: Obesidade Mórbida '''

from math import pow
nome = str(input('\nInforme seu nome: '))
peso = float(input('Informe seu peso (Ex: 82): '))
altura = float(input('Informe sua altura (Ex: 1.77): '))
imc = peso/pow(altura, 2)
# imc = peso / (altura ** 2) => Sem importar biblioteca
print('Seu IMC: {:.2f}'.format(imc))

if imc < 18.5:
    print('{}, você está \033[31;40mAbaixo do Peso\033[m.'.format(nome))
elif imc >= 18.5 and imc < 25:
    print('{}, você está com \033[31;40mPeso Ideal\033[m.'.format(nome))
elif imc >= 25 and imc < 30:
    print('{}, você está com \033[31;40mSobrepeso\033[m.'.format(nome))
elif imc >= 30 and imc <= 40:
    print('{}, você está com \033[31;40mObesidade\033[m.'.format(nome))
elif imc >= 40:
    print('{}, você está com \033[31;40mObesidade Mórbida\033[m.'.format(nome))

print('''\n- Abaixo de 18.5: Abaixo do Peso\n- Entre 18.5 e 25: Peso Ideal\n- De 25 a 30: Sobrepeso\n- De 30 a 40: Obesidade\n- Acima de 40: Obesidade Mórbida''')
