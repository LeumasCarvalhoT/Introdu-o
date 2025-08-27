vetor = []
v = 0

for i in range(1, 5):
    v = int(input("Digite um valor: "))
    vetor.append(v)


for i in range(len(vetor)-1):
    for j in range(i+1,len(vetor)):
        if (vetor[i] > vetor[j]):
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

        
for i in range(len(vetor)):
    print( "{",vetor[i],"}",end=' ')