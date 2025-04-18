ladoa = int(input("Digite um número para ser o lado A de um triângulo: "))
ladob = int(input("Outro número para ser o lado B de um triângulo: "))
ladoc = int(input("O ultimo número para ser o lado C de um triângulo: "))
if not ladoa < ladob + ladoc and ladob < ladoa + ladoc and ladoc < ladoa + ladob:
    print("Não é possível formar um triângulo com esses lados!")
elif ladoa == ladob == ladoc:
    print("Isso é um triângulo equilátero")
elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print("Isso é um triângulo Isósceles")
else:
    print("Isso é um triângulo escaleno")