pala = input("Digite uma palavra: ")
inv = pala[::-1]
print(inv)

if pala == inv:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
