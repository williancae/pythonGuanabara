pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0] #colocando em Maiusculo e pegado apenas o primeiro Caracter
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
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
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('C) Pessoas acima da media de idade ')
for p in galera:
    if p['idade'] > media:
        print('    ')
        for k, v in p.items():
            print(f'{k}: {v}', end=' ')
        print()
print('°°'*35)