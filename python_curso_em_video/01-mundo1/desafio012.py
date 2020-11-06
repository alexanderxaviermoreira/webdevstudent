# Cálculo de área para pintura

largura = float(input('\n- Digite o vaor da Largura da parede: '))
altura = float(input('- Digite o valor da Altura da parede: '))
area = largura * altura
tintaNecessaria = area / 2

print('     => Largura: {} m'.format(largura))
print('     => Altura: {} m'.format(altura))
print('     => Área da parede: {:.2f} m²'.format(area))
print('- A quahtidade de tinta pára pintar essa área é: {:.2f} Litros'.format(tintaNecessaria))
