#  Aula de Modulos
'''
Teorica
1 - Adicionar funcionalidades;
2 - 'import' utilizado para chamar modulos/ bibliotecas;
3 - 'from' Modulo/biblioteca 'import' funcionalidade desejada;
'''

# Atividades
import math # importa todas as funções da math
# from math import sqrt, floor, ceil  --> definir as funções que sera utilizada para importar
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.3f}'.format(num,raiz))
# math.floor(raiz)  --> arrendonda pra baixo
# math.ceil(raiz) --> arredonda pra cima

import random
# import emoji
num = random.randint(1, 10)
# random.randint(x,y) --> definir intevalo de numeros que serao gerador de formas aleatorias
print('Numero aleatorio: ',num)
# print(emoji.emojize('Mostra emoji: :earth_americas:', use_aliases=True))