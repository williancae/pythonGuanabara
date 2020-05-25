'''
Ler varios valores dá media, maior, menor e opção de continuar ou parar
'''
soma = media = maior = menor = cont = 0
op = ''
while op != 'N':
    num = int(input('Digite um numero: '))
    op = str(input('Quer Continuar [S/N]: ').strip().upper())
    # print(op)
    soma += num
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    cont += 1
media = soma / cont
print(f'A media entre os Valores são {media:.2f}\nForam digitados {cont} vezes\nMaior {maior}\nMenor {menor}')