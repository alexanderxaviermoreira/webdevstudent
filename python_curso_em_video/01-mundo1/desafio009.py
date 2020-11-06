# Converter de Metro para centímetros e milímetros

vM = float(input('Digite um valor: '))
vKm = vM / 1000
vHm = vM / 100
vDam = vM / 10
vDcm = vM * 10
vCm = vM * 100
vMm = vM * 1000
print('Convesão de medidas: {} m é igual a\n\n- {} Km\n- {} hm\n- {} dam\n- {} dcm\n- {} cm e \n- {} mm'.format(vM, vKm, vHm, vDam, vDcm, vCm, vMm))

