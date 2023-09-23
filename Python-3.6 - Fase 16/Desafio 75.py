valor1 = int(input('Digite um número inteiro: '))
valor2 = int(input('Digite um número inteiro: '))
valor3 = int(input('Digite um número inteiro: '))
valor4 = int(input('Digite um número inteiro: '))
tupla = (valor1, valor2, valor3, valor4)
print(f'Os valores digitados foram {tupla}')
print(f'O Número 9 apareceu {tupla.count(9)}ª vezes')
if 3 in tupla:
    pos = tupla.index(3) + 1
    print(f'O número 3 está na posição: {pos}')
for valor in tupla:
    if valor % 2 == 0:
        print(f'Foi digitado os seguintes números pares: {valor}', end=' ')