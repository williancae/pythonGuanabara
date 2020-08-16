def notas():
    """A função notas retorna, para uma
     lista de notas escolares inseridas pelo usuário,
    um dicionário contendo o seguinte conteúdo:
    -Quantidade de notas
    -A maior nota
    -A menor nota
    -A média da turma
    -A situação (opcional para o usuário)
    Com cada índice do dicionário tendo o título correspondente acima.
    :return:
    """
    no = []
    maior = t = x = 0
    menor = 10
    n = int(input('Quantas notas tem? '))
    for i in range(n):
        no.append(int(input(f'Digite a {i + 1}ª nota: ')))
        if maior < no[i]:
            maior = no[i]
        if menor > no[i]:
            menor = no[i]
        t += no[i]
        if no[i] < 7:
            x += 1
    dic={}
    dic['Quantidade de notas']=n
    dic['maior nota']=maior
    dic['menor nota']=menor
    dic['média da turma']=t/n
    op=input('Você quer saber a situação da turma? [S/N] ').upper()
    if op=='S':
        if x >= n / 3: dic['Situação'] = 'Tá tensa'
        else: dic['Situação'] = 'Tá sussa'
    return dic
print('-='*15)
print(notas())