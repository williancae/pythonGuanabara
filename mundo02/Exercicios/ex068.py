num = flag = cont = soma = 0
while flag != 999:
    num = int(input('Digite um numero[999 para]: '))
    flag = num
    if flag != 999:
        soma += num
        cont += 1

print(f'soma: {soma}, Digitados: {cont}')