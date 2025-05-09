def romano(n):
    mapa = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
        (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
        (1,    "I"),
    ]
    resultado = ""
    for valor, simbolo in mapa:
        repeticoes = n // valor
        if repeticoes:
            resultado += simbolo * repeticoes
            n %= valor
    return resultado

entrada = input("Digite um número inteiro entre 1 e 3999: ")
n = int(entrada)

if 1 <= n <= 3999:
    print(romano(n))
else:
    print("Valor fora do intervalo permitido (1–3999).")