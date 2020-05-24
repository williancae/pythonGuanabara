'''
leia um numero e mostre seu fatorial
'''
num = int(input('Digite um numero pra saber o fatorial: '))
fat = 0
for c in range(num - 1, 0, -1):
    num = num * c
print(f'O  fatorial é {num}')

# Ou
c = num
while c != 1:
    c -= 1
    num = num * c
    print(c)
print(f'O  fatorial é {num}')