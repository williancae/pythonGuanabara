matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = menor = scol = l = c = spar = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para matriz: [{l}][{c}] -> '))
print('-*'*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print('')
print('-*'*20)
print(f'A soma dos pares é {spar}')
for x in range(0,3):
    scol += matriz[x][2]
print(f'A soma da coluna 3 é : {scol}')
for x in range(0,3):
    if x == 0:
        maior = matriz[1][x]
    elif  maior < matriz[1][x]:
        maior = matriz[1][x]
print(f'O Maior é {maior}')