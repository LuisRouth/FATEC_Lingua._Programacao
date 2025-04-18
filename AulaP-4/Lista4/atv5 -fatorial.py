numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("O número deve ser maior ou igual a zero.")
else:
    fatorial_for = 1
    for resultado in range(1, numero + 1):
        fatorial_for *= resultado

    fatorial_while = 1
    contador = numero
    while contador > 0:
        fatorial_while *= contador
        contador -= 1

    print("Usando for:", numero, "! =", fatorial_for)
    print("Usando while:", numero, "! =", fatorial_while)