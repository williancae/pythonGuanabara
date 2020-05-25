'''
Multiplas tabuadas para quando valor digitado for negativo
'''
num = result = cont = rod = 0

while True:
    cont += 1
    print('\33[31mTabuada \33[m')
    num = int(input('Digite um valor: '))
    print('->>-' * 3)
    if num < 0:
        print('Voce saiu do programa')
        break
    for r in range(1, 11):
        result = num * r
        print(f'{r} x {num} = {result}')
    print('->>-'*3)