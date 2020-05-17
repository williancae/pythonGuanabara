'''
Digite o nome de 4 alunos depois faça um sorteio entre eles
'''
import random
a1 = input('Digite o nome aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1,a2,a3,a4]
print('O aluno {} gannhou o sorteio!'.format(random.choice(lista)))
# random.choice() --> traz um  valo aleatorio da lista