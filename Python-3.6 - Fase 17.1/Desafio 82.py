lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N]: ')
    if resp in 'Nn':
        break
par = list()
impar = list()
for elemento in lista: # os elementos de listacopia estão sendo percorridos e então realizados uma filtragem abaixo
    if elemento % 2 == 0:
        par.append(elemento)
    else:
        impar.apepnd(elemento)
print(f'A lista completa é {lista}')
print(f'Os números pares são: {par}')
print(f'Os números impares são: {impar}')
