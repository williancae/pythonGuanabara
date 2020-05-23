'''
digite o sexo que aceite apenas M e F, quando nao umas dessas opçoes saia do laço
'''
sexo = 'M'
while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite [M] pra masculino e [F] pra feminino: ').upper().strip())
print('O sexo é [{}]!'.format(sexo))

# Ou
sexo = str(input('Digite [M] pra masculino e [F] pra feminino: ').strip().upper()[0])
while sexo not in 'FM':
    sexo = str(input('Digite [M] pra masculino e [F] pra feminino: ').strip().upper()[0])
print(f'O sexo é [{sexo}]!')
