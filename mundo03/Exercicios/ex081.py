numero = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n)
    else:
        r = str(input(';quer continuar'))
    if r in 'Nn':
        break
print('-+'*30)
print(f'Voce digitou {numero.sort}')