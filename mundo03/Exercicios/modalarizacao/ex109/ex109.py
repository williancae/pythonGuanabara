import ex109Formatacao as a
p = float(input('Digite um numero: '))
print(f'O dobro de {a.moeda(p)} é {a.moeda(a.dobro(p))}')
print(f'A metade de {a.moeda(p)} é {a.moeda(a.metade(p))}')
print(f'O aumentando 10% é {a.moeda(a.aumenta(p, 10))}')
