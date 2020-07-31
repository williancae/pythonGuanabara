l1 = []
l2 = []
for x in range(0,7):
    y = int(input('Digite um numero: '))
    if y % 2 == 0:
        l1.append(y)
    else:
        l2.append(y)
l1.sort()
l2.sort()
print(f'Pares: {l1}') #Pares
print(f'Impares: {l2}') #Impares       