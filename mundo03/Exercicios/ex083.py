lista = []
cont = 0
# lista.sort(reverse=True)
# print(lista)
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        cont += 1
    else:
        print('Valor duplicado')
    s = str(input('Deseja continuar [S/N]: '))
    if s in 'Nn':
        break
print('\n'+'-='*15)
lista.sort(reverse=True)
print(f'Voce inseriu {cont} elementos')
print(f'Ordenado em descrescente {lista}.')
if 5 in lista:
    print('Existe o valor 5')
else:
    print('Não possui o valor 5')