valor = int(input("Digite o valor do saque: "))

if valor >= 100:
    notas_100 = valor // 100
    valor = valor % 100
else:
    notas_100 = 0

if valor >= 50:
    notas_50 = valor // 50
    valor = valor % 50
else:
    notas_50 = 0

if valor >= 20:
    notas_20 = valor // 20
    valor = valor % 20
else:
    notas_20 = 0

if valor >= 10:
    notas_10 = valor // 10
    valor = valor % 10
else:
    notas_10 = 0

print("Notas de R$ 100:", notas_100)
print("Notas de R$ 50:", notas_50)
print("Notas de R$ 20:", notas_20)
print("Notas de R$ 10:", notas_10)