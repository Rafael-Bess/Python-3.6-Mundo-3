tupla = ('Base', 200,
         'Rimel', 60,
         'Batom', 20,
         'Perfume', 350,
         'Primer', 55)
print(20 * '=')
print(f'{"Listagem de preços":^20}')
print(20 * '=')
produtos = tupla[0::2]
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:<14}', end='')
    else:
        print(f'R${tupla[pos]:>4}')