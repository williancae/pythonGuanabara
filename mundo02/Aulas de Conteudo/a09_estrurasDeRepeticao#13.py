'''
Laços de Repeticao
--Simplificar codigos repetivos - Com (For x in y:)
    for c in range(1,10):
        função
    foraLaço
--
'''
print('oi')
print('oi')
print('oi')

# Ou
print('\nCom o Laço')
for c in range(1,6):
    print(c,' - oi')
print('FIM')

# ou Decrementar
print('\nCom o Laço')
for c in range(6, 0, -1):
    print(c,' - oi')
print('FIM')

# ou for com intervalos
print('\nCom o Laço')
for c in range(0, 10, 2):
    print(c,' - oi')
print('FIM')

# ou com entrada de dados
n = int(input('\nDigite um numero: '))
print('Com o Laço')
for x in range(0, n+1):
    print(x, '- Oi')
print('Fim')

# ou estipulando inicio, fim e intervalos
i = int(input('\ninicio: '))
f = int(input('fim:  '))
p = int(input('Intervalo/ passos: '))
for c in range(i, f, p):
    print(c, '- oi')
print('Fim')

# ou ler valores dentro de for & operações
print('\ncom laço for')
s = 0 #iniciando variavel
for c in range(1, 4):
    n = int(input('{}° - Digite um numero: '.format(c)))
    s += n
print('somatoria é ', s)