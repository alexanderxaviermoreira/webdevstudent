print('\n       =>      Até 200 Km: R$ 0,50 por Km;\n       =>      Acima de 200 Km: R$ 0,45 por Km.')
distancia = float(input('\nQual a distância percorrida na viagem? '))
print('Foi percorrido {} Km.'.format(distancia))
valor1 = 0.50
valor2 = 0.45
if distancia <= 200:
    print('Preço da passagem é R$ \033[4;35m{:.2f}\033[m \n'.format(
        valor1 * distancia))
else:
    print('Preço da passagem é R$ \033[4;35m{:.2f}\033[m \n'.format(
        valor2 * distancia))


# preco = distancia * 0.50 if distancia >= 200 else distancia * 0.45
# if inline ou operador ternário como no javascript
