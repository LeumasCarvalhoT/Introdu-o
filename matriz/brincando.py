mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
maior3C = 0
sdp = 0
p2L = 1

for i in range(0, 4):
    for j in range(0, 4):
        mat[i][j] = int(input(f"Digite o valor da posição [{i},{j}]:"))
        if i == j:
            sdp += mat[i][j]


for j in range(0, 4):
    p2L *= mat[1][j]
    if mat[j][2] > maior3C:
        maior3C = mat[j][2]



for i in range(0, 4):
    for j in range(0, 4):
        print(f"{mat[i][j]:^5}", end='')
    print()

print()
print("A soma dos números da linha diagonal esquerda principal é",sdp)
print("A multiplicação dso números da segunda linha é",p2L)
print("O maior número da 3º coluna é",maior3C)