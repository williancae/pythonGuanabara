'''
    Crie um Programa que leia 2 valores, e faça um laço com, soma, multiplica, repetir e sair
'''
# Inicializando variaveis
somar = multiplicar = maior = repetir = op = 0
while op != 5:
    print('-'*5,' Operaçõs ','-'*5)
    op =int(input('[1] Somar\n'''
                  '[2] Multiplicar\n'
                  '[3] Maior\n'
                  '[4] Novos Valores\n'
                  '[5] Sair\n'
                  'Escolha umaa opção: '))

    if op == 1:
        num1 = int(input('Digite o numero: '))
        num2 = int(input('Digite outro valor: '))
        somar = num1 + num2
        print(f'A soma é {somar}')
    elif op == 2:
        multiplicar = num1 * num2
        print(f'O resultdado da multiplicação {multiplicar}')
    elif op == 3:
        num1 = int(input('Digite o numero: '))
        num2 = int(input('Digite outro valor: '))
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior é {maior}')
    elif op == 4:
        op = 0
    elif op == 5:
        op = 5

