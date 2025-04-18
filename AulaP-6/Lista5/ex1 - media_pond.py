def nota(lab, av, ex):
    return (lab * 2 + av * 3 + ex * 5) / 10
lab = float(input("Digite sua primeira nota: "))
av = float(input("Digite sua segunda nota: "))
ex = float(input("Digite sua terceira nota: "))

media = nota(lab, av, ex)

if media < 4.9:
    print ("Sua nota é",media,",você tirou E!")
elif media < 5.9:
    print ("Sua nota é",media,",você tirou D!")
elif media < 6.9:
    print ("Sua nota é",media,",você tirou C!")
elif media < 7.9:
    print ("Sua nota é",media,",você tirou B!")
else:
    print ("Sua nota é",media,",você tirou A!")