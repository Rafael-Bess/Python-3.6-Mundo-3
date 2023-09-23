tupla = ('CASA', 'BARRACA', 'MESA', 'BARCO',
         'FAROL', 'MARUJO', 'SEREIA', 'MARISCO')
for c in tupla:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra, end=' ')
