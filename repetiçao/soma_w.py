soma = int(0)
cont = int(0)
resp = str(input(""))

while (resp == 's'):
    n = int(input("Digite o valor: "))
    soma = soma + n
    resp = str(input("Quer continuar? [s/n] "))

    

print("O resultado foi: ", soma)
