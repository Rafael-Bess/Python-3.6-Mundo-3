def ficha():
    nome = input("Digite seu nome ")
    gols = input("Digite a quantidade de gols ")
    if not gols:
        gols = 0

    if not nome:
        nome = "<Desconhecido>"

    print(f'O jogador {nome} fez {gols} gols')


#Programa principal
ficha()

