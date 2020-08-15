jogadores = {}
golsPartidas = []
jogadores['nome'] = str(input('Nome jogador: '))
jogadores['partidas'] = int(input('Quantas partidas jogou: '))
quant = jogadores['partidas']
for i in range(0, quant):
    golsPartidas.append(int(input(f'Gols na {i+1}° partida: ')))
jogadores['golsPartidas'] = golsPartidas
jogadores['totalGols'] = sum(golsPartidas)
print(jogadores)