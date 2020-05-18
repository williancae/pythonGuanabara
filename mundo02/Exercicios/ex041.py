'''
Leia ano de nascimento de compare com a data inicial para para saber se é maior ou igual a 18 anos
'''
from datetime import date
anoA = date.today()
b = int(anoA.year)
# print(type(b))
# ----------------------
anoN = int(input('Ano de Nascimento: '))
if 17 <= (b - anoN) <= 18:
    print('Você devera se apresentar pro alistamento!')
elif (b - anoN) > 18:
    print('Passou da Hora meu amigo!')
else:
    print('Aguarde sua vez, voce sera chamado!')
