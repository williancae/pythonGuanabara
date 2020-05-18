'''
Receber 3 valores e verificar se é possivel formar triangulo, e qual tipo equilatero, isoceles e escalenos
'''
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b

a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if ((b - c)< a < (b + c)) & ((a - c) < b < (a + c)) & ((a - b) < c < (a + b)):
    if b == c and b == a:
        print('Equilatero')
    elif (c != a != b) and (b != c):
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não é um triangulo')