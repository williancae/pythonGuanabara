'''
Digite um numero de 0 a 9999, e diga seu milhar, centena, dezenas, unidades
'''
print('Numeros validos de 0 a 9999')
num = list(str(input('Digite um numero: ')))
# num = list(num)
print('===========\nUnidades: {}\nDezenas: {}\nCentenas: {}\nMilhar: {}'.format(num[3],num[2],num[1],num[0]))