boletim = {
    "Ana":     (8.0, 7.5),
    "Carlos":  (5.0, 6.0),
    "Beatriz": (9.0, 8.5),
    "Daniel":  (6.0, 6.5)
}

medias = {}
for nome, notas in boletim.items():
    medias[nome] = (notas[0] + notas[1]) / 2

print("Médias dos alunos:")
for nome, media in sorted(medias.items()):
    print(nome + ": " + str(round(media, 2)))

print("Aprovados:")
for nome, m in medias.items():
    if m >= 7.0:
        print(nome)

print("Reprovados:")
for nome, m in medias.items():
    if m < 7.0:
        print(nome)