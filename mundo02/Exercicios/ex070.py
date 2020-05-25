import random
acertos = erros = soma = media = 0

while True:

    num = int(input('\n______ Digite um numero: ').strip())
    op = str(input('Par ou impar [I/P]: ').upper().strip())
    pc = random.randint(0, 10)
    print(pc)
    soma = num + pc
    media = num % 2
    if media == 1 and op == 'I':
        print('Ganhou')
    else:
        print('Perdeu')
        break
