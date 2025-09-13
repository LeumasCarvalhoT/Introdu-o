
b1 = 'B1'
b2 = 'B2'
b3 = 'B3'
b4 = 'B4'
b5 = 'B5'
b6 = 'B6'
b7 = 'B7'
b8 = 'B8'
b9 = 'B9'
b10 = 'B10'
cadeira = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
resp = 's'

import os
while resp.lower() == 's':

 os.system('cls')
 print(cadeira)
 print("---------------------------------------------------------------")
 assento = str(input("Qual assento deseja alugar?: "))
 if ((assento == 'B1') and (cadeira[0] == '---')):
     print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B2') and (cadeira[1] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B3') and (cadeira[2] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B4') and (cadeira[3] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B5') and (cadeira[4] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B6') and (cadeira[5] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B7') and (cadeira[6] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B8') and (cadeira[7] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B9') and (cadeira[8] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")

 elif (assento == 'B10') and (cadeira[9] == '---'):
    print("ERRO: ASSENTO JÁ OCUPADO OU INVÁLIDO!.")


 for i in range(len(cadeira)):
        if(assento == cadeira[i]):
            cadeira[i] = '---'

 resp = str(input("Deseja continuar?[S/N]: "))

os.system('cls')
print(cadeira)
print("Os assentos alugados foram: ")
for i in range(len(cadeira)):
    if cadeira[i] == '---':
        print("B",i + 1, end='  ')






