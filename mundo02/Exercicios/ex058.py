'''
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
maior = 0
idadeMulher = 0
homem = 0
maisVelho = ''
somaIdade = 0
for c in range(1,5):
    print('------------- {}º Pessoa --------------'.format(c))
    nome = str(input('Nome: ').strip())
    sexo = str(input('Sexo [F/M]: ').strip().upper())
    idade = int(input('Idade: ').strip())
    somaIdade += idade
    if sexo == 'M':
        homem += 1
        if c == 1:
            maior = idade
        else:
            if idade > maior:
                maisVelho = nome
                maior = idade
            elif homem == 0:
                nome = 'Não tem homem no grupo'
    else:
        if idade < 20:
            idadeMulher += 1
somaIdade /= 4
print('->>-'*10)
print('Media de idade {}'.format(somaIdade))
print('Homem mais Velho é {} '.format(maisVelho))
print('{} Mulhere(s) menores de 20'.format(idadeMulher))
