id = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            id[i][j] = 1

for i in range(0, 3):
    for j in range(0, 3):
        print(id[i][j], end='  ')  
    print()