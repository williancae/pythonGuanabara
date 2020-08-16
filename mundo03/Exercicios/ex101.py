from random import randint
from time import sleep
def sorteia(lista):
    print('Numeros sorteados: ', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('>>Pronto!!')
def soma(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    sleep(0.5)
    print(f'A soma dos pares é {soma}')
numero = []
sorteia(numero)
soma(numero)