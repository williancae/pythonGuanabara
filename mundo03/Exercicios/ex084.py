num = []
par = []
impar = []
while True:
    num.append(int(input('Digite o valor: ')))
    res = str(input('Quer continuar [S/N]: '))
    if res in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('='*20)
print(f'Os numeros são {num}')
print(f'Os pares são {par}')
print(f'Os impares são {impar}')