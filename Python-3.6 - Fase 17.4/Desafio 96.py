'''adorei da forma que fiz me diverti bastante sei que tem formas mais compactadas e simples, porém essa achei complexa e muito estilizada.
'''
'''Façã um programa que tenha uma função chama area(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.'''
# funções

# código de inicio de linhas do programa

def linhainicio(msg):  # função utilizada para mostrar o tópico do programa 'definição'
    print('-' * 50)
    print(msg)
    print('-' * 50)

def linha(): # função utilizada para mostrar uma separação do código e deixar estilizado
    print('-' * 50)


# função utilizada para calcular a pessoa inserir os dados de comprimento e largura
def area(): #função para calculo e printar o calculo de uma area em metros quadrados e estilizado
    comprimento = float(input('Digite o comprimento: '))
    largura = float(input('Digite a largura: '))
    linha()
    calculo_area = largura * comprimento
    print(f'A Area de um terreno retangular é: {calculo_area:.2f}(m²)')
    linha()
15
#código principal
linhainicio('Calculo precido das dimensões de um terreno retangular')
print('Exemplo de calculo: Largura = [20.78] Comprimento [21.75]')
linha()
area()
while True: # utilizei forma de repetição infinita para quando usarem o S de continue ele printe area
    cont = input('Quer continuar? [S]|[N]: ')
    linha()
    if cont in ('Ss'):
        area()
    else:
        print('Fim do código')
        break
        '''por algum motivo se eu não utilizar break ele printa um fim do código ele da erro porque é float
        não sei como ajustar. e se eu tentar utilizar outro metodo da erro ao usar o N :('''
