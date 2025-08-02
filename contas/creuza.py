saldo = float(input("Digite quantos reais você tem: "))
passagem = 200
custo = float(saldo / 5.57 * 1)
insuficiente = (saldo < passagem)
suficiente = (saldo >= passagem)

print("Você tem",f"{custo:.2f}", "em dolar")
print("Você não tem o dinheiro suficiente.", insuficiente)
print("Pode pegar a passagem.", suficiente)