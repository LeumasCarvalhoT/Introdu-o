i = 0
mai = 0
pesado = 0

import os
def topo():
 os.system('cls')
 print("----------------------------------")
 print("      DETECTOR DE PESADO")
 print("Maior peso até então: ",mai,"Kg")
 print("----------------------------------")

 

    

topo()
for i in range(1, 4):
    n = str(input("Digite o nome da pessoa: "))
    p = float(input("DIgite o peso dela: "))

    if (p >= mai):
        mai = p
        pesado = n 
    topo()

os.system('cls')  

print("A pessoa mais pesada foi ", pesado," com", mai)