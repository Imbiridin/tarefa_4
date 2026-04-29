numero = int(input("Digite um número para saber o seu fatorial: "))
total = 1

for i in range(1, numero + 1):
    total *= i
    print(f'{numero}.{i} = {total}')