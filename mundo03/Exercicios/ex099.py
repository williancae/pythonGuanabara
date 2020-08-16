from time import sleep
def contador(ini, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini < fim:
        fim += 1
    else:
        fim -= 1
        if passo>0:
            passo = passo*(-1)
    for x in range(ini, fim, passo):
        print(f'{x} ', end='', flush=True)
        sleep(0.3)
    print('FIM!')
    print('-='*20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez')
contador(int(input('Inínio: ')), int(input('Fim: ')), int(input('Passo: ')))
