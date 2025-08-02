bgol = int(input("Quantos gols fez Bangu?: "))
mgol = int(input("Quantos gols fez Madureira?: "))
soma = int (bgol - mgol)

if (soma == 0):
    print("DIFERENÇA ", soma)
    print("STATUS: EMPATE!")

elif (soma >= 1) and (soma <= 3):
    print("DIFERENÇA ", soma)
    print("STATUS: partida normal")

elif (soma >= 4):
    print("DIFERENÇA ", soma)
    print("STATUS: GOLEADA!")