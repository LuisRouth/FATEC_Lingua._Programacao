idade = int(input("Digite a sua idade: "))
gestante = input("Você é gestante? (S/N): ")
deficiente = input("Você é deficiente? (S/N): ")

if idade >= 60 or deficiente == "S":
    print("Prioridade máxima")
elif gestante == "S":
    print("Prioridade média")
else:
    print("Atendimento normal")