'''
Crie um Algoritmo que entre com um numero e mostre seu sucesso e antecessor
'''
a = int(input('Digite um numero: '))
ant = a-1
sus = a+1
print('O numero é {} seu sucessor é {} e antecessor {}'.format(a, sus, ant))