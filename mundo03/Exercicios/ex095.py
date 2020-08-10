pessoa = dict()
galera = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #colocando em Maiusculo e pegado apenas o primeiro Caracter
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy()) #pegar copia de PESSOA
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas com S ou N')
    if resp in 'N':
        break
print('°°'*35)
print(galera)