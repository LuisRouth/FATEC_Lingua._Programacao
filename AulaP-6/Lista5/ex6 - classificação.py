def classif(idade):
    if idade < 6:
     return "Idade inválida"
    elif idade <= 10:
     return "Lobinho"
    elif idade <= 14:
     return "Escoteiro"
    elif idade <= 17:
     return "Sênior"
    elif idade <= 21:
     return "Pioneiro"
    else:
     return "Líder"

idade = int(input("Digite a idade do escoteiro: "))
print("Categoria:", classif(idade))
