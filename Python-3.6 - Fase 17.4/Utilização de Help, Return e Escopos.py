help(print) #neste caso estou verificando oque o print faz utilizando o comando help()
print('=' * 50, end='\n')
print(input.__doc__) #uma forma de verificar o input seria utilizando o .__doc__

########################################################################################################################
########################################################################################################################
########################################################################################################################


'''Primeiro exemplo de como utilizar o comando help para documentar o programa'''
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = 1
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')


contador(2, 10, 2)
help(contador) # manual de doc string para verificar utilizando o contador (está na propria função de contador)

########################################################################################################################
########################################################################################################################
########################################################################################################################
print('=' * 50, end='\n')
'''Somar 3 números'''


def somar(a,b,c=0): # '=0' no caso do parametro c não ser preenchido o C vai valer 0 também pode ser todos opcionais.
    '''
    Função utilizada para somar 2 ou 3 parametros                         v  sendo eles A B e C(opcional)
    :param a: primeiro valor a ser somado (obrigatório)
    :param b: segundo valor a ser somado (obrigatório)
    :param c: terceiro valor a ser somado (opcional)
    :return:
    '''
    soma = a + b + c
    print(f'A soma vale {soma}')



somar(3, 2, 5)
somar(1, 2)
#somar() # caso todos os parametros acima 'a,b,c' estiverem como =0 serão opcionais e não vai dar erro nessa chama
somar(a=2, b=8) # caso um dos parametros seja opcionais também podemos declaralos desta forma (pode ser fora de ordem tmb)
print('=' * 50, end='\n')
########################################################################################################################
########################################################################################################################
########################################################################################################################
#ESCOPO DE VARIÁVEIS

def teste():
    x = 8 # está variavel é uma variavel local e não pode ser puxada no programa principal
    print(f'na função teste, n vale {n}')
    print(f'na função teste, x vale {x}')


#Programa Principal
n = 2 # n é uma variavel global
print(f'No programa principal, n vale {n}')
#print(f'na função teste, x vale {x}') # X vai dar erro porque foi declarado um valor apenas na função e não no principal
teste()
print('=' * 50, end='\n')
########################################################################################################################
########################################################################################################################
########################################################################################################################
#Utilização de variaveis globais e locais exemplo

#******** ESCOPO GLOBAL
#&&&&&&&& ESCOPO LOCAL
def teste(b):
    b += 4 # Variavel local que é utilizada apenas na função. que pega o valor de A e soma com B
    c = 2
    print(f'A dentro vale {a}')
    print(f'A dentro vale {b}')
    print(f'A dentro vale {c}')
#&&&&&&&& ESCOPO LOCAL

#Programa principal
a = 5 #Variavel A está sendo utilizada em toda o escopo global definido por ********
teste(a)
print(f'A dentro vale {a}')
print('=' * 50, end='\n')
#print(f'A dentro vale {b}')
#print(f'A dentro vale {c}') não será possivel printar o B e C dentro porque ela está fora do escopo local definido por &&&&&&&&
#******** ESCOPO GLOBAL

########################################################################################################################
########################################################################################################################
########################################################################################################################
#Melhorando o exemplo de ESCOPO GLOBAL E ESCOPO LOCAL

#********
#&&&&&&&& ESCOPO LOCAL
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')
#&&&&&&&& ESCOPO LOCAL

#programa principal
n1 = 2
funcao()
print(f'N1 global vale {n1}')
#********

########################################################################################################################
########################################################################################################################
########################################################################################################################
#Retornando valores utilizando RETURN()

def somar2 (a=0, b=0, c=0):
    soma = a + b + c
    return soma

#programa principal
r1 = somar2(3, 2, 5)
r2 = somar2(2, 2)
r3 = somar2(6)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')
########################################################################################################################
########################################################################################################################
########################################################################################################################
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print('É Par')
else:
    print('É Impar')
########################################################################################################################
########################################################################################################################
########################################################################################################################