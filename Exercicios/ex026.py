'''
Leia o nome de uma cidade e diga se inicia com 'santo' ou nao
'''
city = str(input('Nomde da cidade: '))
city = city.split(' ')
print('O nome inicia com Santo: {}'.format('Santo' in city[0]))