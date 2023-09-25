lista = []
contador = 0
while True:
    num = int(input('Digite um número: '))
    cont = input('Deseja continuar? [S/N]'.lower())
    contador += 1
    lista.append(num)
    if cont in 'Nn':
        break
print(f'você digitou {contador} elementos')
lista.sort(reverse=True)
print(f'A ordem descrecente da lista é: {lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
