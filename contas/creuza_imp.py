gasto = float(input("Digite o quanto gastou: "))
total = gasto * 60 / 100 + gasto
imposto = total - gasto

print("O total do imposto será de", f"U${imposto:.2f}")
print("Já o quanto terá de pagar, é de", f"U${total:.2f}")
