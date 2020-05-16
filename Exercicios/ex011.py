'''
Crie um programa que leia quanto dolares a pessoa consegue comprar com a quantia de dinheiro posta
U$ 1,0 --> R$ 3,27
'''
a = float(input('Quanto você tem: '))
conversao = a/3.27
print('Com R$ {} voce comprar U$ {:.2f}'.format(a, conversao))
