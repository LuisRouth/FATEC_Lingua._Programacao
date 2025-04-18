def conta(salario, aliquota, parcela):
    return (salario * aliquota) - parcela

salario = float(input("Digite seu salário bruto: "))

aliquota = 0
parcela = 0

if salario > 4664.68:
    aliquota = 0.275
    parcela = 884.96
elif salario >= 3751.06:
    aliquota = 0.225
    parcela = 651.73
elif salario >= 2826.66:
    aliquota = 0.15
    parcela = 370.40
elif salario >= 2112.01:
    aliquota = 0.075
    parcela = 158.40
else:
    print("Você está isento, não há imposto a pagar.")

imposto = conta(salario, aliquota, parcela)
print ("Seu imposto é R$",imposto)