'''
Mostrar pregreção aritmetica
'''
n = int(input('Digite numero: '))
r = int(input('Razão: '))
for x in range(n, (n + (10 - 1) * r) + r, r):
    print(x, end=' >> ')
print('Fim')

#Ou

n = int(input('Digite numero: '))
r = int(input('Razão: '))
t = (n + (10 - 1) * r) + r
x = 0
while x != t:
    x += r
    print(x, end=' >> ')
print('Fim')
