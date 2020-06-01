'''
    Tuplas
    1- Dividido em indices
    2- Mostrar na tela print(lanche[2]) -> posição 2 da tupla
    3- Tuplas são imputaveis
'''
# Pratica de Aula
lanche = ('Hamburger','Suco','Pizza','Pudim') # tuplas utilizão parenteses
print(lanche)
print(lanche[0])
print(lanche[:2])
print(lanche[2:])
print(lanche[1:3])
print(lanche[:-2])
print(lanche[::-1])
for alimento in lanche:
    print(alimento, end=' ')
print('\n\n')
for alimento in range(0, len(lanche)):
    print(lanche[alimento])
print('\n')

#----------- Enumerate -------- Enumera a tupla
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#---------Sorted-------- Colocar em Ordem
print(sorted(lanche))

a = (1,2,5,2,4,)
b = (0,1,0,3,1,1)
c = a + b
print(c)

