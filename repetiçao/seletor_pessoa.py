print("===================")
print("Seletor de Pessoas")
print("===================")

F = 0
M = 0
resp = 's'

while resp.lower() == 's':

    print("--------------")
    sexo = str(input("Qual o sexo?[M/F]: "))
    idade = int(input("Qual a idade?: "))
    print("--------------")

    print("[1] PRETO")
    print("[2] CASTANHO")
    print("[3] LOIRO")
    print("[4] RUIVO")
    cabelo = int(input("Qual a cor do cabelo?: "))

    if ((sexo == "f") or (sexo == "F")) and (cabelo == 3) and (idade >= 18):
        F += 1

    elif ((sexo == "m") or (sexo == "M")) and (cabelo == 2) and (idade >= 18):
        M += 1


    resp = str(input("Quer continuar?[S/N]: "))


print("Ha ao todo", F," de mulheres adultas de cabelos loiros.")
print("Há ao todo", M," de homens adultos de cabelos castanhos.")



