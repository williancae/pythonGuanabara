from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'Andre': randint(1,6),
    'Lucas': randint(1,6),
    'Pedro': randint(1,6),
    'Joao': randint(1,6)}
# print(jogo)
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('RANKING')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} tirou {v[1]}')
    sleep(1)