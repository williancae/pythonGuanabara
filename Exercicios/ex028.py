nomeCompleto = str(input('Digite nome completo: ')).lower().strip()
print('A letra (a) aparece {} vezes'.format(nomeCompleto.count('a')))
print('A primeira letra (a) na posição: {}'.format(nomeCompleto.find('a')+1))
print('A ultima letra (a) posição: {}'.format(nomeCompleto.rfind('a')))
