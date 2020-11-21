'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão - 1 para binário - 2 para octal - 3 para hexadecimal
'''

import math

numero = int(input('\nDigite um número inteiro: '))
bases = int(input('\nOPÇÕES:\n => Digite "1" para binário\n => Digite "2" para octal ou\n => Digite "3" para hexadecimal: \n    => '))
binario = 1
octal = 2
hexadecimal = 3

if bases == binario:
    print('\nConvertido {} para \033[30;41mbinário\033[m =>  {}'.format(numero, bin(numero)[2:]))
elif bases == octal:
    print('\nConvertido {} para \033[30;41moctal\033[m =>  {}'.format(numero, oct(numero)[2:]))
elif bases == hexadecimal:
    print('\nConvertido {} para \033[30;41mhexadecomal\033[m => {}'.format(numero, hex(numero)[2:]))
else:
    print('\nValor incorreto.')