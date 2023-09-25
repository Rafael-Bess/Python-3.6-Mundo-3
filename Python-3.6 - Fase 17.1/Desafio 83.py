expressao = str(input('Digite a expressão: '))
pilha = []
for elemento in expressao:
    if '(' in elemento:
        pilha.append(elemento)
    elif ')' in elemento:
        pilha.append(elemento)
if pilha.count('(') == pilha.count(')'):
    print('A espressão está correta')
else:
    print('A espressão está errada')

