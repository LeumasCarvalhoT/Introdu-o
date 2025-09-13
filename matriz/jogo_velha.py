posicao = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contador = 0

import os
posicao[0][0] = '1'
posicao[0][1] = '2'
posicao[0][2] = '3'
posicao[1][0] = '4'
posicao[1][1] = '5'
posicao[1][2] = '6'
posicao[2][0] = '7'
posicao[2][1] = '8'
posicao[2][2] = '9'

for i in range(0, 3):
    print("+---+---+---+")
    for l in range(0, 3):
        print(f"|{posicao[i][l]:^3}", end='')
    print("|")   
print("+---+---+---+")

rec = str(input("Onde jogará o [X]?: "))
contador += 1

for i in range(0, 3):
    for l in range(0, 3):
        if rec == posicao[i][l]:
            posicao[i][l] = 'X'

os.system('cls')

while contador != 5:
    #########################[O]
    for i in range(0, 3):
        print("+---+---+---+")
        for l in range(0, 3):
            print(f"|{posicao[i][l]:^3}", end='')
        print("|")  
    print("+---+---+---+")

    rec = str(input("Onde jogará o [O]?: "))

    if   ((rec == '1') and (posicao[0][0]) == 'X') or ((rec == '1') and (posicao[0][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '2') and (posicao[0][1]) == 'X') or ((rec == '2') and (posicao[0][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '3') and (posicao[0][2]) == 'X') or ((rec == '3') and (posicao[0][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '4') and (posicao[1][0]) == 'X') or ((rec == '4') and (posicao[1][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '5') and (posicao[1][1]) == 'X') or ((rec == '5') and (posicao[1][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '6') and (posicao[1][2]) == 'X') or ((rec == '6') and (posicao[1][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '7') and (posicao[2][0]) == 'X') or ((rec == '7') and (posicao[2][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '8') and (posicao[2][1]) == 'X') or ((rec == '8') and (posicao[2][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    elif ((rec == '9') and (posicao[2][2]) == 'X') or ((rec == '9') and (posicao[2][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [O]?: "))

    contador += 1


    for i in range(0, 3):
        for l in range(0, 3):
            if rec == posicao[i][l]:
                posicao[i][l] = 'O'

    os.system('cls')
     #DIAGONAL ESQUERDA
    if ((posicao[0][0] == 'O')  and (posicao[1][1] == 'O') and (posicao[2][2] == 'O') ): 
        break

    #DIAGONAL DIREITA
    if ((posicao[0][2] == 'O')  and (posicao[1][1] == 'O') and (posicao[2][0] == 'O') ): 
        break

    #1º LINHA
    if ((posicao[0][0] == 'O')  and (posicao[0][1] == 'O') and (posicao[0][2] == 'O') ): 
        break
    
    #2º LINHA
    if ((posicao[1][0] == 'O')  and (posicao[1][1] == 'O') and (posicao[1][2] == 'O') ): 
        break

    #3º LINHA
    if ((posicao[2][0] == 'O')  and (posicao[2][1] == 'O') and (posicao[2][2] == 'O') ): 
        break

    #1º COLUNA
    if ((posicao[0][0] == 'O')  and (posicao[1][0] == 'O') and (posicao[2][0] == 'O') ): 
        break

    #2º COLUNA
    if ((posicao[0][1] == 'O')  and (posicao[1][1] == 'O') and (posicao[2][1] == 'O') ): 
        break

    #3º COLUNA
    if ((posicao[0][2] == 'O')  and (posicao[1][2] == 'O') and (posicao[2][2] == 'O') ): 
        break
    
    #############################[X]
    for i in range(0, 3):
        print("+---+---+---+")
        for l in range(0, 3):
            print(f"|{posicao[i][l]:^3}", end='')
        print("|") 
    print("+---+---+---+")

    rec = str(input("Onde jogará o [X]?: ")) 

    if   ((rec == '1') and (posicao[0][0]) == 'X') or ((rec == '1') and (posicao[0][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '2') and (posicao[0][1]) == 'X') or ((rec == '2') and (posicao[0][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '3') and (posicao[0][2]) == 'X') or ((rec == '3') and (posicao[0][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '4') and (posicao[1][0]) == 'X') or ((rec == '4') and (posicao[1][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '5') and (posicao[1][1]) == 'X') or ((rec == '5') and (posicao[1][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '6') and (posicao[1][2]) == 'X') or ((rec == '6') and (posicao[1][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '7') and (posicao[2][0]) == 'X') or ((rec == '7') and (posicao[2][0]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '8') and (posicao[2][1]) == 'X') or ((rec == '8') and (posicao[2][1]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))

    elif ((rec == '9') and (posicao[2][2]) == 'X') or ((rec == '9') and (posicao[2][2]) == 'O'):
        print("JOGADA INVÁLIDA!")
        rec = str(input("Onde jogará o [X]?: "))


    for i in range(0, 3):
        for l in range(0, 3):
            if rec == posicao[i][l]:
                posicao[i][l] = 'X'
    
    os.system('cls')

    #DIAGONAL ESQUERDA
    if ((posicao[0][0] == 'X')  and (posicao[1][1] == 'X') and (posicao[2][2] == 'X') ): 
        break

    #DIAGONAL DIREITA
    if ((posicao[0][2] == 'X')  and (posicao[1][1] == 'X') and (posicao[2][0] == 'X') ): 
        break

    #1º LINHA
    if ((posicao[0][0] == 'X')  and (posicao[0][1] == 'X') and (posicao[0][2] == 'X') ): 
        break
    
    #2º LINHA
    if ((posicao[1][0] == 'X')  and (posicao[1][1] == 'X') and (posicao[1][2] == 'X') ): 
        break

    #3º LINHA
    if ((posicao[2][0] == 'X')  and (posicao[2][1] == 'X') and (posicao[2][2] == 'X') ): 
        break

    #1º COLUNA
    if ((posicao[0][0] == 'X')  and (posicao[1][0] == 'X') and (posicao[2][0] == 'X') ): 
        break

    #2º COLUNA
    if ((posicao[0][1] == 'X')  and (posicao[1][1] == 'X') and (posicao[2][1] == 'X') ): 
        break

    #3º COLUNA
    if ((posicao[0][2] == 'X')  and (posicao[1][2] == 'X') and (posicao[2][2] == 'X') ): 
        break

    







for i in range(0, 3):
    print("+---+---+---+")
    for l in range(0, 3):
        print(f"|{posicao[i][l]:^3}", end='')
    print("|")
print("+---+---+---+")
print("JOGO FINALIZADO!")
