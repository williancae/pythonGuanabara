palavras = ('ANNA', 'CARRO' , 'FUTEBOL', 'SKATE','PYTHON','JAVA','CHUVA','ARVORE','NATUREZA')
count = 0
for x in range(0,len(palavras)):
    print(f"\nNa palavra {palavras[x]} temos as vogais:", end=' ')
    for i in palavras[x]: # divide a palavra em letras
        if i in 'AEIOUÃ': # verifica se posição[i] esta entra essas sequencias letras
            print(i,end=' ')
print('\n')