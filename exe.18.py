numero = []
minimo = 0
maximo = 0

while True:
    pergunta = int(input("Digite um número: "))
    numero.append(pergunta)
    continuar = input('Gostaria de continuar?(s/n): ').lower()

    if pergunta == min(numero):
        minimo = pergunta
    if pergunta == max(numero):
        maximo = pergunta

    soma = minimo + maximo

    if continuar == 'n':
        break
    else:
        print(numero)
    
    

print(f'Os números digitados são: {numero}')
print(f'O valor mínimo digitado é: {minimo}')
print(f'O maior valor digitado é: {maximo}')
print(f'A soma dos 2 valores(minímo e máximo) é: {soma}')