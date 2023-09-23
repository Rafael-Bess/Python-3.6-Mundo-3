from random import randint
lista = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
listaabc = sorted(lista)
print(f'Os números escolhidos foram {lista}')
print(f'O maior número é {listaabc[-1:]}')
print(f'O menor número é {listaabc[:1]}')
