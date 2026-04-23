num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

inicio = min(num_1, num_2)
fim = max(num_1, num_2)

print(f"O ínicio dos número é: {inicio} e o último número é: {fim}")

for i in range(inicio + 1, fim):
    print(f'{i}')