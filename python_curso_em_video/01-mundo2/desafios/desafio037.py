'''Escreva um programa que leia um número
inteiro qualquer e peça para o usuário
escolher qual será a base de conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

import math

numero = int(input('\nDigite um número inteiro: '))
bases = int(input('\nOPÇÕES:\n => 1 para binaŕio\n => 2 para octal e\n => 3 para hexadecimal: \n => '))
binario = 1
octal = 2
hexadecimal = 3

if bases == binario:
    print('\nConvertido {} para \033[30;41mbinário\033[m =>  {}'.format(numero, bin(numero)))
elif bases == octal:
    print('\nConvertido {} para \033[30;41moctal\033[m =>  {}'.format(numero, oct(numero)))
elif bases == hexadecimal:
    print('\nConvertido {} para \033[30;41mhexadecomal\033[m => {}'.format(numero, hex(numero)))
else:
    print('\nValor incorreto.')