def festa(idade):
    if idade < 14:
        return "Não pode entrar", "Não pode beber"
    elif idade < 18:
        return "Pode com acompanhamento dos pais", "Não pode beber"
    else:
        return "Pode Entrar", "Pode Beber"

idade = int(input("Digite sua idade: "))
entrada, bebida = festa(idade)

print("Condição para entrar na festa:", entrada)
print("Condição para beber:", bebida)
