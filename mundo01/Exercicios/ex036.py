'''
salarios superiores a 1250 aumento de 10%
inferiores ou igual 15%
'''
salario = float(input('Digite o Salarios: '))
if salario > 1250:
    salario += (salario*10)/100
else:
    salario += (salario*15)/100
print('Seu novo Salario é {}'.format(salario))
