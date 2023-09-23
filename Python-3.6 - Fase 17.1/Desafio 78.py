cont = 0
numeros = []
for pos in range(0, 5):
    numeros.append(int(input(f'Digite a posição {cont}: ')))
    cont += 1
numasc = sorted(numeros)
maior_valor = numasc[-1]
menor_valor = numasc[0]

posicoes_menor = [i for i, x in enumerate(numeros) if x == menor_valor]
posicoes_maior = [i for i, x in enumerate(numeros) if x == maior_valor]
print(20 * '=-')

print(f'O Menor valor digitado é {menor_valor} nas posições {posicoes_menor[:]}')
print(f'E o Maior valor digitado é {maior_valor} nas posições {posicoes_maior[:]}')
