valor = int(input("Digite o valor da compra: "))

if valor >= 100:
    print("Você ganhou frete grátis!")
else:
    print("O valor total com o frete é" , valor + 15 )