
while True:
    numero = int(input("Digite um número para saber o seu fatorial: "))

    if numero > 16:
        print("Não pode números maiores que 16!")
        break
    elif numero <= 0:
        print("Não é possível calcular números negativos ou igual a zero!")
        break
    else:
        total = 1


    for i in range(1, numero + 1):
        total *= i
        print(f'{numero}.{i} = {total}')

    continuar = input("Deseja continua?(s/n): ").lower()

    if continuar == 'n':
        break

print(f'{total}')