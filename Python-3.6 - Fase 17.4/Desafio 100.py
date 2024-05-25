'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar().
A primeira função vai sortear 5 números 
e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares 
sorteados pela função anterior'''

from random import randint


def sorteia(lista):
   for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)   
        print(f'{n}', end=' ', flush=True)


def somapar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'E a soma dos pares são {soma}')
        
            


    #===============================================================================================================================================================================================
#Programa Principal
numeros = list()
sorteia(numeros)
somapar(numeros)




