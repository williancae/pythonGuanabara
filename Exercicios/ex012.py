'''
Faça um Programa que leeia a largura e altura de parede em metros e calcule a sua quantidade de tinta necesaria para pintala sabendo que que cada litro pinta uma area de 2m²
'''
largura = float(input('Digite a Largura: '))
altura = float(input('Digite Altura: '))
area = largura * altura
quantidade = area/2
print('Com a Area de {:.2f} m², é necessario possuir {:.2f} Litros de tinta'.format(area, quantidade))