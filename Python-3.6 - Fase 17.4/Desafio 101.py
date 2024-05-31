'''Crie um programa que tenha uma função chamada voto()
que vai receber como parametro o ano de nascimento de uma pessoa
retornando um valor literal indiciando se uma pessoa
tem voto negado -18 opcional +65 ou obrigatorio entre 18 a 65 nas eleiçoes'''


def voto():
    nascimento = int(input('Em que ano você nasceu: '))
    idade = 2018 - nascimento
    if idade <= 17:
        print(f'{idade} anos e você não pode votar.')
    if 18 <= idade <= 65:
        print(f'{idade} anos e você pode votar.')
    if idade >= 65:
        print(f'{idade} anos, e seu voto é opcional.')



voto()
