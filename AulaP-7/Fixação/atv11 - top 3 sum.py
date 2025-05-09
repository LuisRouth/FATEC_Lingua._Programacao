numeros = [10, 3, 5, 7, 2, 8, 12]
ordenado = sorted(numeros)

somamenor = sum(ordenado[:3])
somamaior = sum(ordenado[-3:])

print(somamaior, somamenor)