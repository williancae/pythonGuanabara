def leiaInt(num):
    while True: 
        valor = str(input((num)))
        if valor.isnumeric(): return valor
        else: print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        if valor.isnumeric(): break
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')