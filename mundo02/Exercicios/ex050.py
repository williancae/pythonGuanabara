'''
soma de todos os numeros impares multiplos 3, entre 1 de 500
'''
s = 0 #somatoria
for c in range(1, 501):
    if c%2 == 1:
        if c%3 == 0:
            s += c
print('A somatoria é',s)