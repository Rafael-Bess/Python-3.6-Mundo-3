'''from time import sleep
from random import randint
lista = list()
resultado = dict()
print('Bem-vindo ao jogo de dados...')
for c in range(0, 4):
    resultado['Nome'] = str(input('Olá, digite seu nome: '))
    resultado['Dado'] = num = randint(1, 6)
    print(f'{resultado["Dado"]}')
    lista.append(resultado.copy())
print(lista)
for i in lista:
    listaord = sorted(lista['Dado'])'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado') #K seria a chave(Key) e o V o valor(Value)
    sleep(1)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)#estou pegando os itens de jogo e ordenar pela chave 1 que é os numeros
print('=-' * 10, 'RANKING', '=-' * 10)
for i, v in enumerate(ranking):
    print(f'Em {i + 1}° lugar o {v[0]} tirou {v[1]}')
