preco_original = float(input("Digite o valor original do produto: "))
desconto = float(input("Digite o valor de desconto: "))
preco_final = (preco_original - (preco_original / 100) * desconto )
print ("O produto que custava " , preco_original , " com o desconto de " , desconto , " agora custa " , preco_final)