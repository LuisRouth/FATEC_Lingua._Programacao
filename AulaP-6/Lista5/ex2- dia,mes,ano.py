def data(dia,mes,ano):
    return f"{dia} de {nome_mes} de {ano}"

dia = int(input("Digite o dia: "))
if dia > 31:
 print ("Insira um dia valido,esse dia não existe")
else:
 mes = int(input("Digite o mês: "))
 if mes > 12:
  print ("Insira um mês valido,esse mês não existe")
 else:
    if mes == 1:
     nome_mes = "janeiro"
    elif mes == 2:
     nome_mes = "fevereiro"
    elif mes == 3:
     nome_mes = "março"
    elif mes == 4:
     nome_mes = "abril"
    elif mes == 5:
     nome_mes = "maio"
    elif mes == 6:
     nome_mes = "junho"
    elif mes == 7:
     nome_mes = "julho"
    elif mes == 8:
     nome_mes = "agosto"
    elif mes == 9:
     nome_mes = "setembro"
    elif mes == 10:
     nome_mes = "outubro"
    elif mes == 11:
     nome_mes = "novembro"
    elif mes == 12:
     nome_mes = "dezembro"

    ano = int(input("Digite o ano: "))
    print (dia,"de",nome_mes,"de",ano)