login = input("Digite seu novo USUARIO:")
senha = input("Digite sua nova SENHA:")

cara = False
especial = False

if len(senha) >= 8:
    cara = True

for char in senha:
    if char in "!@#$%&*":
        especial = True
        break

if not cara and not especial:
    print("É necessário ter pelo menos 8 caracteres e um caractere especial (ex: @, !, #).")
elif not cara:
    print("É necessário mais que 8 caracteres.")
elif not especial:
    print("É necessário pelo menos um caractere especial (ex: @, !, #).")
else:
    print("Login criado com sucesso!")