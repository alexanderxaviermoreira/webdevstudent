# Seno, Cosseno e Tangente

import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))       # Necessário converter para radianos
cosseno = math.cos(math.radians(angulo))    # Necessário converter para radianos
tangente = math.tan(math.radians(angulo))   # Necessário converter para radianos
print('O Seno de {} é {:.2f}\n'
      'O Cosseno de {} é {:.2f}\n'
      'A Tangente de {} é {:.2f}'.format(angulo,seno,angulo,cosseno,angulo,tangente))