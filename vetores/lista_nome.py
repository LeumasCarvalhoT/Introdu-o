soc = []

print("Escreva 5 nomes para fazer uma lista")

for i in range(1, 6):
    nome = str(input("Escreva um nome: "))
    if nome.capitalize().startswith("C"):
          soc.append(nome)

print("lista dos Nomes")
print(soc)