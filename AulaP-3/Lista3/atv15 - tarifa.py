idade = int(input("Digite sua idade: "))
estudante = (input("Digite(S/N) se você tem carteira de estudante: "))

if estudante == "S":
    print("Você tem 50% de desconto")
elif idade <= 6 or idade >=65:
    print("Você tem acesso de graça")
else:
    print ("Você paga normal")
             
