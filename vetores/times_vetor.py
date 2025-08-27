times = []

import os
for c in range(1, 4):
    nome = str(input("Digite os nomes dos Times: "))
    times.append(nome)

os.system('cls')

print("-----------------------------------")
print("       TABELA DE PARTIDAS")
print("-----------------------------------")

print(times[0],"[] x []", times[1])
print(times[0],"[] x []", times[2])

print(times[1],"[] x []", times[0])
print(times[1],"[] x []", times[2])

print(times[2],"[] x []", times[0])
print(times[2],"[] x []", times[1])





