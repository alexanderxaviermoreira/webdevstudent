# Reajuste Salarial

nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) # Acrescenta um número de caracteres
print('Prazer em te conhecer {:>20}!'.format(nome)) # Alinha a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) # Alinha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) # Alinha ao centro
print('Prazer em te conhecer {:=^20}!'.format(nome)) # Adicona o caractere no lugar dos espaços (=)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1 - n2
d = n1 / n2
di = n1 // n2
e = n1**n2
print('A soma é {}.\nA multiplicação é {}.\nA divisão é {:.3f}.\n'.format(s, m, d), end='')
# end='' - Manter prints na mesma linha
# {:.3f} - Limita o números de casas decimais (f = flutuante)
# \n - Quebra de linha
print('A divisão Inteira é {}.\nA potência é {}.'.format(di, e))



