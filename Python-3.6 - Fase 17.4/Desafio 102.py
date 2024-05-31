def fatorial(num, show=False):
    resultado = 1  # Start with 1 since 0! = 1 and 1! = 1
    contador = num
    while contador > 1:  
        if show:
            print(f'{contador} x ', end='')
        resultado *= contador  
        contador -= 1
    if show:
        print('1 = ', end='')  # Print the final part of the factorial calculation
    return resultado


print(fatorial(5, show=True))