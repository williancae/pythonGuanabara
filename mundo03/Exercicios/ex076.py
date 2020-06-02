'''
Crie cinco numeros aleatorios e coloque dentro de uma tupla e mostre  o maior e o menor
'''
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')