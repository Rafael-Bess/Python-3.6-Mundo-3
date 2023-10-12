jogador = dict()
jogador['Nome'] = str(input('Digite o nome do Jogador: ')).title()
jogador['Jogos'] = int(input('Digite a quantidade de partidas jogadas: '))
jogador['QtGols'] = []

for c in range(1, jogador["Jogos"] + 1):
    gols = int(input(f'Quantos gols na partida {c}: '))
    jogador['QtGols'].append(gols)

jogador['Total de Gol'] = sum(jogador['QtGols'])

for k, v in jogador.items():
    print(k, v)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Jogos"]} partidas')
print('Gols em cada partida:')

for c, v in enumerate(jogador['QtGols'], start= 1):
    print(f'Partida {c}: {v} gols')
