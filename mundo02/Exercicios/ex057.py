menor = 0
maior = 0
for c in range(0, 5):
    peso = float(input('Digite peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print('Maior {}\nMenor {}'.format(maior,menor))
