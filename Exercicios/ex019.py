'''
Programa que leia o comprimento do cateto oposto e o adjacente de um triangulo e mostre o comprimento da Hipotenusa
'''
# h²=ca² + cp²
import math
ca = float(input('Digite cateto Adjacente: '))
cp = float(input('Digite cateto Oposto: '))
h = math.hypot(ca,cp) #calcular Hipotenusa
print('A Hipotenusa é {:.2f}'.format(h))
