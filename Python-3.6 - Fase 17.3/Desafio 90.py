#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela
dados = dict()
dados['nome'] = str(input('Digite o seu nome: ')).title()
dados['media'] = float(input(f'Media de {dados["nome"]}: '))
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
if dados['media'] >= 7:
    dados['situação'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situação'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
print(f'O aluno {dados["nome"]} teve a media de {dados["media"]} e ficou como {dados["situação"]}')