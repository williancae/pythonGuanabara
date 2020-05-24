'''
Gere um numero aleatorio de 1 a 5 e tente adivinha caso acerte mostre na tela acertou, caso não errou
'''
import random
op = 0
stop = 0
alea = 0
cont = 0
while stop != 3:
    alea = random.randint(1, 10)
    # print(alea)
    op = int(input('Escolha um numero de 1 a 10 e tente a sorte\nDigite: '))
    if alea == op:
        print('-' * 10)
        print('Voce acertou!')
        stop = 3
        print('-' * 10)
    else:
        print('-'*10)
        print('Voce errou!')
        cont += 1
        print('-' * 10)
print('->>'*3,f'E errou {cont} vezes')
