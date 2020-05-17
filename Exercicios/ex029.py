'''
Leia nome commpleto e mostre primeiro nome e segundo nome
'''
nomeCompleto = str(input('Digite seu nome: ')).strip()
print('Seu nomoe copleto é {}'.format(nomeCompleto))
nomeCompleto = nomeCompleto.split()
print('Primeiro nome: {}'.format(nomeCompleto[0]))
print('Ultimo nome:  {}'.format(nomeCompleto[-1]))
