aux = a = 0
b = 1
n = int(input('Digite um Numero: '))
i = 0
print('1 >> ',end='')
while i != n:
    aux = a + b;
    a = b;
    b = aux;
    i += 1
    print(f'{aux} >> ',end='')
