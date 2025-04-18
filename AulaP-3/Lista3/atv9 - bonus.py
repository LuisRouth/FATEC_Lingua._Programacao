salario = int(input("Digite seu salário atual: "))
if salario < 2000:
 bonus = salario * 0.2
 salario_novo = salario + bonus
 print ("Você recebeu um bónus de 20%, seu salário agora é: " , salario_novo )
elif salario >= 2000 and salario <= 5000:
 bonus = salario * 0.1
 salario_novo = salario + bonus
 print ("Você recebeu um bónus de 10%, seu salário agora é: " , salario_novo )
else:
 bonus = salario * 0.05
 salario_novo = salario + bonus
 print ("Você recebeu um bónus de 5%, seu salário agora é: " , salario_novo )