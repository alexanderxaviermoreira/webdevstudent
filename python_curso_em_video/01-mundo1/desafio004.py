valor = input('Digite algo: ')
print('O tipo primitivo é ', type(valor))
print('Só tem espaços ', valor.isspace())
print('Se é numerico: ', valor.isnumeric())
print('Se é alfabetico: ', valor.isalpha())
print('Se é alfanumérico: ', valor.isalnum())
print('Se é maiúsculo: ', valor.isupper())
print('se é minúsculo: ', valor.islower())
print('Se é decimal: ', valor.isdecimal())
print('Se é capitalize ', valor.istitle())