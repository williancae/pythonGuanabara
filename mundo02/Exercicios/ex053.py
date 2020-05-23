'''
Mostrar pregreção aritmetica
'''
n = int(input('Digite numero: '))
r = int(input('Razão: '))
for x in range(n, (n + (10 - 1) * r) + r, r):
    print(x, end=' >> ')
print('Fim')

