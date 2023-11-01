from time import sleep
'''Faça um programa que tenha uma função chamada contador(), que receba três parametros
iniciom fim e passo e realizar a contagem. Seu programa tem que realizar três contagens
atráves da função criada:
A: de 1 até 10, de 1 em 1
B: de 10 até 0, de 2 em 2
C: Contagem personalizada (inserir)'''
from time import sleep


#Funções
def linha():
    tamanho = 40
    print('=' * tamanho)


def programa(msg):
    print('=-' * 21)
    print(msg)
    print('=-' * 21)

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até o {fim} de {passo} em {passo}')
    linha()
    sleep(2.5)

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1


    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ',  end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print('Fim!')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print('fim')

#Código principal
programa('Ola pessoal eis aqui a contagem de números')
contador(1, 10, 2)
contador(1, -5, 2)
print('Sua vez de fazer a contagem!')
ini = int(input('Digite o Inicio da contagem:'))
final = int(input('Digite o final da contagem:'))
pas = int(input('Digite a quantidade de passos da contagem:'))
contador(ini, final, pas)