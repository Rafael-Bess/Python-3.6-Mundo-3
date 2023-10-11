'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatotal = coluna3 =  0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para ({linha}) ({coluna}): '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:3^}]', end='')
    print()
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            somatotal += valor
print(f'a soma total dos pares digitados são {somatotal}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = coluna3 = maiornum = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor para ({linha}) ({coluna}): '))
    print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:3^}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print(f'a soma total de todos os valores digitados é {somapar}')
for l in range(0, 3):
    coluna3 += matriz[l][2]
print(f'a soma total da terceira coluna é : {coluna3}')
for c in range(0, 3):
    if c == 0:
        maiornum = matriz[1][c]
    elif matriz[1][c] > maiornum:
        maiornum = matriz[1][c]
print(f'O valor da segunda linha é {maiornum}')