'''
Verificar se o ano é bissexto ou não
'''
ano = int(input('Descubra se é bissexto\nDigite um ano: '))
if ano%4 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('Não é Bissexto!')