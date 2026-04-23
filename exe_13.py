num_base = int(input("Digite um número: "))
num_expoente = int(input("Digite um número: "))

elevado = 1

for i in range(num_expoente):
    elevado = elevado * num_base
print(f'O número base é: {num_base}. E o número expoente é: {num_expoente}. Os 2 elevados são: {elevado}')