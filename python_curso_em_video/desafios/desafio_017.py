''' Cálculo da hipotenusa
 Podendo ser feito sem múdulo math
       => (co**2 + ca **2) ** (1/2) '''
import math
cO = float(input('Digite o comprimento do cateto oposto: '))
cA = float(input('Digite o comprimento do cateto adjacente: '))
hipo = math.sqrt(math.pow(cA, 2) + math.pow(cO, 2))
hipo1 = math.hypot(cA, cO)
print('O comprimento da hipotenusa é {:.2f}'.format(hipo))
print('O comprimento da hipotenusa, usando hypot é {:.2f}'.format(hipo1))
