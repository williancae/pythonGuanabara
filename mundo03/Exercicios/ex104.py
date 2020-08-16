def ficha(nome ='<Desconhecido>', gol=0): print(f'O jogador {nome} fez {gol} gol(s).')    
j = str(input('Nome jogador: '))
g = str(input('Quantos Gols: '))
if g.isnumeric(): g = int(g)
else: g = 0
if j.strip() == '': ficha(gol = g)
else: fiha(j, g)