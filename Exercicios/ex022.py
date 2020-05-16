from random import shuffle

a1 = input('Digite o nome aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1,a2,a3,a4]
shuffle(lista) # Embaralhar lista
print('A ordem é: ordem = {}'.format(lista))