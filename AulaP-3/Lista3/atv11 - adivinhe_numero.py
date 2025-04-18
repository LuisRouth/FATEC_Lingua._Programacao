import time
numero_secreto = (int(time.time()) % 100) + 1

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while True:
    print (" ")
    print ("Qual número você acha que é?")
    tentativa = int(input("Seu chute: "))

    if tentativa > numero_secreto: 
     print("Muito alto!")
    elif tentativa < numero_secreto:
        print("Muito baixo!")
    else:
        print("Parabéns! Você acertou!")
        break