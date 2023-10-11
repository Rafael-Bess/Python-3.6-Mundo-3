'''from random import randsample
numeros = []
qtjogos = int(input('Quantos jogos você deseja gerar?' ))
for c in range(1, qtjogos +1):
    for n in range(6):
        numero = randsample(0, 60)
        numeros.append(numero)
    print(f'{c} Lista: {numeros}')
    numeros.clear()'''

from time import sleep
from random import randint
lista = list()
listaa = list()
qtjogos = int(input('Quantos jogos você deseja gerar?' ))
total = 1
while total <= qtjogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    listaa.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 3, f'Sorteando {qtjogos}', '-=' * 3)
for i, e in enumerate(listaa):
    print(f'Jogo {i+1}: {e}')
    sleep(1)
print('-=' * 3, 'Boa Sorte', '-=' * 3)
