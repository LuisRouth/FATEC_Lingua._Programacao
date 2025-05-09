lista2 = list(range(5,16))
lista1 = list(range(1,10))

lista_resultado = []
for item in lista1:
    if not item in lista_resultado:
        lista_resultado.append(item)
for item in lista2:
    if not item in lista_resultado:
        lista_resultado.append(item)

print (lista_resultado)

"""
Outra forma de fazer
lista3 = list(set(lista1 + lista2))
print lista3
"""