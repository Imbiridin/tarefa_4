total = 1

while True:
    numero = int(input("Digite um número para saber o seu fatorial: "))

    if numero > 16:
        print("Não pode números maiores que 16!")
        break
    elif numero <= 0:
        print("Não é possível calcular números negativos ou igual a zero!")
        break

    for i in range(1, numero + 1):
        total *= i
    
    continuar = input("Deseja continua?(s/n): ").lower()

    if continuar == 'n':
        break


print(f'{numero}.{i} = {total}')
