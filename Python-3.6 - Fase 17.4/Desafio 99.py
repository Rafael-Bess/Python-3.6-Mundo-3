'''Faça um prgorama que tenha uma função chamada maior() que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

#Funções
#===============================================================================================================================================================================================
#Função para separar com linhas
def linha():
    print('=' * 40)


#Função que vai percorres os valores passados e verificar qual é o maior
def maior(*lista): # função para verificar qual o maior valor que eu inseri no programa principal
    maiorvalor = contador = 0
    menorvalor = 9999999999999999999999 # Inicializei o contador menor como muitos 9 para que contasse o menor corretamente
    print('Analisando os valores passados...') #printando na tela os maiores valores passados
    linha()

    if not lista:
        print('A lista está vazia') #caso a lista esteja vazia ele printa a lista está vazia e da quit
        return None

    for numero in lista:
        contador += 1

    for valor in lista:
        if valor > maiorvalor:
            maiorvalor = valor
        if valor < menorvalor:
            menorvalor = valor

    print(f'Os números {lista} ao todos são {contador} números\n' 
            f'O maior valor analisado foi de {maiorvalor} o menor valor analisado foi de {menorvalor}')

#===============================================================================================================================================================================================
#Programa Principal
linha()
maior(10, 5, 8,20,15)
linha()
maior(20,5,1,28,56)
linha()