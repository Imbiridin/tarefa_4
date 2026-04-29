turma = []

while True:
    idade = int(input("Digite a sua idade: "))
    turma.append(idade)

    continuar = input("Gostaria de continuar?(s/n): ").lower()

    if continuar == 'n':
        break

media = sum(turma) / len(turma)

print(turma)

if media >= 60:
    print("A maior parte da turma é composta de Idosos!")
elif media < 60 and media >= 18:
    print("A maior parte da turma é composta por Adultos!")
else:
    print("A mair parte da turma é composta por Crianças!")

 