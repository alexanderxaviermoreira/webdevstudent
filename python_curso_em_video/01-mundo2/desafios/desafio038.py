'''Escreva um prgrama que leia dois números inteiros
e compare-os, mostrando na tela umam mensagem:

- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais'''

nOne = int(input('\nDigite um número: '))
ntwo = int(input('Digite outro número: '))

if nOne > ntwo:
    print('\nO primeiro valor é o maior')
elif ntwo > nOne:
    print('\n O segundo valor é o maior.')
else:
    print('\n{} e {} são iguais.'.format(nOne, ntwo))
