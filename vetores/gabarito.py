gabarito = []
aluno = []
resp = []
s1 = []
s2 = []
s3 = []
nota = []
Naluno1 = []
Naluno2 = []
Naluno3 = []
valor1 = 0
valor2 = 0
valor3 = 0

import os
print("-----------------------------")
print("    Cadastro de Gabarito")
print("-----------------------------")

for i in range(1, 6):
    alternativas = str(input("Resposta das questões: "))
    gabarito.append(alternativas)



os.system('cls')
print("ALUNO 1")
nome = str(input("Nome: "))
aluno.append(nome)
for c in range(1, 6):
    solu = str(input("Respostas dadas: "))
    Naluno1.append(solu)


os.system('cls')
print("ALUNO 2")
nome = str(input("Nome: "))
aluno.append(nome)
for c in range(1, 6):
    solu = str(input("Respostas dadas: "))
    Naluno2.append(solu)


os.system('cls')
print("ALUNO 3")
nome = str(input("Nome: "))
aluno.append(nome)
for c in range(1, 6):
    solu = str(input("Respostas dadas: "))
    Naluno3.append(solu)



for c in range(len(gabarito)):
    if Naluno1[c] == gabarito[c]:
        valor1 += 2

for c in range(len(gabarito)):
    if  Naluno2[c] == gabarito[c]:
        valor2 += 2

for c in range(len(gabarito)):
    if  Naluno3[c] == gabarito[c]:
        valor3 += 2


nota.append(valor1)
nota.append(valor2)
nota.append(valor3)

    
print(aluno[0], nota[0])
print(aluno[1], nota[1])
print(aluno[2], nota[2])    


      
    

