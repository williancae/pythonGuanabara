from time import sleep
def maior(*num):
    cont = maior = 0
    print('\nAnalizando os valores Passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam inforamados {cont} valores ao todo')
    print(f'O maior é {maior}')

maior(2,6,4,23,5,23,64,34,64,2,3,54,75)
maior(1,34,52,34,676,45,23)
maior(2,5,7,85,3,2,5) 