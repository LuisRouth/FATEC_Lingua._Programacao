peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Você esta abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Você esta com peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Você esta com sobrepeso")
else:
    print("Você tem Obesidade")
