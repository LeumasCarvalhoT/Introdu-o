produto = float(input("Qual o valor do produto: "))
desconto = float(input("Por quanto quer descontar?: "))

def desc(p, d):
    r = p - (p * d/100 )
    return r

resultado = desc(produto, desconto)
print(f"O produto ficará por: {resultado:.2f}")