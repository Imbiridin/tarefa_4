numero = 0

for i in range(1,6):
    numero_1 = int(input("Digite um número para saber a média dele: "))
    numero += numero_1

media = numero / 5  
print(f'Soma total {numero}')  
print(f'Media dos números {media}')
