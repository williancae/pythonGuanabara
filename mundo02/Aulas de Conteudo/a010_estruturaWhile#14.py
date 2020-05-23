'''
TEORIA
---While (enquanto)
    while condicao:
        faça
    fim
Obs:
    -não é necessario saber o fim
    -pode vir diversão condições dentro dele
'''
#pratica
for c in range(1,10):
    print(c)
print('fim')


# ou usando while
print('='*10, 'usando while')
c = 1
while c < 10:
    print(c)
    c +=1
print('Fim While')

# While com condição
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Foram digitados {} numeros pares e {} numeros impares'.format(par - 1, impar))