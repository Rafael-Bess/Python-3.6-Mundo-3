principal = list()
numero = 0  # ou qualquer valor inicial desejado
while True:
    nome = (str(input('Digite o seu nome:')))
    nota1 = (float(input('Digite sua nota [Ex:7.8]: ')))
    nota2 = (float(input('Digite sua nota [Ex:5.4]: ')))
    resp = str(input('Deseja continuar? [N/S]: '))
    media = (nota1 + nota2) / 2
    principal.append([nome, [nota1, nota2], media])
    if resp in 'Nn':
        break
print('=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"Média":>8}')
print('-' * 16)
for i, a in enumerate(principal):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('=-' * 20)
while True:
    numero = int(input('Qual aluno deseja ver a nota? (ou 999 para sair): '))
    if numero == 999:
        print('FINALIZANDO...')
        break
    if numero <= len(principal) - 1:
        print(f'As notas de {principal[numero][0]} são {principal[numero][1]}')
print('<<< VOLTE SEMPRE >>>')