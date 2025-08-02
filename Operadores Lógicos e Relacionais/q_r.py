l1 = int(input("Digite o 1° lado: "));
l2 = int(input("Digite o 2° lado: "));
l3 = int(input("Digite o 3° lado: "));
l4 = int(input("Digite o 4° lado: "));

qua = (l1 == l2) and (l2 == l3) and (l3 == l4)
ret = (l1 != l2) and (l3 != l4) and (l1 == l3) and (l4 == l2)

print("É um quadrado?", qua)
print("É um retanculo?", ret)


