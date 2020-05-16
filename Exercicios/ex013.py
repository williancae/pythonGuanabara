'''
faça um algoritmo que leia o preço de um produto  e mostre seu novo preço, com de desconto
'''
preco = float(input('Digite o preço: '))
desconto = (preco * 5)/100
precoComDesconto = preco - desconto
print('O produto custa {} com desconto de 5% fica {:.2f}'.format(preco, precoComDesconto))