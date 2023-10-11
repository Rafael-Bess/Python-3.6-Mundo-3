matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para ({linha}) ({coluna}): '))
#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
#também pode ser feito o print com for
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:3^}]', end='')
    print()