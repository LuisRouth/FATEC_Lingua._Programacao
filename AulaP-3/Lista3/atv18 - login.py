
usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "usuario" and senha == "123":
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos. Tente novamente.")
    # Segunda tentativa
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario == "usuario" and senha == "123":
        print("Login bem-sucedido")
    else:
        print("Usuário ou senha incorretos. Última tentativa.")
       
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        if usuario == "usuario" and senha == "123":
            print("Login bem-sucedido")
        else:
            print("Acesso bloqueado")