def fatorial(numero):
    resultado = 1
    for multiplicador in range(1, numero+1):
        resultado = resultado * multiplicador
    return resultado

numero = int(input("Digite um número para ser o fatorial: "))
if numero < 0:
    print("Erro, digite outro número")
else:
    print("O fatorial é", fatorial(numero))