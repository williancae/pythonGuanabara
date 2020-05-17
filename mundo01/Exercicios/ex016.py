'''
Escreva um sistema de aluguel de carros com as seguintes informações cada dia de aluguel é DIA = 60 e  0.15 centavos por quilometro por rodado
'''
dia = int(input('Quantos dias com carro: '))
km = float(input('Quantos quilometros rodou: '))
dia *= 60
km *= 0.15
resultado = dia + km
print('Total a pagar R$ {}'.format(resultado))