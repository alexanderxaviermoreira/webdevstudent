# Cálculo da hipotenusa

import math
cOposto = float(input('Digite o comprimento do cateto oposto: '))
cAdacente = float(input('Digite o comprimento do cateto adjacente: '))
hipo = math.sqrt(math.pow(cAdacente, 2) + math.pow(cOposto, 2))
print('O comprimento da hipotenusa é {:.2f}'.format(hipo))
