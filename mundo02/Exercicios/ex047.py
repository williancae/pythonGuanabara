'''
Crie um pedra papel e tesoura
'''
import random
print('======= Vamos Brincar =========')
print('Para participar da brincadeira é nescessario que voce escolha uma opção'
      '\n[1] - Tesoura'
      '\n[2] - Papel'
      '\n[3] - Pedra')
op = int(input('Escolha uma das opções: '))
comp = random.randint(1,3)

if op == comp:
    print('empate')
elif (op == 1) == (comp == 2):
    print('Computador ganhou')

elif (op == 2) == (comp == 1):

    print('Voce Ganhou')
elif (op == 2) == (comp == 3):
    print('Computador ganhou')

elif (op == 3) == (comp == 2):
    print('Voce ganhou')

elif (op == 1) == (comp == 3):
    print('Computador Ganhou')

elif (op == 3) == (comp == 1):
    print('Voce ganhou')
