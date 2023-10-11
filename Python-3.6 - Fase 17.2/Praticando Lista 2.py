print(50 * '=', 'FASE 17.2', 50 * '=')

pessoas = [['Pedro' , 25], ['Maria', 19], ['João', 32]]
print(f'{pessoas}')

print(f'{pessoas[0][0]}') # vai printar o nome de Pedro
print(f'{pessoas[1][1]}') # vai printar a idade 19 de Maria
print(f'{pessoas[2][0]}') # vai printar o João
print(f'{pessoas[1]}') # printou a maria e idade dela

print(15 * '=')

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print(15 * '=')

teste2 = [['Carlos', 25], ['Fernando', 19], ['Marcos', 32]]
for item in teste2[0:2]:  # Itera sobre as listas na posição 0 e 1
    print(item) # aqui está pegando todos os itens que estão na lista por exemplo (carlos 25 e fernando 19)
teste2[0][0] = 'João'
teste2[1][1] = 22
teste2[2][1] = 64
print(teste2)



galera = [['joao', 19], ['Carol', 34], ['Rafael', 21], ['Marcos', 32], ['Victoria', 30]]
for p in galera:
    print(f'{p[0]} tem {p[1]} de idade')





galera = list()
dado = list()
totmai = totmen = 0
listamai = list()
listamen = list()
for c in range(0, 3):
    dado.append(str(input('Digite o seu nome: ').title()))
    dado.append(int(input('Digite a sua idade: ')))
    galera.append(dado[:]) # devo utilizar a copia de dados para agrupar varios
    dado.clear()
     # devo dar clear porque se repetir os inputs no for vai dar ruim.

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
        listamai.append(p[0])
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
        listamen.append(p[0])
print(f'Temos {totmai} maiores de idade e {totmen} menor de idade.')
