par = 0
impar = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        par += 1
        print("par")
    else:
        impar += 1
        print("ímpar")

print(f'O total de número par é: {par}')
print(f'O total de número ímpar é: {impar}')

    