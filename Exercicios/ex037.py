'''
Receber 3 valores e verificar se é possivel formar triangulo
'''
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if ((b - c)< a < (b + c)) & ((a - c) < b < (a + c)) & ((a - b) < c < (a + b)):
    print('É um triangulo!')
else:
    print('Não é um triangulo')