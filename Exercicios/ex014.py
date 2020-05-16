'''
Faça um algoritmo que leia o salario de um fuuncionario e  mostra seu novo salario, com 15% de aumento
'''
salario = float(input('Quanto você recebe: '))
aumento = (salario * 15)/100
salarioComAumento = salario + aumento
print('Você recebeu um aumento e seu novo salario é {:.2f}'.format(salarioComAumento))
