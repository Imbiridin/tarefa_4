numero = []
minimo = 0
maximo = 0

while True:
    pergunta = int(input("Digite um número: "))

    if pergunta > 1000:
        print('*' * 50)
        print("Não é possível calcular número maior que Mil!")
        break
    elif pergunta < 0:
        print('*' * 50)
        print("Não é possível calcular números negativos!")
        break
    
    numero.append(pergunta)
    continuar = input('Gostaria de continuar?(s/n): ').lower()

    if pergunta == min(numero):
        minimo = pergunta
    if pergunta == max(numero):
        maximo = pergunta
    

    if continuar == 'n':
        break
    else:

        print(numero)

if minimo == maximo:
    soma = minimo
elif minimo < maximo:
    soma = minimo + maximo

print('*' * 50)
print(f'Os números digitados são: {numero}')
print(f'O valor mínimo digitado é: {minimo}')
print(f'O maior valor digitado é: {maximo}') 
print(f'A soma dos 2 valores(minímo e máximo) é: {soma}')  
print('*' * 50)
    
    

