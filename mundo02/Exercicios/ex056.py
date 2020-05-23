menor = 0
maior = 0
for c in range(0,7):
    idade = int(input('Digite idade: '))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} Menores de 21 e {} Maiores de 21'.format(menor,maior))
