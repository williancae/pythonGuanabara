num = (int(input('1ª numero: ')), int(input('2ª numero: ')), int(input('3ª numero: ')), int(input('4ª numero: ')))
print(f'Numeros Digitados {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 aparceu na {num.index(3)+1}ª posição')
else:
    print('O numero 3 nao foi digitado')
print('Os valores pares são ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
