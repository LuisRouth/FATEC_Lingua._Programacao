numeros = input("Digite 5 números positivos separados por espaço: ").split()


for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

total = sum(numeros)
menor = min(numeros)
maior = max(numeros)

menor_soma = total - maior
maior_soma = total - menor

print(menor_soma, maior_soma) 