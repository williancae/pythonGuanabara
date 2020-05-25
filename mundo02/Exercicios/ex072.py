indice = total = menor = cont = prodBarato = 0
while True:

    nomeProd = str(input('Nome Produto: '))
    preco = float(input('Qual o preço: '))
    total += preco
    if preco > 1000:
        cont += 1
    if indice == 0:
        menor = preco
    elif preco < menor:
        menor = preco
        prodBarato = nomeProd

    indice += 1
    continuar = str(input('Continuar [S/N]: ').strip().upper())
    print('\n')
    if continuar == 'N':
        break
print(f'Total {total}\n{cont} são mais caro que R$ 1000\nMais barato {prodBarato}')