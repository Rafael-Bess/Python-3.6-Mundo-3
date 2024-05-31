def leiaInt(mensagem):
    while True:
        try:
            n = int(input(mensagem))
            return n
        except ValueError:
            print("Erro! Por favor, digite um número inteiro válido.")

# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')