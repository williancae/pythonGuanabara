numeros = []
for n in range(0,5):
    numeros.append(int(input('Digite um numero: ')))
maior = menor = pma = pme = 0
print(numeros)
for i,n in enumerate(numeros):
    if i == 0:
        maior = n
        menor = n
    elif maior < n:
        maior = n
        pma = i
    elif menor > n:
        menor = n
        pme = i
print(f'O maior valor é {maior} e seu indice {pma}')
print(f'O menor valor é {menor} e seu indice {pme}')
# print(menor)

    

