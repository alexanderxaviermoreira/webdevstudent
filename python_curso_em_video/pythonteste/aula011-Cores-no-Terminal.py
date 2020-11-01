print('''
Cores no terminal
ANSI - Scape Sequence

     style;     text;       background
\033[0;         33;         44m

style                   text                background
0 - none                30 - branco         40 - branco 
1 - bold                31 - vermelho       41 - vermelho 
4 - underline           32 - verde          42 - verde 
7 - negative            33 - amarelo        43 - amarelo 
                        34 - azul           44 - azul 
                        35 - magenta        45 - magenta 
                        36 - ciano          46 - ciano 
                        37 - cinza          47 - cinza
''')


print('\033[0;30;41m Trocando as cores \33[m')
print('\033[4;33;44m Trocando as cores \33[m')
print('\033[1;35;43m Trocando as cores \33[m')
print('\033[30;42m Trocando as cores \33[m')
print('\033[m Trocando as cores \33[m')
print('\033[7;30m Trocando as cores \33[m')


print('\nEXERCÍCIO:\n')

print('\033[31m Olá, Mundo!\33[m \n')
print('\33[1;31;43m Olá, Mundo!\33[m \n')
print('\033[4;30;45m Olá, Mundo! \33[m \n')
print('\33[7;30m Olá, Mundo \33[m \n')
print('\33[7;33;44m Olá, Mundo \33[m \n')


a = 5
b = 8
print('Os valores das letras são \33[1;33m {} \33[m e \33[1;31m {} \33[m !!!\n\n'.format(a, b))

nome = 'Alexander'
sobrenome = 'Moreira'
print('Muito prazer {}{}{} {}{}{} !!!'.format('\33[1;31m', nome, '\33[m', '\33[1;34;43m', sobrenome, '\33[m'))

