import ex110formatandoMoedas as a

p = float(input('Digite o Preço: '))
print(f'O dobro de {a.moeda(p)} é {a.dobro(p, True)}')
print(f'A metade de {a.moeda(p)} é {a.metade(p, True)}')
print(f'O aumentando 10% é {a.aumenta(p, 10, True)}')
