numero = []

while True:
    nota = float(input("Digite a nota: "))
    numero.append(nota)


    continuar = input("Deseja continuar?(s/n): ").lower()

    if continuar == 'n':
        break

media = sum(numero) / len(numero)

print("-" * 30)
print(f"Notas digitadas: {numero}")
print(f"A média final é: {media:.2f}") # .2f formata para 2 casas decimais
print("-" * 30)