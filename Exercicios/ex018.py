'''
Mostrar parte inteira de um numero de ponto flutuante
'''
import math
num = float(input('Digite numero: '))
print('O numero é {:}'.format(math.trunc(num)))
# math.trunc --> Pega parte inteira do numero