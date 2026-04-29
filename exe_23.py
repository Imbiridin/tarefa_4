numero = int(input("Digite um número para saber se ele é PRIMO: "))

total = 0

primos = []

for numero_user in range(2, numero + 1):
    primo = True

    if numero < 2:
        print("Não é um número PRIMO")

    for i in range(2,int(numero_user**0.5)+1):
        total += 1
        if numero_user % i == 0:
            primo = False
            break
    if primo:
        primos.append(numero_user)

print("-" *50)
print(f"O número que você digitou: {numero}")
print(primos)
print(f'Total de divisões: {total}')
print("-" *50)