

while True:
    numero = int(input("Diite um número: "))

    if numero >= 0 and numero <= 10:
        break

for i in range(1,6):
    print(f'Tentativas: {i}')
    if numero >= 0 and numero <= 10:
        print(f'Nota: {numero}')
        break
    else:
        print("Valor inválido")
print("ACABOU O PROGRAMA")