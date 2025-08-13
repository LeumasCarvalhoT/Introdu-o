cigs = int(input("Quantos cigarros você fuma por dia?: "))
ano = int(input("Por quantos anos você já fuma: "))

def tempo_perdido(c, a):
    tc = c * 365 * a
    min = tc * 10
    d = min / (60 * 24) 
    return d

dias = tempo_perdido(cigs, ano)
print(f"O total de dias perdido por fumar foi de {dias:.0f} ")