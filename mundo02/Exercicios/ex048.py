'''
contagem regressiva 10 - 0, estouro de fogos
'''
import time

for cont in range(10, -1, -1):
    print(cont)
    time.sleep(1) # contagem regressiva em 1 e 1 segundo
print('Estouro de Fogos!')
