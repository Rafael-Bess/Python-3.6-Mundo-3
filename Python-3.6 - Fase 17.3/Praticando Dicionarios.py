##################################### no código acima aparece o Nome e a idade no caso Pedro e 25
dados = dict()
dados = {'Nome': 'Pedro', 'Idade': 25}
print(dados['Nome'])
print(dados['Idade'])
##################################### no código abaixo estaremos adicionado sexo ao dicionario dados.
dados['Sexo'] = 'M'
print(dados['Sexo'])
##################################### no codigo abaixo estou removendo dando Del em idade e ele some do dicionario
del dados['Idade']
print(dados)
##################################### Também posso utilizar o dicionario dando enter
filme = {'Titulo': 'Star Wars',
         'Ano': 1997,
         'Diretor': 'George Lucas'}

print(filme.values()) #Value é utilizado para pegar os dados ex star wars, 1997 e George Lucas
print(filme.keys()) #Keys é utilizado para pegar as colunas ex: Titulo, Ano Diretor
print(filme.items()) #Caso eu queira pegar todos vai ser utilizado o items
for k, v in filme.items():
    print(f'O {k} é {v}')
########################################################################################################################
#Lembrar que é possivel colocar um dicionario dentro de uma lista/tupla.


#Dicionario dentro de lista
brasil = list()
estado = dict()
for c in range(0, 3):
    estado['UF'] = str(input('Digite o Estado Federativo: '))
    estado['Sigla'] = str(input('Digite a Sigla do estado: '))
    brasil.append(estado.copy()) # para colocar o dicionario em um lista deve ser utilizado o .copy no lugar do [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o campo {v}') #importante

for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()

