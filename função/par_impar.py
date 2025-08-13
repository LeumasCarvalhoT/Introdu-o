n = int(input("Digite um número: "))

def resto(a):
    if a%2 == 0:
        return 'PAR'
    else:
        return 'IMPAR' 
    

r = resto(n)

print("O valor de", n, " é", r)