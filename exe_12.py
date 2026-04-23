numero = int(input("Digite um número para saber a tabuada: "))

for i in range(1,11):
    tabuada = numero * i
    print(f'{numero} x {i} = {tabuada}')