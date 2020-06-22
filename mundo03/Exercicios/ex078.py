tupla = ('Leite', 4, 'Nescau', 5.6, 'Pão', 4.6, 'Manteiga', 5.6, 'Margarina', 6, 'Café', 4.6)

''' print(f': {tupla[0]:.<22} R$ {tupla[1]:.2f} :')
print(f': {tupla[2]:.<22} R$ {tupla[3]:.2f} :')
print(f': {tupla[4]:.<22} R$ {tupla[5]:.2f} :')
print(f': {tupla[6]:.<22} R$ {tupla[7]:.2f} :')
print(f': {tupla[8]:.<22} R$ {tupla[9]:.2f} :')
print(f': {tupla[10]:.<22} R$ {tupla[11]:.2f} :') '''

# Utilizando Laços
print('-'*40)
print('{:^30}'.format('Listagem'))
print('-'*40)
for x in range(0, len(tupla)):
    if x % 2 == 0:
        print(f':{tupla[x]:.<30}', end="")
    else:
        print(f'R$ {tupla[x]:>5.2f}:')
print('-'*40)