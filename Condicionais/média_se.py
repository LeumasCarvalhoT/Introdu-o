nota1 = float(input("Escreva sua nota: "))
nota2 = float(input("Escreva sua outra nota: "))
media = (nota1 + nota2) / 2
if  (media >= 9.0) and (media <= 10):
    
    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: A")
    

elif (media >= 8 ) and (media <= 8.99):
    
    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: B")

elif (media >= 7 ) and (media <= 7.9):

    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: C")

elif (media >= 6 ) and (media <= 6.9):

    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: D")

elif (media >= 5) and (media <= 5.9):

    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: E")

elif (media < 5):

    print("Sua média é:", f"{media:.2f}")
    print("Aproveitamento: F")


    
    

    

    