#(TUPLAS) [LISTAS] {DICIONARIO}
#TUPLAS SÃO IMUTAVEIS. por exemplo não pode atribuir nada a ele sem ser oque já foi atribuido. exemplo lanche receber sorvete no lugar de pudim
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(len(lanche))
print(lanche)
#print(lanche[1]) #vai pegar o suco porque o hamburguer é o 0
#print(lanche[1:3]) #vai imprimir apenas o suco e pizza porque o elemento 3 (pudim) é ignorado.
#print(lanche[1:]) #Imprimindo do elemento 1 até o final
#print(lanche[:3]) # vai aparecer até a pizza
#print(lanche[-2:]) # vai pegar da pizza até o pudim
#print(lanche[:-1]) # aqui ele vai começar e vai parar no -1 que é o pudim e não vai imprimir ele
'''for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi muitoooooo!!')'''

for comida in range(0, len(lanche)):
    print(f'eu vou comer {lanche[comida]} na posição {comida}') # caso precise usar a posição
print('Comi muitoooooo!!')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na pósição {pos}')

a = (1,3,6)
b = (1,3,4,5,7)
c = a + b
print(c, c.count(3))# contar quantos 3 existem
print(c, c.index(4)) #pegando o quarto. sempre lembrar de contar o 0
print(c, c.index(3, 2)) #aqui estou pegando o terceiro que está apartir da posição 2

pessoa = ('Rafael', 21, 'M', 73.60)
print(pessoa)
del(pessoa) #deleta oque possui na tupla.
pessoa = ('Gustavo', 39, 'M', 99.88) # Em python as tuplas podem ter varios tipos de dados String e Inteiros
print(pessoa)
