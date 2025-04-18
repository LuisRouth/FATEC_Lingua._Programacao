idade = int(input("Digite a idade do atleta: "))

if idade <= 12:
    print("Categoria: Infantil")
elif idade <= 17:
    print("Categoria: Juvenil")
elif idade <= 40:
    print("Categoria: Adulto")
else:
    print("Categoria: Veterano")