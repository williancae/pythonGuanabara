'''
Escreva um programa que lleia a velocidade de um carro
1- se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado multiplicando cada quilometro acima por R$ 7,00
'''
velocidade = float(input('Digite a sua velocidade atual: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Voce foi multado! o valor da multa é R$ {:.2f}'.format(multa))
