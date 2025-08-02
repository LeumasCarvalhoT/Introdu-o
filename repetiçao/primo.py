c = 1
contdiv = 0
n = int(input("Escreva um número: "))

for c in range(1, n):
    if n % c == 0:
        contdiv += 1
    c = c + 1

if contdiv > 2:
    print("O valor", n, "não é primo.")

else:
    print("O valor", n,"é primo.")