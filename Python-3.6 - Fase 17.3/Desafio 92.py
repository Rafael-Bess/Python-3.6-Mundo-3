pessoa = dict()
pessoa['nome'] = str(input('Digite o seu nome: '))
pessoa['dtnasci'] = int(input('Digite o ano de nascimento: '))
print('[0] = Não')
pessoa['CTPS'] = int(input('Possui CTPS? Número: '))
pessoa['Idade'] = 2023 - pessoa['dtnasci']
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salario: '))
    resultado = 2023 - pessoa['Contratação']
    pessoa['Aposentadoria'] = (35 - resultado) + pessoa['Idade']
print('=-' * 10, 'Dados pessoais', '=-' * 10)
for i, v in pessoa.items():
    print(f'{i.title()} = {v}')
