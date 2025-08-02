opc1 = 0
opc2 = 11

print("MENU")
print("[1] De 1 a 10.")
print("[2] De 10 a 1.")
print("[3] Sair.")
opcoes = int(input("Qual escolhe?: "))



while (opcoes != 3):
    opcoes = int(input("Qual escolhe?: "))
  
    if opcoes == 1: 

        while (opc1 < 10):
            opc1  += 1
            print(opc1)
        
   
    elif opcoes == 2:
     
        while(opc2 > 1):
         opc2 = opc2 - 1
         print(opc2)

    elif opcoes == 3:

        print("Contador finalizado")
        break