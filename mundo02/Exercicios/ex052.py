'''
ler os 6 numeros, se for par somatoria se for impar desconsidera
'''
s = 0 #somatoria
for x in range(1,7):
    num = int(input('Digite {}° numero: '.format(x)))
    if num % 2 == 0:
        s += num
print('A somatoria dos pares é', s)
