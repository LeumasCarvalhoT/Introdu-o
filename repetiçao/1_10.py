total = 0
impares = 0

for c in range(1, 6):
    v = int(input("Digite um número: "))
    
    if (v > 0) and (v <= 10):
        total += 1

    if v % 2 == 1:
        impares += v

print("O total de números entre 1 a 10 são de: ", total)
print("O total da soma dos impares é de: ", impares)
