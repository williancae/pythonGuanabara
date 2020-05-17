'''
Programa que calcule o preço da viagem com 0.50 centavo para viagens de ate 200km
e acima 0.45 centavos
'''
dist = float(input('Sua viagem é de quantos Quilomentro: '))
if dist <= 200:
    preco = dist *  0.5
    print('O preço da Passagem é R$ {:.2f}'.format(preco))
else:
    preco = dist * 0.45
    print('O Preco da viagem é R$ {:.2f}'.format(preco))
