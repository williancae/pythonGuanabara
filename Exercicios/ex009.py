'''
Escreva um Programa que leia um valor em metro e exiba em centimetro e milimetros
'''
a = float(input('Digite um valor: '))
b = a*100
c = b*100
print('Metros {:>10}'.format(a))
print('Centimetros {:>7}'.format(b))
print('Milimetros {:>6}'.format(c))