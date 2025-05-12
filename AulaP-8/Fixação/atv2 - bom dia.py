frase = input("Digite uma frase: ")
frase.lower()
if frase.startswith("bom dia") and frase.endswith("obrigado"):
    print("Você escreveu bom dia e obrigado!")
elif frase.startswith("bom dia"):
    print("Você escreveu bom dia")
elif frase.endswith("obrigado"):
    print("Você escreveu obrigado!")
else:
    print("Sua frase não tem Bom dia ou obrigado!")
