emprestimo = float(input("Quanto quer de emprestimo com o juros de 20%?: "))
parc = int(input("Por quantas vezes quer parcelar?: "))
total = emprestimo * 20 / 100 + emprestimo
por_parc = (emprestimo*20 / 100 + emprestimo) / parc

print("As parcelas serão de", f"{por_parc:.2f}")
print("Enquanto o valor total é de", f"{total:.2f}")