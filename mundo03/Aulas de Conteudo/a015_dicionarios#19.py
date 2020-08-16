# Dicionarios

# Declarando dicionarios
dados = dict()
dados = {}
# Atribuido valor
# nome = ['willian','gabriel','murilo','samuel','miguel']
dados = {'nome':'Willian','idade':20}
# mostrar conteudo
print('\n\n')
print(dados['nome'])
# Adicionando valores ao dicionario
dados['sexo'] = 'M'
# Deletando elementos
del dados['idade']
# ----------------------------------------
filme = {
    'titulo':'Scooby Doo',
    'ano':2002,
    'diretor':'Desconhecido'
}
print(filme.values())
print(filme.keys())
print(filme.items())
print('\n\n')
for k, v in filme.items():
    print(f'O {k} é {v}')
# ---------------------------
locadora = []
locadora.append(filme)
print()
print(locadora[0])
print(locadora[0]['titulo'])
print(locadora[0]['ano'])
# ----------
print()
pessoas = {'nome':'willian','idade':20,'sexo':'M'}
for k in pessoas.keys():
    print(k) # Mostrando todas as chaves
print()
for v in pessoas.values():
    print(v) # Mostrando todas os valores
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
# ---------------------------
print()
brasil = []
estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado1 = {'uf':'Sao Paulo', 'sigla':'SP'}
brasil.append(estado)
brasil.append(estado1)
print(brasil[1]['uf'])
# ------------------------------
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()