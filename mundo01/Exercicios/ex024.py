"""
leia nome completo e traga nome todo em maiusculo, tudo minusculo, quantas letras menos espaços quantas letras tem o primeiro nome
"""
nomeCompleto = str(input('Digite seu nome completo: '))
nomeCompleto = nomeCompleto.strip(); #tirando espaços iniciais e finais
print('Maiusculas: {}'.format(nomeCompleto.upper()))
print('Minusculas: {}'.format(nomeCompleto.lower()))
print('Quantidade total de letras: {}'.format(len(nomeCompleto) - nomeCompleto.count(' ')))
print('Quantidade total de letras primeiro nome: {}'.format(nomeCompleto.find(' ')))
# willian caetano campos