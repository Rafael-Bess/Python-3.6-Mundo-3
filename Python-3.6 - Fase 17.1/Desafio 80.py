lista = list()
for cont in range(0, 5):
    numeros = (int(input('Digite um valor: ')))
    if cont == 0 or numeros > lista[-1]:
        lista.append(numeros)
    else:
        pos = 0
        while pos < len(lista):
            if numeros <= lista[pos]:
                lista.insert(pos, numeros)
                break
            pos += 1
print(lista)
