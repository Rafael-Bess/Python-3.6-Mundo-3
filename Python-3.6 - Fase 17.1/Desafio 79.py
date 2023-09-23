#Uma maneira para fazer validação é usar 2 variaveis lista que recebe numero
lista = list()
while True:
    numero = (int(input('Digite um número: ')))
    cont = str(input('Quer continuar? [S/N]')).upper()
    if cont == 'N':
        break
    if numero not in lista:
        lista.append(numero)
lista.sort()
print(lista)
