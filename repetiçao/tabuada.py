contador = int(0)
numero = int(input("Digite um número para fazer uma tabuada de 10: "))


for mult in range (contador, 10):

    contador = contador + 1;
    mult = int(contador * numero)

    print(numero, "x", contador, "=", mult)