dia = int(input('Quantos dias Alugados: '))
km = float(input('Quantos quilometros rodados:'))
pago = (dia * 60) + (km * 0.15)
print(f'o total a ser pago é {pago:.2f}')