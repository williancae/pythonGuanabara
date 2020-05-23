n = int(input('Digite um numero: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont +=1
        print('\033[31m{}'.format(c),end=' ')
    else:
        print('\033[33m{}'.format(c),end=' ')
print('\n\033[mO numero \033[33m{}\033[m foi divisivel \033[33m{}\033[m vezes'.format(n, cont))
if cont == 2:
    print('É primo')
else:
    print('Não é primo')

