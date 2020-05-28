'''Inicinando variaveis'''
pro = cont = contHomem = menores = h = 0
idade = 0
sexo = ''
while True: '''Loop Infinito'''
    print('======= Cadastro ======')
    idade = int(input('Idade: ').strip())

    while True:
        sexo = str(input('Sexo [F/M]: ').strip().upper())
        if sexo == 'F' and idade < 20:
            menores += 1
        if sexo == 'M':
            contHomem += 1
        if sexo not in 'FM':
            print('INVALIDO!!')
        else:
            break

    if idade > 18:
        cont += 1

    # while True:
    pro = str(input('Continuar [S/N]: ').strip().upper())
    if pro == 'S':
        continue
    else:
        break

print(f'Total de pessoas com mais de 18 anos, {cont}')
print(f'Temos {contHomem} homens cadastrados')
print(f'Mulheres menores  de 20 {menores}')
