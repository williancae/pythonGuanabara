'''
Gere um numero aleatorio de 1 a 5 e tente adivinha caso acerte mostre na tela acertou, caso não errou
'''
import random
alea = random.randint(1,5)
# print(alea)
op = int(input('Escolha um numero de 1 a 5 e tente a sorte\nDigite: '))
if alea == op:
    print('Voce acertou!')
else:
    print('Voce errou!')
# Poderia ter implementado um laço de repetição para que não haja de ficar executando multiplas vezes
