def leiaInt(inteiro):
    while True: 
        valor = str(input((inteiro))).strip()
        if valor.isnumeric(): 
            return valor
        else: 
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        if valor.isnumeric(): break

def leiaFloat(real):
    while True: 
        valor = str(input((real))).strip().replace(',','.')
        if valor.isalpha(): 
            return valor
        else: 
            print('\033[1;31mERRO! Digite um número Real válido\033[m')
        if valor.isalpha(): break
R = leiaFloat('Digite um numero Real: ')
I = leiaFloat('Digite um numero Inteiro: ')