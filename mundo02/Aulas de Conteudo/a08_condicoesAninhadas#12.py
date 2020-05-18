'''
Teorioa
condição simplificada
tempo = int(input())
print('Carro novo: 'if tempo<=3 else 'Carro velho')
'''
# tarefa 1
nome = str(input('Qual seu nome:')).strip()
if nome == 'Willian':
    print('Nome Legal ')
elif nome == 'Pedro' or nome == 'Matheus' or nome == 'João' or nome ==  'Felipe' or nome == 'Maria':
    print('Seu nome é bem popular!')
elif nome in 'Ana Anna Geovana Raquel Rosa':
    print('Belo nome feminino')
else:
    print('Seu nome é tão normal!')
print('Bom Dia {}'.format(nome))

# tarefa 2
# n1 = float(input('nota 1: '))
# n2 = float(input('nota 2: '))
# n = (n1+n2)/2
# if n >= 6:
#     print('Sua nota foi Boa! ')
# else:
#     print('A sua media é ruim!')
# #       ===========
# #       É o mesmo que:
# #       ===========
# print('Sua nota foia boa'if n>=6 else 'Sua nota é ruim')