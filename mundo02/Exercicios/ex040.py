a = int(input('Digite um numero: '))
b = int(input('Outro numero: '))

if a > b:
    print('O numero {} é o maior'.format(a))
elif a == b:
    print('Não exite valor maior, os dois são iguais.')
else:
    print('O numero {} é o maior'.format(b))