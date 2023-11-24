'''*O que é uma FUNÇÃO no Python?
São blocos nomeados de um código designado para fazer um trabalho em específico. Elas permitem que você escreva o código uma vez que
 poderá ser usado a quantidade de vezes que você precisar para fazer uma mesma função. As funções podem pegar a informação que elas precisam e retornar a informação que elas geram. Então, basicamente é um jeito de tornar os programas fáceis de escrever, ler, testar, e consertar.


*Para definir uma função, a primeira linha dela é a sua definição, marcada pela palavra-chave DEF. O nome da função é seguido por um conjunto
 de parênteses e dois pontos. Uma DOCSTRING, em aspas triplas, descreve o que a função faz. O corpo da função ou o bloco de códigos dela é identado em um nível.'''


def lin():
    print('-' * 20)


print('Teste de Linha')
lin()


def mensagem(msg): # utilizei o nome de msg para definir o parametro do 2° print onde mensagem('vai ir pra dentro do print de msg')
    print('-=' * 20)
    print(msg)
    print('-=' * 20)

#   programa principal
mensagem('Teste mensagem')


a = int(input('digite um número: ')) # também posso definir o parametro utilizando
b = int(input('digite um número: ')) # o nome da variavel A & B antes --linha 20

def soma(a, b):
    s = a + b
    print(s)


#programa principal
soma(3, 6)
soma(7, 3)
soma(a=5, b=5) # posso também fazer a variavel receber algo diretamente
soma(a, b) # recebendo os inputs nas linhas 9 e 10


mensagem('soma2')
def soma2(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
soma(a=4, b=5)


# simbolo * é utilizado quando não sabemos a qt dos parametros (linha 31)
# o python após receber varios parametros ele criou uma tupla
def contador(* num): # Para utilizar inumeros parametros deve ser utilizado *
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} numeros')
    for valor in num:
        print(f'{valor} ', end='')
    print('fim')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


mensagem('listas')

#Trabalhando funções com listaaas.
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [5, 3, 2, 9]
dobra(valores)#tudo que eu tiver fazendo no def de lista vai impactar em valores
print(valores)


