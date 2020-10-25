# Exibir a parte inteira do número real

import math
num = float(input('Digite um número real: '))
res = math.floor(num)
res1 = math.trunc(num)
print('Porção inteira de {}, usando floor é {}'.format(num, res))
print('Porçao inteira de {}, usando trunc é {}'.format(num, res1))
