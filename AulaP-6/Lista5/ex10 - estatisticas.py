M = 0
F = 0
idadeh = 0
idadem = 0
contadorh = 0
contadorm = 0

for aluno in range(1, 11):
    genero = input("Aluno " + str(aluno) + ", digite seu gênero (M/F): ")
    idade = int(input("Aluno " + str(aluno) + ", digite sua idade: "))
    
    if genero == 'M':
        M += 1
        idadeh += idade
        contadorh += 1
    elif genero == 'F':
        F += 1
        idadem += idade
        contadorm += 1

if contadorh > 0:
    mediah = idadeh / contadorh
else:
    mediah = 0
print("Total de homens cadastrados:",M)   
print("Média de idade dos homens:",mediah)

if contadorm > 0:
    mediam = idadem / contadorm
else:
    mediam = 0
print("Total de mulheres cadastradas:",F)
print("Média de idade das mulheres:",mediam)