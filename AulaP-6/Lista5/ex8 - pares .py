def soma():
    total = 0
    for par in range(2, 101, 2):
        total += par
    return total
print("A soma dos 50 primeiros números pares é:", soma())