def area(l1, l2):
    print(f'A are do Terreno é: {l1*l2}m²')
def row():
    print('°'*40)


row()
print('Area do Terreno')
row()
comprimento = float(input('Digite o comprimento do terreno: '))
largura = float(input('Largura do terreno: '))
row()
area(comprimento, largura)
