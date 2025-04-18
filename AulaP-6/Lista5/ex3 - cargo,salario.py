def salari (salar,benef,impost):
  total = salar + benef
  return int(total - (total * impost / 100))
salrio = salari
cargo = int(input("Digite seu codigo do cargo: "))
if cargo == 1:
 cargo = "Escriturário"
 salario = salari(2500,300,8)
elif cargo == 2:
 cargo = "Secretário"
 salario = salari(3200,450,10)
elif cargo == 3:
 cargo = "Caixa"
 salario = salari(3800,600,12)
elif cargo == 4:
 cargo = "Gerente"
 salario = salari(7500,1000,15)
elif cargo == 5:
 cargo = "Diretor"
 salario = salari(12000,2000,20)

print ("Bem vindo",cargo,"! Seu salário total é de R$",salario)
