'''
tupla de 0 a 20 por extenso, ao ler umm numero mostra o numero respectivo a ele
'''
ext = ('Zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if -1 >= num <= 20:
        print('Digite um numero valido entre 0 & 20')
    else:
        print(f'O numero por extenso é {ext[num]}')
        break
