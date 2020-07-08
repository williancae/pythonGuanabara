numero = list()
r = ''
n = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in numero:
        numero.append(n) #Adiciona no final da lista
        print('Valor Adicionado!')
    else:
        print('Valor Duplicado!')
    r = str(input('Quer continuar [S/N]: '))
    if r in 'Nn':
        break
print('-+'*20)
print(f'Voce digitou {numero}!')
print('-+'*20)