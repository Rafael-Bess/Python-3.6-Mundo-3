#[LISTAS]
# A partir do momento que iguala uma lista na outra elas criam uma ligação.
a = [2,3,4,7]
b = a #Aqui elas tem ligação uma com a outra
b2 = a[:] #Aqui a lista B está recebendo uma copia de A
b[2] = 8
print(f'lista A {a}\nLista B {b}\nLista B2 {b2}')

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
print(len(lanche)) #Para ver a quantidade de palavras

print('\nPara substituir algum item da lista deve-se utilizar a lista e a posição = lanche[3]')
lanche[3] = 'picole'
print(lanche)

print('\nPara adicionar um novo item a lista deve-se utilizar APPEND')
lanche.append('Cookie')
print(lanche)

print('\nPara inserir um novo item em uma determinada posição deve-se utilizar insert')
lanche.insert(0,'Cachorro-Quente')
print(lanche)

print('\n Para apagar algum item da lista deve-se utilizar del lanche[3] / lanche.pop(3) / lanche.remove(pizza))')
del lanche[0]
lanche.pop(4)
lanche.remove('picole')
print(lanche)

print('\n para fazer um input removendo algo da lista')
lanche.remove(input('Digite qual será eliminado: '))
print(lanche)

print('\n utilizando if para remover')
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)

print('\n utilizando a função list a variavél valores terá atribuido os numeros 4,5,6,7,8,9,10 na sua lista ')
valores = list(range(4,11))

print('\n Para ordenar valores é utilizado o valores.sort()')
valores2 =[8,2,5,4,9,3,6,7,0]
valores2.sort()
print(valores2)
print('\n para deixar a sequencia descrescente é utilizado valores.sort(reverse=True)')
valores2.sort(reverse=True)
print(valores2)
print('\n C está contando as posições e encontrando as respectivas posições de V em valores')
valores3 =[8,2,5,4,9,3,6,7,0]
for c, v in enumerate(valores3):
    print(f'Na posição {c} encontrei {v}')
print('Cheguei ao final da lista')
print('\nPara usuario adicionar valores em uma lista deve-se utilizar list()')
valores4 = list()
for cont in range(0, 5):
    valores4.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores4):
    print(f'Na posição {c} encontrei {v}')
print('Cheguei ao final da lista')
