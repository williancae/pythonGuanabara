<<<<<<< HEAD
# exercicicio 1018 - Cédulas  URI
# valor = int(input())
# print(valor)
# notas = [100,50,20,10,5,2,1]
#
# for nota in notas:
#     quantidadeNotas = int(valor/nota)
#     print("{} nota(s) de R$ {},00".format(quantidadeNotas,nota))
#     valor -= quantidadeNotas * nota
#criar um painel de saque sem ultilizar lista


valor = int(input('Digite um valor de saque: '))
=======
"""
EXERCÍCIO 071: Simulador de Caixa Eletrônico
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
"""
print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
>>>>>>> 13a70f29656d05bf854326a760349c53af5cd1ae
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')