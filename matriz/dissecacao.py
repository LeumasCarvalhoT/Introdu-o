import os
def lista():
    print()
    print("====================")
    print("   MENU DE OPÇÕES")
    print("====================")
    print("[1] Mostrar Matriz")
    print("[2] Diagonal Principal")
    print("[3] Triângulo Superior")
    print("[4] Triângulo Inferior")
    print("[5] Sair")


matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
opcao = 0


for i in range(0, 4):
    for j in range(0, 4):
        matriz[i][j] = int(input(f"Digite o valor da posição[{i},{j}]: "))



os.system('cls')
lista()
opcao = int(input("  OPÇÃO: "))
os.system('cls')


while opcao != 5:
    if opcao == 1:
        for i in range(0, 4):
            for j in range(0, 4):
                print(f"{matriz[i][j]:>4}",end='')
            print()

    elif opcao == 2:
        print(f"{matriz[0][0]:>4}")
        print(f"{matriz[1][1]:>8}")
        print(f"{matriz[2][2]:>12}")
        print(f"{matriz[3][3]:>16}")
        
    elif opcao == 3:
        print(f"{matriz[0][1]:>8}", f"{matriz[0][2]:>3}", f"{matriz[0][3]:>3}")
        print(f"{matriz[1][2]:>12}", f"{matriz[1][3]:>3}")
        print(f"{matriz[2][3]:>16}")

    elif opcao == 4:
        print()
        print(f"{matriz[1][0]:>4}")
        print(f"{matriz[2][0]:>4}", f"{matriz[2][1]:>3}")
        print(f"{matriz[3][0]:>4}", f"{matriz[3][1]:>3}", f"{matriz[3][2]:>3}" )



    lista()
    opcao = int(input("  OPÇÃO: "))
    os.system('cls')
