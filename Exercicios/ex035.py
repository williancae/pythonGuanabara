'''
Receba 3 numeros e
'''
num1 = int(input('Digite um numero: '))
num2 = int(input('Mais um: '))
num3 = int(input('Mais outro: '))

maior = num3
if num1 > maior:
    maior = num1
if num2 > maior:
    maior = num2

menor = num2
if num1 < menor:
    menor = num1
if num3 < menor:
    menor = num3

print('O MAIOR numero é {}, e o MENOR {}!'.format(maior,menor))