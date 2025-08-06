soma = 0
media = 0
pares = 0
nuls = 0
divs = 0

for i in range(1, 6):
    v1 = int(input("Digite um valor: "))

    soma += v1
    media = soma / 5
    
    if v1 % 2 == 0:
        pares  += v1

    if v1 % 5 == 0:
        divs  += 1

    if v1 == 0:
        nuls  += 1

print("\n")
print("O total dos números somados é equivalente a: ", soma)
print("A media dos números é: ",media)
print("O total de números divisiveis por cinco são: ",divs)
print("A soma dos valore pares é igual a: ",pares)
print("O total de valores nulos é de: ",nuls)