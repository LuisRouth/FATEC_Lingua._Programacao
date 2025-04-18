salario = int(input("Digite seu salário: "))

if salario > 4600:
    imposto = salario * 0.275
    print("Você pagara:" , imposto)
elif salario >= 3700:
    imposto = salario * 0.225
    print("Você pagara:" , imposto)
elif salario >= 2800:
    imposto = salario * 0.15
    print("Você pagara:" , imposto)
elif salario >= 1900:
    imposto = salario * 0.75
    print("Você pagara:" , imposto)
else:
    print("Você esta isento")
