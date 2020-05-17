'''
Faça um Programa que leia um numero e retorna sua tabuada
'''
a = float(input('Digite um numero: '))
print('='*15)
for n in range(11):
    resultado = n * a
    print('{} x {} = {}'.format(n, a, resultado))
