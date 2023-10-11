pessoas = []
temp = []
pesomaior = pesomenor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))  # Convertendo a entrada para float
    if len(pessoas) == 0:
        pesomaior = pesomenor = temp[1]
    else:
        if temp[1] > pesomaior:
            pesomaior = temp[1]
        if temp[1] < pesomenor:
            pesomenor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    para = str(input('Quer continuar? [S|N] '))
    #Condição de parada.
    if para in 'Nn':
        break
print('=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas:')
for lpessoas in pessoas:
    print(lpessoas[0])
print('=' * 30)
print(f'O maior peso foi de {pesomaior} Peso de ', end='')
for p in pessoas:
    if p[1] == pesomaior:
        print(f'{p[0]},\n')
print(f'O menor peso foi de {pesomenor} ')
for p in pessoas:
    if p[1] == pesomenor:
        print(f'{p[0]} , ', end='')
