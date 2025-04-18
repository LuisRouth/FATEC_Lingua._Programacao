valor = int(input("Digite quantos reais você tem: "))

novo_valor= 0
notas_100 = 0
notas_50  = 0
notas_20  = 0
notas_10  = 0
notas_5   = 0
notas_2   = 0

if valor >= 100:
 while valor >= 100:
  notas_100 += 1
  valor -= 100

if valor >= 50:
 while valor >= 50:
  notas_50 += 1
  valor -= 50

if valor >= 20:
 while valor >= 20:
  notas_20 += 1
  valor -= 20

if valor >= 10:
 while valor >= 10:
  notas_10 += 1
  valor -= 10

if valor >= 5:
 while valor >= 5:
   notas_5 += 1
   valor -= 5

if valor >= 2:
 while valor >= 2:
   notas_2 += 1
   valor -= 2

print (" vc tem",notas_100,"notas de $100,",notas_50,"notas de $50,",notas_20,"notas de $20,",notas_10,"notas de $10",notas_5,"notas de $5,",notas_2,"notas de $2, e o resto foi $",valor)
